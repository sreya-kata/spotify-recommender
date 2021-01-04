# spotify-recommender
Python application to read a user's recent songs and curate a playlist of recommended songs based on seeded recent songs

## Install
Need to -pip install:
* requests

## Run
Need to export/create two environment variables:
* SPOTIFY_AUTHORIZATION_TOKEN={OAuth Code generated from https://developer.spotify.com/console/post-playlists/)
* SPOTIFY_USER_ID={user_id}

Run the entry-point script and follow the console instructions:
python create.py
