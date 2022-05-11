from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def Home():
    return "Welcome Home"

@app.post('/login')
async def login_user():
    pass

