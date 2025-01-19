from flask import Flask, send_from_directory, jsonify
from werkzeug.exceptions import NotFound, InternalServerError
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.errorhandler(NotFound)
def handle_not_found(error):
    logger.error(f'Resource not found: {error}')
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(InternalServerError)
def handle_internal_server_error(error):
    logger.error(f'Internal server error: {error}')
    return jsonify({'error': 'Internal server error'}), 500

@app.route('/')
def serve_html():
    try:
        if not os.path.exists(os.path.join(os.getcwd(), 'build', 'index.html')):
            raise NotFound()
        logger.info('Serving HTML file')
        return send_from_directory(os.getcwd() + '/build', 'index.html')
    except Exception as e:
        logger.error(f'Error serving HTML file: {e}')
        raise InternalServerError()

@app.route('/static/js/<name>')
def serve_js(name):
    try:
        logger.info(f'Serving JS file: {name}')
        return send_from_directory(os.getcwd() + '/build/static/js', name)
    except Exception as e:
        logger.error(f'Error serving JS file: {e}')
        raise InternalServerError()

@app.route('/static/css/<name>')
def serve_css(name):
    try:
        logger.info(f'Serving CSS file: {name}')
        return send_from_directory(os.getcwd() + '/build/static/css', name)
    except Exception as e:
        logger.error(f'Error serving CSS file: {e}')
        raise InternalServerError()

@app.route('/static/media/<name>')
def serve_media(name):
    try:
        logger.info(f'Serving media file: {name}')
        return send_from_directory(os.getcwd() + '/build/static/media', name)
    except Exception as e:
        logger.error(f'Error serving media file: {e}')
        raise InternalServerError()

@app.route('/favicon.ico')
def serve_favicon():
    return send_from_directory(os.path.join(os.getcwd(), 'build'), 'favicon.ico')

@app.route("/robots.txt")
def serve_robots():
    return "gtfo BANNED!", 403

@app.route("/manifest.json")
def serve_manifest():
    return send_from_directory(os.path.join(os.getcwd(), "build"), "manifest.json")

@app.route("/<filename>")
def serve_static(filename):
    try:
        logger.info(f'Serving static file: {filename}')
        return send_from_directory(os.getcwd() + '/build', filename)
    except Exception as e:
        logger.error(f'Error serving static file: {e}')
        raise InternalServerError()

if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
    port = int(os.getenv('FLASK_PORT', 7070))
    app.run(debug=debug_mode, port=port)
