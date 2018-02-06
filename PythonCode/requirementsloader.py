# -*- coding: utf-8 -*-
"""
Created on Mon Nov 06 15:38:41 2017

@author: Sachal
"""
import csv, pyodbc

myserver = 'GHOSTPROGS60' 
mydatabase = 'DAEN690' 
db = pyodbc.connect('Trusted_Connection=yes', driver = '{SQL Server}',server = myserver, database = mydatabase)
cur = db.cursor()

myFile = open('reqts.csv')
myReader = csv.reader(myFile)

lst_reqts = []

for eachRow in myReader:
    if eachRow[0] != '' or eachRow[1]!='':
        lst_reqts.append((eachRow[1],eachRow[0][2:]))


Query_Insert = '''INSERT INTO tbl_Requirements (Reqt_text, Reqt_ChapterSource) 
                    VALUES (?,?)'''



cur.executemany(Query_Insert,lst_reqts)


lst_Votes = []
Query_GetReqtID = '''SELECT Reqt_ID from tbl_Requirements'''
cur.execute(Query_GetReqtID)
rows = cur.fetchall();
for eachRow in rows:
    lst_Votes.append((eachRow[0],0,0))

print lst_Votes[2],lst_Votes[3]



Query_VoteTable = '''INSERT INTO tbl_VoteCount(ReqtID,CountYes,CountNo)
                    VALUES (?,?,?)'''
cur.executemany(Query_VoteTable,lst_Votes)


db.commit()