from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    html = f"<h1><p>Hello World, my name is Thiruvarasamoorthy Viswanathan. This is a revised application with rolling deployment</h1></p>"
    return html.format(format)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)  # specify port=80