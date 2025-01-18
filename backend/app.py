from flask import Flask, send_from_directory
import os

app = Flask(__name__)

def serve_html():
    return send_from_directory(os.getcwd() + "/build", "index.html")

def serve_js(name):
    return send_from_directory(os.getcwd() + "/build/static/js", name)

def serve_css(name):
    return send_from_directory(os.getcwd() + "/build/static/css", name)

def serve_media(name):
    return send_from_directory(os.getcwd() + "/build/static/media", name)

if __name__ == '__main__':
    app.add_url_rule("/", "index", serve_html)
    app.add_url_rule("/static/js/<name>", "js", serve_js)
    app.add_url_rule("/static/css/<name>", "css", serve_css)
    app.add_url_rule("/static/media/<name>", "asset", serve_media)
    app.run(debug=True, port=7070)

