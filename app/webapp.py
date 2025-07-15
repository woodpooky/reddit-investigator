# app/webapp.py
from flask import Flask, render_template, request
from main import get_account_creation_date, get_user_activity_in_subreddit

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        username = request.form.get("username")
        subreddit = request.form.get("subreddit")
        if username and subreddit:
            created_date = get_account_creation_date(username)
            if isinstance(created_date, str):
                result = {"error": created_date}
            else:
                activity = get_user_activity_in_subreddit(username, subreddit)
                if isinstance(activity, str):
                    result = {"error": activity}
                else:
                    result = {
                        "username": username,
                        "subreddit": subreddit,
                        "created_date": created_date.strftime("%Y-%m-%d %H:%M:%S UTC"),
                        "activity": activity
                    }
    return render_template("index.html", result=result)
