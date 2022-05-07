from flask import Flask, render_template

server = Flask(__name__)


@server.route("/")
def main_page():
    return render_template("index.html")


if __name__ == "__main__":
    server.run(debug=True, port=1623)
