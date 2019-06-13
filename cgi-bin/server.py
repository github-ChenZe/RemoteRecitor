#!/usr/bin/python

import cgi
import json
import recitor
import mysql.connector


print "Content-type: text/plain"
print "Access-Control-Allow-Origin: *"
print


form = cgi.FieldStorage()
subject = form.getvalue("subject")

if subject == 'login':

    mydb = mysql.connector.connect(host='localhost',user='root',passwd='Chen004948*',database='accounts')
    mycursor = mydb.cursor()
    sql = 'SELECT * FROM students WHERE username=%s AND password=%s'
    val = (form.getvalue("username"), form.getvalue("password"))
    mycursor.execute(sql,val)
    myresult = mycursor.fetchone()
    if myresult is not None:
        userinfo = {}
        userinfo['name'] = json.loads(myresult[2])
        userinfo['username'] = myresult[0]
        userinfo['mistaken'] = myresult[4]
        print 'OK ' + json.dumps(userinfo)
    else:
        print 'DENIED'

elif subject == 'mistaken':
    username = form.getvalue("username");
    password = form.getvalue("password");
    mistakenDir = form.getvalue("dir");
    index = form.getvalue("index");

    mydb = mysql.connector.connect(host='localhost',user='root',passwd='Chen004948*',database='accounts')
    mycursor = mydb.cursor()
    sql = 'SELECT * FROM students WHERE username=%s AND password=%s'
    val = (username, password)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchone()
    if myresult is not None:
        mistaken = myresult[4]
    
    originalMistaken = []
    if len(mistaken) > 0:
        originalMistaken = json.loads(mistaken)
    mistakenData = { 'dir': mistakenDir, 'index': index }

    alreadyContained = False

    for item in originalMistaken:
        if item["dir"] == mistakenData["dir"] and item["index"] == mistakenData["index"]:
            alreadyContained = True
            break

    if not alreadyContained: 
        originalMistaken.append(mistakenData)

    mistakenJson = json.dumps(originalMistaken)

    sql = "UPDATE students SET mistaken=%s WHERE username = %s"
    val = (mistakenJson, username)
    mycursor.execute(sql, val)
    mydb.commit()

    print 'MISTAKEN ' + mistakenJson

else:

    options = int(form.getvalue("options"))

    new_question = recitor.new_question(subject, options)
    new_question['state'] = 'success'

    print json.dumps(new_question)
    
