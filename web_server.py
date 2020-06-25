from flask import Flask

app = Flask(__name__)

def wrap_html(message):
    html = """
        <html>
        <body>
            <div style='font-size:120px;'>
            <center>
                {0}
            </center>
            </div>
        </body>
        </html>
    """.format(message)
    return html

@app.route("/")
def hello_world():
    message = "Hello Docker Peeps"
    html = wrap_html(message)
    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)