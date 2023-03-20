from fastapi import FastAPI,Form,status,Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import Field,BaseModel
from fastapi.responses import RedirectResponse
import models

app = FastAPI()

articles = []

templates = Jinja2Templates(directory="templates")

app.mount("/static",StaticFiles(directory="static"),name="static")

@app.get('/')

def home(request:Request):
    return templates.TemplateResponse("home.html",{"request":request})

@app.get('/')
def home_page(request:Request):
    return templates.TemplateResponse("home_page.html",{"request":request,"articles":articles})

@app.get('/create')
def create_page(request:Request):
    return templates.TemplateResponse("create.html",{"request":request})


class articles(BaseModel):
    title: str = Field(min_length=1)
    content: str = Field(min_length=1)

@app.post('/save_article_form_data')
async def save_data_response(title:str=Form(...),content:str=Form(...)):
    # data=ArticleData(title=title,content=content)
    # articles.append(data)
    # print(articles.data.title)
    article_model = models.articles()
    article_model.title = title
    article_model.content = content
    print(article_model.data.title)
    print(article_model.title)
    # print(articles[-1].title)
    """
    When I replace print(articles.data.title) with print(articles[-1].title)
    the title which we have entered in the webpage is printed in the terminal of VScode
    """
    return RedirectResponse(url=app.url_path_for("home_page"),status_code=status.HTTP_303_SEE_OTHER)

