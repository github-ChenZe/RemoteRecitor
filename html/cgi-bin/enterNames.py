import mysql.connector
import json

names = open("namelist")
out = open("passwordlist", 'w')

if __name__ == '__main__':

    mydb = mysql.connector.connect(host='localhost',user='root',passwd='Chen004948*',database='accounts')
    mycursor = mydb.cursor()

    letters = [chr(i) for i in range(97, 97 + 26)]
    digits = [chr(i) for i in range(48, 48 + 10)]
    dictionary = digits + letters

    for line in names.readlines():
        line = line.strip()
        username = line[:6]
        realname = line[6:]
        name = json.dumps(line[6:])
        print '(' + username + ')'
        print '(' + name + ')'
        print line
        usernameVal = int(username)
        mistaken = ''

        passwordDigits = []
        usernameVal = usernameVal * usernameVal * usernameVal * usernameVal

        for i in range(0, 6):
            passwordDigits.insert(0, dictionary[usernameVal % 36])
            usernameVal /= 36

        password = ''.join(passwordDigits)

        sql = "INSERT INTO students (username, password, name, mistaken) VALUES (%s, %s, %s, %s)"
        val = (username, password, name, mistaken)

        out.write(username + '\t')
        out.write(realname + '  \t')
        out.write(password)
        out.write('\n')

        mycursor.execute(sql, val)

        mydb.commit()

        # myresult = mycursor.fetchall()

        # for x in myresult:
        #     print(x)

out.close()
