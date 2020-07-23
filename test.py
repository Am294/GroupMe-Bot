import json
import requests
from pprint import pprint

data = {
    "bot_id": "eb51bc7141c6e7ba5133e0deef",
    "text": "Text from command line"
}
out = requests.post("https://api.groupme.com/v3/bots/post?token=c8c7f1b0ad350138f2846a76bf88d819", data={"bot_id": "eb51bc7141c6e7ba5133e0deef","text": "Text from command line"})
pprint(out.content)
pprint(out.text)