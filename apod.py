from flask import Flask, render_template, request


app=Flask("MyApp")

def get_resource_as_string(name, charset='utf-8'):
    with app.open_resource(name) as f:
        return f.read().decode(charset)

app.jinja_env.globals['get_resource_as_string'] = get_resource_as_string

@app.route("/")
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.form
    print(form_data["email"])
    return "We will let you know more about Anunnaki's secrets soon!"


app.run(debug=True)
