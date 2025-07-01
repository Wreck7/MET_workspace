from fastapi import APIRouter
from backend.db import db


router = APIRouter()

@router.get("/transactions")
def get_transactions(token: int):
    user = db.table('users').select('id').eq('login_token', token).execute()
    if not user:
        return {"message": "Invalid token"}
    user_id = user.data[0]
    result = db.table("transactions").select("*").eq("id", user_id).execute()
    if result:
        return result.data[0]
    else:
        return 'user not found!'
 
 
@router.get("/transactions")
def get_transactions_by_coin(token: int, coin_id: str):
    user = db.table('users').select('id').eq('login_token', token).execute()
    if not user:
        return {"message": "Invalid token"}
    user_id = user.data[0]
    result = db.table("transactions").select("*").eq("id", user_id).eq("coin_id", coin_id).execute()
    if result:
        return result.data[0]
    else:
        return 'transactions not found!'