from supabase import create_client
from fastapi import APIRouter
from fastapi.responses import RedirectResponse

import random
import string

router = APIRouter()

url = 'https://trhagyasyglhhsmmngjx.supabase.co'
api_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRyaGFneWFzeWdsaGhzbW1uZ2p4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTAzNTQ3MzUsImV4cCI6MjA2NTkzMDczNX0.fgD8-UuOCV5hkCU5OdHMD2ROOvlsJqTIOzy1U6oLg2Q'

db = create_client(url, api_key)

def rand_str(length):
    length = 8
    phrase = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return phrase



@router.post('/')
def url_getter(long_url):
    res = db.table('urls').insert({"long_url": long_url, "phrase": rand_str(7)}).execute()
    return "http://127.0.0.1:8000/" + res.data[0]['phrase']

@router.get('/{phrase}')
def redirect_main(phrase):
    res = db.table('urls').select('long_url').eq('phrase', phrase).execute()
    return RedirectResponse(res.data[0]["long_url"])

