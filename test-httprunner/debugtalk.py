import hashlib
import time
import random
from httprunner import __version__
from httprunner.response import ResponseObject

def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)

def get_documents_num(response:ResponseObject):
    resp_json = response.resp_obj.json()
    document_num = len(resp_json['data'].get("documents"))
    print("document_num===",document_num)
    return document_num

def gen_token(phone,password,timestamp):
    s = "".join([phone,password,str(timestamp)])
    token = hashlib.md5(s.encode("utf-8")).hexdigest()
    print("签名是~~~~~",token)
    return token

def gen_random_title():
    return f"喵喵喵→{random.randint(1,7777777)}"

def gen_doc_titles(num):
    return [gen_random_title() for _ in range(num)]