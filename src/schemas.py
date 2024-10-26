from pydantic import BaseModel
from enum import Enum
from typing import List, Optional


class PostSchema(BaseModel):
    site_type: str
    url: str
    content: str


    class Config:
        orm_mode = True



class SiteType(Enum):
    XCOM = "x.com"
    CHINA_NEWS = "10jqka.com.cn"


class ParseRequestSchema(BaseModel):
    site_type: SiteType
    accounts: Optional[List[str]] = []

    class Config:
        use_enum_values = True