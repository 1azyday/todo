# ��� weibo all ·�ɡ�
# ��� webo add ·�ɡ�
from utils import log
from routes import json_response
from routes import current_user
from models.weibo import Weibo

def all(request):
    weibos = Weibo.all_json()
    return json_response(weibos)

def add(request):
    u = current_user(request)
    form = request.json()
    w = Weibo.new(form, u.id)
    return json_response(w.json())
	
	
# ʵ��delete ·��
def delete(request):
    form = request.json()
    weibo_id = int(form['id'])
    w = Weibo.delete(weibo_id)
    return json_response(w.json())
	
	
def update(request):
    form = request.json()
    w = Weibo.update(form)
    return json_response(w.json())

	
def route_dict():
    d = {
       '/api/weibo/all': all,
       '/api/weibo/add': add,
       '/api/weibo/delete': delete,
	'/api/weibo/update': update,
    }
    return d
