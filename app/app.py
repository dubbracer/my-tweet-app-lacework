from flask import Flask, render_template, url_for
import urllib.parse
import random
import platform

app = Flask(__name__)

event_text = "Welcome to our new DevSecOps automation Demo Site Feb 8th 2022"
tweet_text = "I just just enjoyed a fantastic demonstration about shifting left Security with #laceworks"


@app.route('/')
def index():
    images = [
        url_for('static', filename='beachops-1.png'),
        url_for('static', filename='beachops-2.png'),
        url_for('static', filename='norules-1.png'),
        url_for('static', filename='norules-2.png'),
    ]
    url = random.choice(images)
    hostname = platform.node()
    return render_template('index.html', url=url, hostname=hostname, event_text=event_text, tweet_text=tweet_text, tweet_text_url=urllib.parse.quote(tweet_text))

@app.route('/lacework')
def lacework():
    return render_template('lacework.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0")
