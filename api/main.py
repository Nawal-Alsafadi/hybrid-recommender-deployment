from routes.app_routes import app_routes
from flask import Flask
from flask_cors import CORS



app = Flask(__name__)
app.debug = True
CORS(app)
app_routes(app)


@app.route('/')
def index():
    return "Hola!"

@app.route('/second_page')
def index2():
    return "Hola from second page !!"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000)



