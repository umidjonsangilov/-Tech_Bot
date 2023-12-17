import mysql.connector
from datetime import date
from data.config import *

class DataBase():
    def update_connection(self):
        self.cursor.close()
        self.con.close()
        self.__init__()

    def __init__(self) -> None:
        self.con = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            database=DB_NAME,
            password=DB_PASS,
            charset="utf8mb4",
            autocommit=True)
        self.cursor = self.con.cursor(buffered=True)

    def add_user(self, tg_id, tel, name):
        self.update_connection()
        cursor=self.cursor
        cursor.execute("INSERT INTO users (tg_id,tel, name) VALUES(%s,%s,%s)",(tg_id,tel,name))

    def users(self):
        self.update_connection()
        cursor=self.cursor
        cursor.execute("SELECT tg_id FROM users")
        users=[i[0] for i in cursor.fetchall()]
        return users

    def order_data(self,category):
        self.update_connection()
        cursor=self.cursor
        cursor.execute("SELECT name, id FROM products WHERE category=%s",(category,))
        return cursor.fetchall()

    def product(self, id):
        self.update_connection()
        cursor=self.cursor
        cursor.execute("SELECT * FROM products WHERE id=%s",(id,))
        return cursor.fetchone()

    def add_order(self,pr_id, user_id, amount):
        self.update_connection()
        cursor=self.cursor
        cursor.execute("INSERT INTO orders (product_id, user_id, amount, status) VALUES(%s,%s,%s,'New')",(pr_id,user_id,amount))
