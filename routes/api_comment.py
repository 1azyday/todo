from utils import log
from routes import json_response
from routes import current_user
from models.comment import Comment



def all(request):
    comments = Comment.all_json()
    return json_response(comments)

def add(request):
    u = current_user(request)
    form = request.json()
    c = Comment.new(form, u.id)
    return json_response(c.json())

def delete(request):
    form = request.json()
    comment_id = int(form['id'])
    c = Comment.delete(comment_id)
    return json_response(c.json())

def update(request):
    form = request.json()
    w = Comment.update(form)
    return json_response(w.json())

def route_dict():
    d = {
        '/api/comment/all': all,
        '/api/comment/add': add,
        '/api/comment/delete': delete,
        '/api/comment/update': update,
    }
    return d