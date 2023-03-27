from fastapi import FastAPI, Request, Form, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from pydantic import Field, BaseModel

app = FastAPI()

templates = Jinja2Templates(directory = "templates")

app.mount("/static", StaticFiles(directory = "static"), name = "static")

@app.get('/')
def home(request:Request):
    return templates.TemplateResponse("home.html",{"request":request})

@app.get('/home')
def home_page(request:Request):
    return templates.TemplateResponse("home_page.html",{"request":request, "articlesList": articlesList})

@app.get('/create')
def create_page(request:Request):
    return templates.TemplateResponse("create.html",{"request":request})

