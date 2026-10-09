playlist = ["Levitating", "As It Was", "Blinding Lights"]

print(f"Starting with {len(playlist)} songs") #Starting with 3 songs 
print(playlist[0]) #Levitating 
print(playlist[-1]) #Blinding Lights 

playlist.append("Flowers") 
playlist.append("Espresso")
print(f"Now {len(playlist)} songs") #Now 5 songs 

now_playing = playlist.pop(0)
print(f"Now playing: {now_playing}") #Now playing: Levitating 
print(f"{len(playlist)} left in the queue") #4 left in the queue

playlist.insert(1, "Golden Hour") 
print(f"Next up after this one: {playlist[1:3]}") #Next up after this one: Golden Hour 

if "Gone" in playlist:
    playlist.remove("Gone")
    print("Removed Gone by request") #Removed Flowers by request 
else: 
    print("Song not in playlist, cannot be removed")

playlist.insert(4, "Undressed")

print(playlist)

#,As it was, Golden hour,  blinding lights, Espresso 
