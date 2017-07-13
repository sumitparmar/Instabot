from get_user_id import get_user_id
APP_ACCESS_TOKEN = '2121110795.18f49b6.01ec923fb3fd4f3bab2327368fd4e839'
BASE_URL = 'https://api.instagram.com/v1/'
import requests

def get_post_id(insta_username):
    # Function Logic to show the post id

    user_id = get_user_id(insta_username)   #Get the User's Id
    if user_id == None:
        print '\n\t\t*****User does not exist!*****'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            return user_media['data'][0]['id']
        else:
            print '\n\t\t*****There is no recent post of the user!*****'
            exit()
    else:
        print '\n\t\t*****Status code other than 200 received!*****'
        exit()