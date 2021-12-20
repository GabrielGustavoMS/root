# Hello Mundo - Flask API

---

**This is my first Flask API.**

It simulate the user create function

---

## Parameters:

Basically, it wait for 3 parameter:

1. name
2. email
3. password

## Routes:

This flask api has two routes:

1. `/helloworld` - It's a route about GET method and it returns a JSON with `{"Hello":"World"}`
2. `/new/user` - It's a route about POST method and it returns a JSON with user information

### Error prevention:

To avoid errors, it checks whether the required parameters, "to create" a new user, are present in request body
