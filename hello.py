from flask import Flask
from urllib3.util.ssl_ import SSLContext  # TODO: <<< look into urllib3 1.x vs 2.x >>>
from urllib3.util.ssl_ import OP_NO_SSLv2
app = Flask(__name__)

def create_urllib3_context():
    context = SSLContext()

    options = 0
    # SSLv2 is easily broken and is considered harmful and dangerous
    options |= OP_NO_SSLv2
    context.options |= options

context = create_urllib3_context()

@app.route("/")
def hello():
    return "hello, world!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
