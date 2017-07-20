import json
import requests
from constant import APP_ACCESS_TOKEN ,BASE_URL
from get_user_post import get_user_post

import matplotlib.pyplot as plt


def get_trending_tag_counts(tag):
    #print(media_id)
    #  message = raw_input("Enter ur comment....\n")
    # payload = {"access_token" : APP_ACCESS_TOKEN, "message":message}
    request_url = (BASE_URL + "tags/" + tag + "?access_token=" + APP_ACCESS_TOKEN)
    get_a_trend = requests.get(request_url).json()
    (trends) = get_a_trend['data']['media_count']
    if get_a_trend['meta']['code'] == 200:
        print("Here is your tag...Popularity\n")
        print(">>> "+str(get_a_trend['data']['media_count'])+" <<<")
        plt.plot(get_a_trend['data']['media_count'], 'ro')
        plt.axis()
        plt.ylabel('Trending----->')
        plt.xlabel("Insta-Bot")
        plt.title("TRENDING GRAPH")
        #plt._auto_draw_if_interactive()
        plt.show()
        print ("Style.RESET_ALL")
        return (get_a_trend['data']['media_count'])
    else:
        print('not successful')

#get_trending_tag_counts(tag="love")git