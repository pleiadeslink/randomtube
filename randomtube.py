import requests, json, os, random
from mastodon import Mastodon
from googleapiclient.discovery import build

DEVELOPER_KEY = 'asdf'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
prefix = ['IMG ', 'IMG_', 'IMG-', 'DSC ']
postfix = [' MOV', '.MOV', ' .MOV']

mastodon = Mastodon(
    access_token = 'asdf',
    api_base_url = 'https://botsin.space/'
)

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

search_response = youtube.search().list(
    q=random.choice(prefix) + str(random.randint(999, 9999)) + random.choice(postfix),
    part='snippet',
    maxResults=5
).execute()

videos = []

for search_result in search_response.get('items', []):
    if search_result['id']['kind'] == 'youtube#video':
        videos.append('%s' % (search_result['id']['videoId']))

mastodon.status_post("https://www.youtube.com/watch?v=" + videos[random.randint(0, 2)])
