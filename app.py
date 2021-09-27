from flask import Flask
from flask.helpers import send_from_directory
from flask_cors import CORS, cross_origin

# front-end folder name
# connect flask to front end
# do not need static_url_path
app = Flask(__name__, static_folder='my-app/build', static_url_path='')
CORS(app)
# on the front end api is not there for dev
# on heroku this is there
@app.route('/api', methods=['GET'])
@cross_origin()
def index():
  return {
    "tutorial": "Flask React Heroku"
  }

# generate html file on / route
@app.route('/')
@cross_origin()
def serve():
  return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
  app.run()