

import os
os.chdir(r"A:\Data science")
import socket
import urllib.request,urllib.error,urllib.parse
from bs4 import BeautifulSoup
import ssl
import xml.etree.ElementTree as et
import json
import urllib.request as ur
import urllib.parse as up
import json

#Week 1
class calculator:
    sumy=0
    def __init__(self,p):
     self.name=p
     print(self.name)
    def add(self,a,b):
        print("yo")
        self.x=a
        self.y=b
        self.sumy=self.x+self.y+1
        print("kk",self.name,self.sumy)
        return self.sumy
    def __del__(self):
        print("bye")
app=calculator("ameya")
app2=calculator("GB")
app.add(5,6)
app2.add(7,8)
#print(dir(app))
#app2=45
#print(b)

import sqlite3
import json
conn=sqlite3.connect("Ameyasdb")
cur=conn.cursor()
cur.executescript("""
Drop table if exists user;
Drop table if exists member;
Drop table if exists course;
Create  table user(
id integer not null primary key autoincrement unique,
email Text,
name Text
);

create table course(
id integer not null primary key autoincrement unique,
title text
);
create table member(
user_id integer,
role integer,
course_id
);
""")

fhandle =urllib.request.urlopen("https://raw.githubusercontent.com/AlexGascon/Using-Databases-with-Python---Coursera/master/Unit%204%20-%20Many%20to%20many%20relationships%20in%20SQL/roster_data.json").read()
#fhandle=open("abc.json")
print(type(fhandle))
data=json.loads(fhandle)
print(type(data))

for entry  in data :
    user=entry[0]
    course=entry[1]
    instructor=entry[2]
    cur.execute("""Insert or ignore into user(name) values(?)""",(user,))
    cur.execute("Select id from user where name=?",(user,))
    user_id=cur.fetchone()[0]#selects first entry eliminates duplicates

    cur.execute("""Insert or ignore into course(title) values(?)""", (course,))
    cur.execute("Select id from course where title=?", (course,))
    course_id = cur.fetchone()[0]

    cur.execute('''Insert or replace into member(user_id,course_id,role) values(?,?,?)''',(user_id,course_id,instructor))
conn.commit()
