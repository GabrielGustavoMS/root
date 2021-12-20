from flask import Flask, request

app = Flask(__name__)
# app = Flask("APP")
@app.route('/',methods=["GET"])
def index():
  return {"Hello":"Mundo"}


@app.route('/', methods=["POST"])
@app.route('/index/', methods=["POST"])
def index_post():
  body = request.get_json()
  return body

if __name__ == '__main__':
  app.run(debug=True)

# app.run()
