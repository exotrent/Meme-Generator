from flask import Flask, render_template
import requests

# Meme_api at work
def get_meme():
    """This is the meme api that adds 'fun' into my programming"""
    api_url = "https://meme-api.com/gimme"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        return f"{data['preview'] [2]}"
    else:
        return "Failed to get a reddit request, code no worky LOL"
    
app = Flask(__name__)
web_var = get_meme()

@app.route("/")
def meme_generator():
    return render_template('index.html', web_var=web_var)


if __name__ == '__main__':
    app.run(debug=True)
