import requests
import json
import tweepy as tw
#ToDo API credentials from config
ACCESS_TOKEN="129606474-PRkkJKsPptFpxuaDAKTvdE95tvtLQw3Tax26eiFU"
ACCESS_TOKEN_SECRET="s2rvgKP2fLFdnDVpxvCxRELXEpoifDq4frSBLn55v3uac"
API_KEY="kwrpezsdCNFZBzvI2YXgzK7s9"
API_SECRET_KEY="mjE0EZ2KiFz9VGLvYTeymMPXaWlvcBb3Hkmt10qdip4YBO5cmZ"
BEARER_TOKEN:"AAAAAAAAAAAAAAAAAAAAAMl2RAEAAAAAwKy7h%2FTPbvyNWC6yjo5gQEbE8QE%3DgJhQuP2fOBXTFc0up3QvPSS5begr6kpS4itJsHSk4ypFbriGFF"

auth = tw.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tw.API(auth)

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {BEARER_TOKEN}"
    # r.headers["User-Agent"] = "eob_twitter_miner"
    return r


def connect_to_endpoint_v2(url):
    response = requests.request("GET", url, auth=bearer_oauth,)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()

def get_profile_data(username:str):
    # user=username
    # user_fields="user.fields=created_at,description,entities,id,location,name,profile_image_url,public_metrics,url,username,verified"
    # url="https://api.twitter.com/2/users/by/username/{}?{}".format(user, user_fields)
    # json_response = connect_to_endpoint(url)
    json_response = api.get_user(username)._json
    return json_response

def get_profile_tweets(username:str, n:int):
    """ Get @username last @n tweets"""
    json_response = api.user_timeline(
            id=username, count=n, tweet_mode="extended")
    return json_response