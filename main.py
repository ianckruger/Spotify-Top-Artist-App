from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json

load_dotenv()
# automatically loads in the enviornment

# load in client ID and secret
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")


# authorization differs based on api
# will be using query api for spotify library using
# client credential workflow

# another api that will control spotify player

# request access token
# need to send grant_type to /api/token
# needs to be encoded in application/x-www-form-urlencoded

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
    # returns a bse 64 object that we convert into a string 

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type":"client_credentials"}
    # send a post request
    result = post(url, headers=headers, data=data)
    # convert JSON string to python dictionary
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}


def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"q={artist_name}&type=artist&limit=1" # there are optional args, we are only finding most popular artist
    # combine query and url
    query_url = url+"?"+query

    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]
    if len(json_result) == 0:
        print("No artist found")
        return None
    
    return json_result[0]

def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result

