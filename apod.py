from flask import Flask, render_template, request
import requests
import json


app=Flask("MyApp")

def get_resource_as_string(name, charset='utf-8'):
    with app.open_resource(name) as f:
        return f.read().decode(charset)

app.jinja_env.globals['get_resource_as_string'] = get_resource_as_string

@app.route("/")
def home():
    r = requests.get('https://api.nasa.gov/planetary/apod?api_key=clABaHP2DhsNUB8mZdjFdEAWT8Bcz1hAGzPMERIl')
    json_object = r.json()
    return render_template('home.html', apod=json.loads(r.text)['hdurl'])

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.form
    print(form_data["email"])
    return "We will let you know more about Anunnaki's secrets soon!"


app.run(debug=True)


#endpoint = "https://api.nasa.gov/planetary/apod"
#payload = {"date":"2019-03-28", "hd":"False", "api_key":"clABaHP2DhsNUB8mZdjFdEAWT8Bcz1hAGzPMERIl"}
#response = requests.get(endpoint, params=payload)
#data = response.json()
