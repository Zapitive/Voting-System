import mysql.connector

def con():
    con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="voting_sys"
    )
    return con

