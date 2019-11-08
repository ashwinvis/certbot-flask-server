from distutils import sys
from invoke import task


EMAIL = "me@example.com"
DOMAIN = "example.com"
VAR_DIR = "var"
BIN_DIR = f"{sys.exec_prefix}/bin"


def run_vars(c, sudo):
    if sudo:
        return c.sudo, "0.0.0.0", 80
    else:
        return c.run, "localhost", 8080

@task
def flask(c, sudo=False):
    run, HOST, PORT = run_vars(c, sudo)
    run(f"{BIN_DIR}/flask run -h {HOST} -p {PORT}")


@task
def gunicorn(c, sudo=False):
    run, HOST, PORT = run_vars(c, sudo)
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
