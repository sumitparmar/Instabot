APP_ACCESS_TOKEN = ' 2121110795.f566e63.45b3d45844144983bd2217db985ca244'
BASE_URL = 'https://api.instagram.com/v1/'
import  requests
import urllib


def get_own_post():
    # Function Logic to Download Own Most Recent Post..

    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' %(request_url)
    own_media = requests.get(request_url).json()

    if own_media['meta']['code'] == 200:        #Download the post
        if len(own_media['data']):
            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print "\n\t\t*****Your Recent image has been downloaded to C:\Users\yooooooooo\PycharmProjects\InstaBot*****"
        else:
            print '\n\t\t*****There Are No Post!*****'
    else:
        print '\n\t\t*****Status code other than 200 received!*****'