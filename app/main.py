# app/main.py
import praw
import datetime
import os
import yaml

# Load Reddit config from YAML
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)["reddit"]

reddit = praw.Reddit(
    client_id=config["client_id"],
    client_secret=config["client_secret"],
    user_agent=config["user_agent"]
)


def get_account_creation_date(username):
    try:
        user = reddit.redditor(username)
        created_utc = user.created_utc
        return datetime.datetime.utcfromtimestamp(created_utc)
    except Exception as e:
        return f"Error: {e}"

def get_user_activity_in_subreddit(username, subreddit_name, limit=1000):
    try:
        user = reddit.redditor(username)
        activity = []

        for comment in user.comments.new(limit=limit):
            if comment.subreddit.display_name.lower() == subreddit_name.lower():
                activity.append({
                    "type": "comment",
                    "url": f"https://reddit.com{comment.permalink}",
                    "created": datetime.datetime.utcfromtimestamp(comment.created_utc)
                })

        for submission in user.submissions.new(limit=limit):
            if submission.subreddit.display_name.lower() == subreddit_name.lower():
                activity.append({
                    "type": "submission",
                    "url": f"https://reddit.com{submission.permalink}",
                    "created": datetime.datetime.utcfromtimestamp(submission.created_utc)
                })

        return sorted(activity, key=lambda x: x["created"])
    except Exception as e:
        return f"Error: {e}"
