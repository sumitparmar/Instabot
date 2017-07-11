
APP_ACCESS_TOKEN = ' 2121110795.f566e63.45b3d45844144983bd2217db985ca244'
BASE_URL = 'https://api.instagram.com/v1/'
import requests
import urllib
import  textblob
from get_post_id import  get_post_id
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer





# *** here we define a fuction named as delete_negative_comment to delete the wrong comments.***

def delete_negative_comment(insta_username):

    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    comment_info = requests.get(request_url).json()

    if comment_info['meta']['code'] == 200:
        if len(comment_info['data']):
            #Here's a naive implementation of how to delete the negative comments :)
            for x in range(0, len(comment_info['data'])):
                comment_id = comment_info['data'][x]['id']
                comment_text = comment_info['data'][x]['text']
                blob = TextBlob(comment_text, analyzer=NaiveBayesAnalyzer())
                if (blob.sentiment.p_neg > blob.sentiment.p_pos):
                    print 'Negative comment : %s' % (comment_text)
                    delete_url = (BASE_URL + 'media/%s/comments/%s/?access_token=%s') % (media_id, comment_id, APP_ACCESS_TOKEN)
                    print 'DELETE request url : %s' % (delete_url)
                    delete_info = requests.delete(delete_url).json()

                    if delete_info['meta']['code'] == 200:
                        # *** this will show you that your comment is successfully deleted.***
                        print 'Comment successfully deleted!\n'
                    else:
                        # *** this this tell you that your comment was not deleted.***
                        print 'Unable to delete comment!'
                else:
                    # *** this will show you positive comments.***
                    print 'Positive comment : %s\n' % (comment_text)
        else:
            # *** otherwise this will show you that there is no existing comments on the post.***
            print 'There are no existing comments on the post!'
    else:
        # else it will run Status code other than 200 received.***
        print 'Status code other than 200 received!'
