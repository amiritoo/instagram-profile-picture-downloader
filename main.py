
import requests
from bs4 import BeautifulSoup
import re
import json

def exctract_url(username):

    insta_url= f'https://www.instagram.com/{usrname}'
    instagram_response = requests.get(insta_url)
    if instagram_response.status_code == 200:
        regexp = r'window._sharedData = {.*<\/script>'
        regex = re.compile(regexp)
        soup = BeautifulSoup(instagram_response.text , 'html.parser')
        result = regex.findall(str(soup))[0]
        result = json.loads(result[21:-10])
        result = result['entry_data']['ProfilePage'][0]['graphql']['user']['profile_pic_url_hd']
        get_image(result)
    else:
        print('this user does not exist!')
        



def get_image(result):
    response= requests.get(result)
    file_name = f'{usrname}.jpg'
    with open(file_name,'wb') as f: 
        f.write(response.content) 


if __name__ == "__main__":
    while True:
        usrname= input("enter ur username: ")
        exctract_url(usrname)
