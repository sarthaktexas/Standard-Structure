from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    hello_world = "Hello World"
    return render_template('index.html', text = hello_world)