from fastapi import FastAPI
from supabase import create_client
import random
import string

url = 'https://trhagyasyglhhsmmngjx.supabase.co'
api_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRyaGFneWFzeWdsaGhzbW1uZ2p4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTAzNTQ3MzUsImV4cCI6MjA2NTkzMDczNX0.fgD8-UuOCV5hkCU5OdHMD2ROOvlsJqTIOzy1U6oLg2Q'

db = create_client(url, api_key)

app = FastAPI()

def rand_str(length):
    length = 8
    phrase = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return phrase



@app.post('/')
def url_getter(long_url):
    res = db.table('urls').insert({"long_url": long_url, "phrase": rand_str(7)}).execute()
    return res.data[0]['phrase']

@app.get()




