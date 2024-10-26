# News parser

# How to run
```
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Create Database and src/.env file like this:
DB_NAME=posts_db
DB_HOST=127.0.0.1
DB_PORT=5432
DB_PASSWORD=my_password
DB_USER=my_user

# apply migrations
alembic upgrade head

# run app
uvicorn src.main:app --reload

```

# How to use 
```
Go to http://127.0.0.1:8000/docs


POST http://127.0.0.1:8000/parse_news/
{
    "site_type": "10jqka.com.cn"
}


GET http://127.0.0.1:8000/news/

Response
[
    {
        "site_type": "news.10jqka.com.cn",
        "url": "https://news.10jqka.com.cn/20241026/c662836814.shtml",
        "content": "伊朗政府：伊朗目前处于正常状态 民众对防御能力充满信心 伊朗政府发言人莫哈杰拉尼表示，伊朗民众对国家的防御能力感到自豪，并充满信心。针对部分媒体发布的虚假图片，政府发言人强调，正如伊朗防空部门的官方声明所示，本次袭击造成的损失有限，伊朗人民需要保持冷静，远离谣言，并及时关注官方媒体和国防部门发布的声明。莫哈杰拉尼表示，伊朗现在处于正常状态，航班也已经在26日9时恢复正常。（新浪财经）"
    },
    {
        "site_type": "news.10jqka.com.cn",
        "url": "https://news.10jqka.com.cn/20241026/c662836782.shtml",
        "content": "美以防长就以色列打击伊朗通话 美国国防部26日发表声明说，美国国防部长奥斯汀与以色列国防部长加兰特就以色列打击伊朗通电话。声明说，以色列防长向美方通报了以色列国防军打击伊朗军事目标的最新情况。奥斯汀重申美国对以色列安全和自卫权的坚定承诺，强调美国已加强军力部署，以“保护美国人员、以色列以及地区伙伴”。（新华社）"
    }
]
```