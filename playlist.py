# song_list ={
# "Sicko Mode": "Travis Scott",
# "HUMBLE": "Kendrick Lamar",
# "God's Plan": "Drake",
# "Lose Yourself": "Eminem",
# "Juicy": "The Notorious B.I.G."}

# song_list["HUMBLE"]
 

#   Is queue is first in, first out 

class Node():
    def __init__ (self, songs):
        self.songs = songs
        self.next = None
        self.prev = None
class Songs():
    def __init__ (self):
        self.head = None
        self.tail = None


    def append (self,songs):
        songs = Node(songs)
        if self.head is None:
           self.head = songs  
           self.tail = songs
        else:
            self.tail.next = songs
            songs.prev = self.tail
            self.tail  = songs 
        
        # print (f"Added to your playlist: {songs.songs}")
         
    def delete (self):
        if self.head is None:
            return ("Their is not any songs in your playlist to delete.")
        else:
            remove = self.head
            self.head = self.head.next
        if self.head:
            self.head.prev = None

        return remove.songs
    
    def all_songs(self):
        current = self.head
        if current is None:
            return "The playlist is empty."
        while current:
            print(current.songs)
            current = current.next

        
    def to_list(self):
        
        current = self.head
        songs_list = []
        while current:
            songs_list.append(current.songs)
            current = current.next
        return songs_list

    def sort_by_name(self):
       
        songs_list = self.to_list()
        bubble_sort(songs_list)
        for song in songs_list:
            print(song)

    def search_song(self, target):
        
        songs_list = self.to_list()
        songs_list.sort()  
        index = binary_search(songs_list, target)
        if index is not None:
            return f"Song '{target}' found at position {index}."
        else:
            return f"Song '{target}' not found in the playlist."
       


def bubble_sort (list):
    n = len(list)
    for i in range(n):
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

def binary_search (list, target):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low + high)//2
        if list[mid] < target:
            low = mid + 1
        elif list[mid] > target:
            high = mid -1 
        else:
            return mid
    return None

playlistSongs = Songs()


playlistSongs.append("Dark Clouds: Rod Wave")
playlistSongs.append("Sicko Mode: Travis Scott")
playlistSongs.append("HUMBLE: Kendrick Lamar")
playlistSongs.append("God's Plan: Drake")
playlistSongs.append ("Lose Yourself:Eminem")
playlistSongs.append("Juicy: The Notorious B.I.G.")
playlistSongs.append("Love Yourz: J.Cole")


print(f"Deleted Songs : {playlistSongs.delete()}")

deleted_songs = playlistSongs.delete()

print(f"Deleted Songs: {deleted_songs} ")

playlistSongs.all_songs()

search_result = playlistSongs.search_song("God's Plan: Drake")
print(f"\nNext Song: {search_result}")



print('===============================')

print("Current playlist")

playlistSongs.all_songs()

