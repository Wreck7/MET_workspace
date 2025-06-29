from fastapi import FastAPI
from supabase import create_client

db_url = 'https://bzdqxtoexbqfrjkbixkz.supabase.co'

db_api = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJ6ZHF4dG9leGJxZnJqa2JpeGt6Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0OTgyMTg0OCwiZXhwIjoyMDY1Mzk3ODQ4fQ.9-Myd9NglWhW37zNc2XZZI1OfnqTb2yKYRK5sSShJuM'

db = create_client(db_url, db_api)

app = FastAPI()


@app.post('/register')
def register(username, email, name, age, password, gender):
    # check = db.table('register').select('*').eq('username', username).eq('email', email).execute()
    check = db.table('register').select('*').or_(f"username.eq.{username},email.eq.{email}").execute()
    if check.data:
        return False
    else:
        data = {
            'name': name,
            'email': email,
            'username': username,
            'password': password,
            'age': age,
            'gender': gender
        }
        res = db.table('register').insert(data).execute()
        return True

@app.get('/users')
def get_users():
    res = db.table('users').select('*').execute()
    return res


@app.post('/users')
def post_users(name, age):
    data = {
        'name': name,
        'age': age
    }
    res = db.table('users').insert(data).execute()
    return res.data


@app.put('/users')
def update_users(user_id, course_id):
    data = {
        'course_id': course_id
    }
    res = db.table('users').update(data).eq('id', user_id).execute()
    return res.data


@app.delete('/users')
def delete_users(id):
    res = db.table('users').delete().eq('id', id).execute()
    return res.data


@app.get('/courses')
def get_courses():
    res = db.table('courses').select('*').execute()
    return res.data

@app.post('/courses')
def post_courses(name, description, duration):
    data = {
        'name': name, 
        'description': description, 
        'duration': duration
    }
    res = db.table('courses').insert(data).execute()
    return res


@app.put('/courses')
def update_courses(description, duration, id):
    data = {
        'description': description, 
        'duration': duration
    }
    res = db.table('courses').update(data).eq('id', id).execute()
    return res.data


@app.delete('/courses')
def delete_courses(id):
    res = db.table('courses').delete().eq('id', id).execute()
    return res.data

# comment! :)