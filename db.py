import pymysql
from config import *

def connect():
    con = pymysql.connect(HOST,USER,PASS, DB)
    return con

def add_user(c,id_user,nickname,):
    cur = c.cursor()
    sql = "Insert into users (id_user,nickname,balance,date_reg) values (%s,%s,0,curdate())"
    cur.execute(sql,(id_user,nickname))
    c.commit()

def select_users(c):
    cur = c.cursor(pymysql.cursors.DictCursor)
    sql = 'select * from users'
    cur.execute(sql)
    return cur.fetchall()