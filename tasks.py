from distutils import sys
from invoke import task


EMAIL = "me@example.com"
DOMAIN = "example.com"
VAR_DIR = "var"
HOST = "localhost"
BIN_DIR = f"{sys.exec_prefix}/bin"


@task
def flask(c, sudo=False):
    if sudo:
        PORT = 80
        run = c.sudo
    else:
        PORT = 8080
        run = c.run
    run(f"{BIN_DIR}/flask run -h {HOST} -p {PORT}")


@task
def gunicorn(c):
    if sudo:
        PORT = 80
        run = c.sudo
    else:
        PORT = 8080
        run = c.run
    # run("gunicorn --certfile cert.pem --keyfile key.pem -b 0.0.0.0:80 app:app")
    run(f"{BIN_DIR}/gunicorn -b {HOST}:{PORT} app:app")


@task
def certbot(c):
    mode = "--webroot"
    c.run(
        f"{BIN_DIR}/certbot certonly {mode} -w . -d {DOMAIN} "
        f" --config-dir {VAR_DIR}/config --work-dir {VAR_DIR}/work "
        f"--logs-dir {VAR_DIR}/logs -m {EMAIL} --agree-tos "
    )
