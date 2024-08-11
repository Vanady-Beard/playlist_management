from flask import Flask, request, jsonify 
from playlist import Songs

# Create Song
# Update Song
# Delete Song
# Search/Get a Song

app = Flask(__name__)

playlist =Songs()

@app.route('/create', methods=['POST'])
def create ():
        song_title = request.json.get('title')
        if not song_title:
                return jsonify({"error": "Need to provide a song title."}), 400
        playlist.append(song_title)
        return jsonify({"message": f"Song '{song_title}' added to the playlist."}), 201

@app.route('/update', methods=['PUT'])
def update():
        old_title = request.json.get('old_title')
        new_title = request.json.get ('new_title')
        if not old_title or not new_title:
             return jsonify({"error": "Both old and new song title must be given."})
        
        current = playlist.head
        while current:
                if current.songs == old_title:
                        current.songs = new_title
                        return jsonify({"message": f"Song '{old_title} updated to '{new_title}'."})
                current = current.next
        return jsonify ({"error": f"Song '{old_title}' not found in the playlist."})



@app.route('/delete', methods=['DELETE'])
def delete():
        deleted_song = playlist.delete()
        if deleted_song == "Your playlist is empty. Nothing to delete.":
                return jsonify ({"error":deleted_song}), 404
        return jsonify({"message": f"Deleted song: {deleted_song}"}), 200


@app.route('/search', methods=['GET'])
def search():
        song_title = request.args.get('title')
        if not song_title:
                return jsonify ({"error": "No song title provided"}), 400
        result = playlist.search_song(song_title)
        return jsonify({"result": result}), 200

@app.route('/songs', methods=['GET'])
def get_all_songs():
    songs = []
    current = playlist.head
    while current:
        songs.append(current.songs)
        current = current.next
    return jsonify({"songs": songs}), 200



if __name__ == '__main__':
        app.run(debug=True)





