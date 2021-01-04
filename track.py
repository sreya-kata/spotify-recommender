class Track:
    
    # Represents a single track on Spotify
    def __init__(self, title, id, artist):
        self.title = title
        self.id = id
        self.artist = artist
        
    def create_spotify_uri(self):
        return f"spotify:track:{self.id}"
    
    def __str__(self):
        return f"{self.title} by {self.artist}"