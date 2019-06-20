#!/usr/bin/python

import cgi
import mysql.connector
import json
import re

print "Content-type: text/plain"
print "Access-Control-Allow-Origin: *"
print

if True:
    mydb = mysql.connector.connect(host='localhost',user='root',passwd='Chen004948*',database='accounts')
    mycursor = mydb.cursor()

    allErrs = {}

    # mycursor.execute("DESCRIBE students")

    #sql = "UPDATE students SET mistaken=%s WHERE username = %s"
    #val = ('', '130501')

    mycursor.execute('SELECT * FROM students')

    myresult = mycursor.fetchall()

    i = 0

    regex = re.compile('"index": "([0-9]+)"')

    for x in myresult:
        if x[0].startswith('16') and len(x[4]) > 0:
            errs = x[4]
            # print(x[0])
            it = re.finditer(regex, errs)
            for match in it:
                # print match.group(1)
                if not match.group(1) in allErrs:
                    allErrs[match.group(1)] = 1
                else:
                    allErrs[match.group(1)] += 1
            # print ""
            i += 1

    print '%d students had finished'%i
    # print allErrs

    pairs = []
    for k, v in allErrs.items():
        pairs.append((int(k), v))
    pairs.sort(key=lambda x: x[1])
    print "<table>"
    for item in pairs:
        print "<tr><td>%s</td><td>%s</td></tr>"%item
    print "</table>"

    print

    #mydb.commit()

    #myresult = mycursor.fetchall()

    #for x in myresult:
        #print(x)
