"""https://habr.com/ru/articles/346342/"""

from app import app, db
from app.models import User, Post


@app.shell_context_processors
def make_shell_context():
    return {"db": db, "User": User, "Post": Post}
