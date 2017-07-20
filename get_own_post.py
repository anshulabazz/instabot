#import urllib library to download the image
import urllib
#import the requests library
import requests
#import the base url and app access toeken form constant.py

from constant import APP_ACCESS_TOKEN,BASE_URL


#getting own post of user

def get_own_post():
    #function logic
    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)
    print ('GET request url : %s' % (request_url))
    own_media = requests.get(request_url).json()
    if own_media['meta']['code'] == 200:
        # extract post ID
        if len(own_media['data']):
            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print ('Your image has been downloaded!')
        else:
            print ('Post does not exist!')
    else:
        print ('Status code other than 200 received!')
