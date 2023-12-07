from flask import Flask
import requests

# Meme_api at work
def get_meme():
    """This is the meme api that adds 'fun' into my programming"""
    api_url = "https://meme-api.com/gimme"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        return f"{data['postLink']}"
    else:
        return "Failed to get a reddit request, code no worky LOL"

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    print(get_meme())
