
APP_ACCESS_TOKEN = '2121110795.18f49b6.01ec923fb3fd4f3bab2327368fd4e839'
BASE_URL = 'https://api.instagram.com/v1/'
import requests
import urllib
from get_post_id import get_post_id

def like_user_post(insta_username):
    # Function Logic to Like User's Recent Post

    media_id = get_post_id(insta_username)
    print(media_id)
    request_url = (BASE_URL + "media/"+media_id+"/likes")
    payload = {"access_token" : APP_ACCESS_TOKEN}
    post_a_like = requests.post(request_url,payload).json()
    if post_a_like['meta']['code'] == 200:
        print '\n\t\t*****Like was successful!*****'
    else:
        print '\n\t\t*****Your like was unsuccessful. Try again!*****'