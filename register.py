from condb import *
from passlib.hash import sha256_crypt

def secure(psw):
    return sha256_crypt.encrypt(psw)

def register(name,email,password):
    mydb = con()
    mycursor = mydb.cursor()
    password = secure(password)
    sql = "INSERT INTO user_info (username,email,password) VALUES (%s, %s, %s)"
    val = (name,email,password)
    mycursor.execute(sql, val)
    mydb.commit()
    mydb.close()