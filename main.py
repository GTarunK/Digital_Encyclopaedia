from fastapi import FastAPI, Request, Form, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from pydantic import Field, BaseModel

app = FastAPI()

articlesList = []

class article(BaseModel):
    title: str = Field(min_length = 1)
    content: str = Field(min_length = 1)


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

@app.post('/save_article_form_data/')
async def save_data_response(title:str=Form(...),content:str=Form(...)):
    data=article(title=title,content=content)
    articlesList.append(data)
    print(articlesList)
    return RedirectResponse(url=app.url_path_for("home_page"),status_code=status.HTTP_303_SEE_OTHER)