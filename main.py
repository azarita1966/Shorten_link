import os
import requests
import urllib
import argparse

from dotenv import load_dotenv
from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

def shorten_link(token, user_url):
    payload = {'long_url': user_url}
    api_endpoint_url = "https://api-ssl.bitly.com/v4/shorten"
    headers = {
        "Authorization": f"Bearer {token}"}
    response = requests.post(api_endpoint_url, json=payload, headers=headers)
    response.raise_for_status()
    bitlink = response.json()["link"]
    return bitlink


def count_clicks(token, link):
    parsed_link = urllib.parse.urlparse(link)
    short_link = f"{parsed_link.netloc}{parsed_link.path}"
    api_endpoint_url = f"https://api-ssl.bitly.com/v4/bitlinks/{short_link}/clicks/summary"
    headers = {
        "Authorization": f"Bearer {token}"}
    response = requests.get(api_endpoint_url, headers=headers)
    response.raise_for_status()
    click_count = response.json()['total_clicks']
    return click_count


def is_bitlink(token, user_url):
    parsed_link = urllib.parse.urlparse(user_url)
    short_link = f"{parsed_link.netloc}{parsed_link.path}"
    api_endpoint_url = f"https://api-ssl.bitly.com/v4/bitlinks/{short_link}/clicks/summary"
    headers = {
        "Authorization": f"Bearer {token}"}
    response = requests.get(api_endpoint_url, headers=headers)
    return response.ok

parser = argparse.ArgumentParser()
parser.add_argument('--user_url',
                    default=['aa'],
                    dest='user_url',
                    help='Define url',
                    type=str,
                    nargs=1
                    )
args = parser.parse_args()


def main():
    #bitly_token = os.getenv('TOKEN')
    bitly_token = os.environ['TOKEN']
    user_url = args.user_url[0]
    user_url = 'https://www.massimodutti.com/'
    if is_bitlink(bitly_token, user_url):
      print ('Link is bitlink')
      print(f'Number of clicks: {count_clicks(bitly_token, user_url)}')
    else:
      print("Link is not bitlink")
      print(f'Its bitlink is: {shorten_link(bitly_token, user_url)}')

print(f'The defined url is {args.user_url[0]}')
import pprint
if __name__ == '__main__':
    #env_var =os.environ
    #pprint.pprint(dict(env_var), width = 1)
    main()
