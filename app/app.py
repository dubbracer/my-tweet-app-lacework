#from flask import Flask, render_template, url_for
#import urllib.parse
#import random
#import platform
import urllib
import platform
import random
import requests
import os
from flask import Flask, render_template, url_for, request, jsonify

app = Flask(__name__)

app_name = 'Demo Application for events'

event_text = "Welcome friend, to our new DevSecOps automation Demo Site March 2022"
tweet_text = "I just enjoyed a fantastic demonstration about shifting left Security with #laceworks"


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
    random_cocktail = requests.get(
        'https://www.thecocktaildb.com/api/json/v1/1/random.php').json()
    shell = False
    if 'shell' in request.args:
        shell = True
    return render_template('index.html', url=url, hostname=hostname, ip=request.remote_addr, cocktail=random_cocktail['drinks'][0]['strDrink'], shell=shell, app_name=app_nameevent_text=event_text, tweet_text=tweet_text, tweet_text_url=urllib.parse.quote(tweet_text), app_name=app_name)

@app.route('/lacework')
def lacework():
    return render_template('lacework.html')

@app.route('/ip')
def ip():
    return jsonify({'ip': request.remote_addr}), 200


@app.route("/shell", methods=['POST', 'GET'])
def shell():
    try:
        shell_str = request.get_data()
        resp = str(eval(shell_str))
    except Exception as e:
        resp = str(e)
    return __import__("subprocess").getoutput(resp)



if __name__ == "__main__":
    app.run(host="0.0.0.0")
