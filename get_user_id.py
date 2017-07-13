# Here we define a function named as"get_user_id"this will provide you users id
APP_ACCESS_TOKEN = '2121110795.18f49b6.01ec923fb3fd4f3bab2327368fd4e839'
BASE_URL = 'https://api.instagram.com/v1/'

import requests
def get_user_id(insta_username):
    # Function Logic to get user id
    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print( user_info['data'][0]['id'])
            return user_info['data'][0]['id']
        else:
            return None
    else:
        print '\n\t\t*****Status code other than 200 received!*****'
        exit()
