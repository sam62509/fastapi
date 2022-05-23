from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# made a small change, just for testing
# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres',
#                                 password='lewishamilton', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection established")
#         break
#     except Exception as e:
#         print(e)
#         print("database connection failed")
#         time.sleep(2)

# my_posts = [{"title": "post 1 about football", "content": "man city sucks", "id": 1}, {
#     "title": "post 2 about football", "content": "liverpool rocks", "id": 2}]


# def find_post(id):
#     for p in my_posts:
#         if p['id'] == id:
#             return p


# def find_by_id(id):
#     for i, p in enumerate(my_posts):
#         if p['id'] == id:
#             return i


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
async def root():
    return {"message": "Sup bitches!!!"}


# @app.get("/sqlalchemy")
# def test_sql(db: Session = Depends(get_db)):
    # posts = db.query(models.Post).all()
    # return {"data": posts}

# @app.post("/create_posts")
# def create_posts(payLoad: dict = Body(...)):
#     print(payLoad)
#     return {"message": f"Title:{payLoad['title']} Content:{payLoad['description']}"}
