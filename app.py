from flask import Flask, render_template
from controllers.bucket_list_controller import countries_blueprint
app = Flask(__name__)

app.register_blueprint(countries_blueprint)

@app.route('/')
def home():
    # return "Hello World!"
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)