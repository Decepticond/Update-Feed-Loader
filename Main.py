import json
import feedparser

url = "https://stackoverflow.com/feeds/tag?tagnames=python&sort=newest"
dir(feedparser)
f = feedparser.parse(url)


"""
print("hi")
def hello(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}
"""
