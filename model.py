#Developer Diary
#Sample Web App by RunnerMom

import sqlite3
import traceback

DB = None
CONN = None

class User(object):
    def __init__(self, name, fb_uid, photo):
        self.name = name
        self.fb_uid = fb_uid
        self.photo = photo

    def add_user_to_db(self):
        sql = """INSERT into Users VALUES (?, ?, ?)"""   #expects 3 args
        DB.execute(sql, (self.username, self.fb_uid, self.photo))
        CONN.commit()

    # def get_student_by_github(github):
    #     sql = """SELECT first_name, last_name, github 
    #     FROM Students
    #     WHERE github = ?"""
    #     DB.execute(sql, (github,))
    #     record = DB.fetchone()

    #     return record


# get post by title
class Post(object):
    def __init__(self, title, body, author, timestamp):
        self.title = title
        self.body= body
        self.author = author
        self.timestamp = timestamp

    def add_post_to_db(self):
        sql = """INSERT into Posts (title, body, author, created_at) VALUES (?, ?, ?, ?)"""
        DB.execute(sql, (self.title, self.body, self.author, self.timestamp))
        CONN.commit()

    # def get_post_id_by_title(self):
    #     sql = """SELECT id FROM Posts WHERE title = ?"""
    #     DB.execute(sql, (self.title,))
    #     record = DB.fetchone()

    #     return record        

    # def get_post_by_title(self):
    #     sql = """SELECT * FROM Posts WHERE title = ?"""
    #     DB.execute(sql, (self.title,))
    #     record = DB.fetchone()

    #     return record

    # def get_posts_by_author(self):
    #     sql = """SELECT * FROM Posts WHERE author = ?"""
    #     DB.execute(sql, (self.author,))
    #     records = DB.fetchall()

    #     return records


class Vote(object):
    def __init__(self, voter_id, post_id):
        self.voter_id=voter_id
        self.post_id=post_id

    def add_vote_to_db(self):
        sql = """INSERT into Votes VALUES (?, ?)  """
        DB.execute(sql, (self.voter_id,self.post_id))
        CONN.commit()

    def count_votes_by_post_id(self, post_id):
        sql = """SELECT COUNT(*) FROM Votes WHERE post_id = ?"""
        DB.execute(sql, self.post_id)
        record = DB.fetchone()

        return record

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("hackbright.db")
    DB = CONN.cursor()

def get_all_posts():
    sql = """SELECT * FROM Posts"""
    DB.execute(sql)
    records = DB.fetchall()

    return records
