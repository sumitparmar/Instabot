#here we define a function named as "self_info"
from main import APP_ACCESS_TOKEN
from main import BASE_URL
import requests

def self_info():
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username: %s' %(user_info['data']['username'])
            print 'Number of followers: %s' %(user_info['data']['counts']['followed_by'])
            print 'No of people you are following: %s' %(user_info['data']['counts']['following'])
            print 'Number of posts %s' %(user_info['data']['counts']['media'])
        else:
            print 'User Does Not Exist'
    else:
        print'status code other than 200 recieved!'



