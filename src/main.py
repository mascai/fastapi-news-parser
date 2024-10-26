from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from . import models
from .database import SessionLocal, engine, get_db
from .schemas import PostSchema, ParseRequestSchema, SiteType
from src.parsers.china_news import ChinaNewsParser
from src.parsers.xcom import XcomParser


app = FastAPI()


models.Base.metadata.create_all(bind=engine)


@app.get('/news')
def read_items(db: Session = Depends(get_db)) -> list[PostSchema]:
    """
    List all items
    """
    posts = db.query(models.Post).all()
    return posts


@app.post("/parse_news")
def parse_news(body: ParseRequestSchema, db: Session = Depends(get_db)):
    if body.site_type == SiteType.CHINA_NEWS.value:
        parser = ChinaNewsParser(db=db)
        posts_count = parser.parse()
    elif body.site_type == SiteType.XCOM.value:
        parser = XcomParser(db=db)
        posts_count = parser.parse(account_names=body.accounts)
    return {"message:": f"Created {posts_count} posts"}

