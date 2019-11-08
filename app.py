import json
from flask import Flask, send_from_directory, send_file


app = Flask(__name__, static_url_path='')
app.config['DEBUG'] = True


@app.route("/")
def hello():
    return "Hello World!"


@app.route('/.well-known/acme-challenge/<challenge>')
def letsencrypt(challenge):
    # return Response(credentials[challenge], mimetype='text/plain')
    # return send_from_directory('.well-known/acme-challenge', challenge, as_attachment=False)
    return send_file(f'.well-known/acme-challenge/{challenge}', mimetype='text/plain')


if __name__ == "__main__":
    app.run()
