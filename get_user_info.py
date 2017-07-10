# here we define a function named as"get_useer_info" to get the user information.
from get_user_id import  get_user_id
import requests
APP_ACCESS_TOKEN = ' 2121110795.f566e63.45b3d45844144983bd2217db985ca244'
BASE_URL = 'https://api.instagram.com/v1/'


def get_user_info(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print "User does not exist"
        exit()

    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username: %s' % (user_info['data']['username'])
            print 'Number of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'Number of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'Number of posts: %s' % (user_info['data']['counts']['media'])
        else:
            print 'There is no data for this user!'
    else:
        print 'Status code other than 200 received!'
