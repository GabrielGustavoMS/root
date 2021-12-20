from flask import Flask, request
from main import insertUser as createNewUser

app = Flask("Hello Mundo")

@app.route("/helloworld", methods=["GET"])
def helloworld():
  return {"Hello":"World"}

@app.route("/new/user",methods=["POST"])
def insertUser():
  body = request.get_json()

  if("name" not in body):
    return getResponse(400,'name is required !')

  if("email" not in body):
    return getResponse(400,'email is required !')
    
  if("password" not in body):
    return getResponse(400,'password is required !')
  
  user = createNewUser(body['name'],body['email'],body['password'])

  return getResponse(200,'Usurário criado',"user",user)

def getResponse(status, msg, content_name = False,content = False):
  resp = {}
  resp['status'] = status
  resp['msg'] = msg

  if(content_name and content):
    resp[content_name] = content  
  return resp

app.run()
