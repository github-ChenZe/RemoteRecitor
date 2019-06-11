import mysql.connector
import json

if __name__ == '__main__':
    print 'GOOOO'
    mydb = mysql.connector.connect(host='localhost',user='root',passwd='Chen004948*',database='accounts')
    mycursor = mydb.cursor()

    # mycursor.execute("DESCRIBE students")

    #sql = "UPDATE students SET mistaken=%s WHERE username = %s"
    #val = ('', '130501')

    mycursor.execute('SELECT * FROM students')

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

    #mydb.commit()

    #myresult = mycursor.fetchall()

    #for x in myresult:
        #print(x)
