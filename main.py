from fastapi import FastAPI

app=FastAPI()


@app.get('/') # / indicates   the root route of our API, which is accessed by default when we hit the base URL@app.get("/")
def index():
    return {'data':{'name':'Siva'}}


@app.get('/about')
def about():
    return {'about':'page'}