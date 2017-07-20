#import urllib library to download the image
import urllib

#import user_id from the user_id file to get the recent the post of the user
from get_user_id import get_user_id
#Here we import the requests library
import requests
#Here we import the base_url and app_access_token
from constant import BASE_URL,APP_ACCESS_TOKEN

#create a function to get another user post
def get_user_post(insta_username):
       user_id = get_user_id(insta_username)
       if user_id == None:
        print ('User does not exist!')
       exit()
       request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
       print( 'GET request url : %s' % (request_url))
       user_media = requests.get(request_url).json()

       if user_media['meta']['code'] == 200:
           # extract post ID
           if len(user_media['data']):
               image_name = user_media['data'][0]['id'] + '.jpeg'
               image_url = user_media['data'][0]['images']['standard_resolution']['url']
               urllib.urlretrieve(image_url, image_name)
               print( 'Your image has been downloaded!')
           else:
               print ("There is no recent post!")
       else:
           print ('Status code other than 200 received!')