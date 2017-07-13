APP_ACCESS_TOKEN = '2121110795.18f49b6.01ec923fb3fd4f3bab2327368fd4e839'
BASE_URL = 'https://api.instagram.com/v1/'


import urllib
import requests
from get_user_id import  get_user_id



def get_user_post(insta_username):
    user_id = get_user_id(insta_username)  # Get the User's Id
    if user_id == None:
        print '\n\t\t*****User does not exist!*****'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:  # Check if there is any user or not
        if len(user_media['data']):
            image_name = user_media['data'][0]['id'] + '.jpeg'
            image_url = user_media['data'][0]['images']['standard_resolution']['url']
            (urllib.urlretrieve(image_url, image_name))
            print(user_media['data'][0]['id'])
            print "\n\t\t*****User's Recent Post has been downloaded!*****"
            return user_media['data'][0]['id']

        else:
            print '\n\t\t*****Post does not exist!*****'
    else:
        print '\n\t\t*****Status code other than 200 received!*****'
