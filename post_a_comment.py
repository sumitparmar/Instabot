

APP_ACCESS_TOKEN = ' 2121110795.f566e63.45b3d45844144983bd2217db985ca244'
BASE_URL = 'https://api.instagram.com/v1/'
import requests
import urllib

from get_user_post import get_user_post

def comment_user_post1(insta_username):
    #Function Logic for post a Comment

    post_id = get_user_post(insta_username)   #Get the User's Post Id
    message = raw_input("\n\tPlease Enter Your comment : \n")
    request_url = (BASE_URL + 'media/%s/comments') % (post_id)
    payload = {"access_token":APP_ACCESS_TOKEN, "text": message}
    post_a_comment = requests.post(request_url, payload).json()
    print 'POST request url : %s' % (request_url)

    print(post_a_comment['meta']['code'])   #Check if Comment is Posted Or Not
    if post_a_comment['meta']['code'] == 200:
        print("\n\t\t\t*****Post comment successfully*****")
    else :
        print("\n\t\t\t*****Post comment Unsuccessfull*****")
