from pydantic import BaseModel

class articles(BaseModel):

    title: str
    content: str
