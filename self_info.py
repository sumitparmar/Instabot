# *** here we define a function named as "self_info".***

APP_ACCESS_TOKEN = ' 2121110795.f566e63.45b3d45844144983bd2217db985ca244'
BASE_URL = 'https://api.instagram.com/v1/'
import requests
import urllib


def self_info():
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username: %s' %(user_info['data']['username'])
            print 'Number of followers: %s' %(user_info['data']['counts']['followed_by'])
            print 'Number of people you are following: %s' %(user_info['data']['counts']['follows'])
            print 'Number of posts %s' %(user_info['data']['counts']['media'])
        else:
            print 'User Does Not Exist'
    else:
        print'status code other than 200 recieved!'



