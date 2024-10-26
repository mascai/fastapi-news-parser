import requests
import logging

from typing import Dict
from fastapi import Depends

from src.models import Post
from src.database import get_db
from sqlalchemy.orm import Session


logger = logging.getLogger("uvicorn")
logger.setLevel(logging.INFO)


class ChinaNewsParser():
    def __init__(self, db: Session = Depends(get_db)) -> None:
        self.base_url = "news.10jqka.com.cn"
        self.api_url = "https://news.10jqka.com.cn/tapp/news/push/stock"
        self.db = db

        self.headers: Dict[str, str] = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "zh-CN",
            "Connection": "keep-alive",
            "Cookie": "",
            "Host": "news.10jqka.com.cn",
            "Referer": "https://news.10jqka.com.cn/realtimenews.html",
            "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"macOS"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 "
            "(Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/126.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
        }       

        
    def parse(self, page: int = 1, limit: int = 10, tag: str = ""):
        posts = []
        try:
            for page_id in range(1, page+1):
                url = self.api_url + f"/?page={page_id}&tag={tag}&track=website&pagesize={limit}"
                response = requests.get(url, headers=self.headers)
                
                if response.status_code == 200:
                    response = response.json()
                    for curr_post in response["data"]["list"]:
                        if not self.db.query(Post).filter(Post.url==curr_post.get("url")).count():
                            posts.append(Post(
                                site_type=self.base_url,
                                url=curr_post.get("url"),
                                content=curr_post.get("title", "") + ' ' + curr_post.get("digest", "")
                            ))
                    
            logger.info(f"Created {len(posts)} posts")
            if posts:
                self.db.add_all(posts) # bulk creation
                self.db.commit()
        except Exception as e:
            logger.error("ChinaNewsParser::parse error: {e}")
        return len(posts)
