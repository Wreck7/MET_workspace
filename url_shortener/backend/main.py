from fastapi import FastAPI
from supabase import create_client

url = 'https://trhagyasyglhhsmmngjx.supabase.co'
api_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRyaGFneWFzeWdsaGhzbW1uZ2p4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTAzNTQ3MzUsImV4cCI6MjA2NTkzMDczNX0.fgD8-UuOCV5hkCU5OdHMD2ROOvlsJqTIOzy1U6oLg2Q'

db = create_client(url, api_key)

app = FastAPI()

@app.get('/')
def url_getter(long_url):
    




