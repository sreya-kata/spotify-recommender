import os
from spotify import Spotify

def main():
    spotify_client = Spotify(os.getenv("SPOTIFY_AUTHORIZATION_TOKEN"),
                             os.getenv("SPOTIFY_USER_ID"))
    num_tracks = 0
    while True:
        try:
            num_tracks = int(input("How many tracks would you like to visualize: "))
            break
        except ValueError:
            continue
            
    last_played_tracks = spotify_client.get_recently_played(num_tracks)
    
    print(f"Here are the last {num_tracks} you listened to: ")
    for i, track in enumerate(last_played_tracks):
        print(f"{i+1} - {track}")
        
    # choose which tracks to use as seed here
    indices = input("Enter up to 5 tracks you would like to use as seeds (indices separated by space) ")
    indices = indices.split()
    seed_tracks = [last_played_tracks[int(index) - 1] for index in indices]
    
    # get recommended tracks based on seeds
    recommended_tracks = spotify_client.get_recommendations(seed_tracks)
    print("Here is a list of recommended tracks in your new playlist: ")
    for i, track in enumerate(recommended_tracks):
        print(f"{i+1} - {track}")
    
    playlist_name = input("What is the name of your new playlist? ")
    playlist = spotify_client.create_playlist(playlist_name)
    print(f"Playlist '{playlist_name}' successfully created!")
    
    # fill the new playlist with the recommended tracks
    spotify_client.fill_playlist(playlist, recommended_tracks)
    print(f"Your recommended tracks were added to playlist '{playlist_name}'")

if __name__ == "__main__":
	main()