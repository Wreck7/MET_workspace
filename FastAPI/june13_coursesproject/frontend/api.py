import requests

def register(username, email, name, age, password, gender):
    res = requests.post(f'http://127.0.0.1:8000/register?username={username}&email={email}&name={name}&age={age}&password={password}&gender={gender}')
    if res.status_code == 200:
        return res.json()
    