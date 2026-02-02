from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello from Flask on Vercel!"

# required for local testing only
if __name__ == '__main__':
    app.run()
