from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    html = f"<p><h1>Hello World, my name is Thiruvarasamoorthy Viswanathan</h1></p><p>This is the revised application with Rolling deployment</p>"
    return html.format(format)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)  # specify port=80