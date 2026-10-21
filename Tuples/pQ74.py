# create a tuple of 5 of your favourite songs. Print the first, last and middle one using indexing.
songs_tuple = ("I'm Unstoppable", "If you Believe", "Rise Again", "Shabasiyan", "I was never born to follow")
print(f"First Song = {songs_tuple[0]}")
n = len(songs_tuple)
middle = n//2
print(f"Middle Song = {songs_tuple[middle]}")
print(f"Last Song = {songs_tuple[-1]}")
