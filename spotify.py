import json
import requests

from track import Track
from playlist import Playlist

class Spotify:
    
    # Represents things done using the Spotify API 
    def __init__(self, authorization_token, user_id):
        self.authorization_token = authorization_token
        self.user_id = user_id
        
    def get_recently_played(self, num=10):
        # Gets the last n recently played songs from a user
        url = f"https://api.spotify.com/v1/me/player/recently-played?limit={num}"
        response = self.get_api_request(url)
        response_json = response.json()
        print(response_json)
        tracks = [Track(track["track"]["name"], track["track"]["id"], track["track"]["artists"][0]["name"])
                 for track in response_json["items"]]
        return tracks
    
    def get_api_request(self, url):
        response = requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.authorization_token}"
            }
        )
        print(response)
        return response
    
    def create_playlist(self, name):
        data = json.dumps({
            "name": name,
            "description": "Recommended Tracks",
            "public": True
        })
        url = f"https://api.spotify.com/v1/users/{self.user_id}/playlists"
        response = self.post_api_request(url, data)
        response_json = response.json()
        
        playlist_id = response_json["id"]
        playlist = Playlist(name, playlist_id)
        return playlist
    
    def fill_playlist(self, playlist, tracks):
        # Populates the given playlist with the given tracks using a POST request
        track_urls = [track.create_spotify_uri() for track in tracks]
        data = json.dumps(track_urls)
        url = f"https://api.spotify.com/v1/playlists/{playlist.id}/tracks"
        response = self.post_api_request(url, data)
        response_json = response.json()
        return response_json
        
    def post_api_request(self, url, data):
        response = requests.post(
            url, 
            data = data,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.authorization_token}"
            }
        )
        return response
    
    def get_recommendations(self, seed_tracks, limit=50):
        # Gets a list of recommended tracks based on the number of seed tracks
        
        seed_tracks_url = ""
        for seed_track in seed_tracks:
            seed_tracks_url += seed_track.id + ","
        seed_tracks_url = seed_tracks_url[:-1]
        url = f"https://api.spotify.com/v1/recommendations?seed_tracks={seed_tracks_url}&limit={limit}"
        response = self.get_api_request(url)
        response_json = response.json()
        tracks = [Track(track["name"], track["id"], track["artists"][0]["name"])
                 for track in response_json["tracks"]]
        return tracks