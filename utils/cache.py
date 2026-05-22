import os
import json
import hashlib
from os import path

CACHE_DIR = "cache"

os.makedirs(CACHE_DIR,exist_ok=True)

def get_key(text):
    return hashlib.md5(text.encode()).hexdigest()

def load_cache(text):
    key = get_key(text)
    path = (f"{CACHE_DIR}/{key}.json")
    if os.path.exists(path):
        with open(path,"r") as f:
            return json.load(f)
    return None

def save_cache(text,data):
    key = get_key(text)
    path = (f"{CACHE_DIR}/{key}.json")
    with open(path,"w") as f:
        json.dump(data,f,indent=2)