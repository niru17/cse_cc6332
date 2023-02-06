from multiprocessing import connection
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')
#It will route to home page
@app.route('/search')
def search():
   return render_template('search.html')
#It will route to update page   
@app.route('/update')
def updatemain():
   return render_template('update.html')
#It will route to update salary page   
@app.route('/updatesal')
def updatemainsal():
   return render_template('updatesal.html')
#It will route to delete page
@app.route('/delete')
def deletemain():
   return render_template('delete.html')

#It will route to salary range page
@app.route('/salrange')
def salrange():
   return render_template('salrange.html')
#It will route to addpicture page
@app.route('/addpicture')
def addpic():
   return render_template('addpicture.html')
#It will search the record from the table by using name
@app.route('/namesearch', methods=['POST','GET'])
def list():
    connection = sqlite3.connect('names.db')
    cursor = connection.cursor()
    field=str(request.form['name'])
    querry="Select * from people WHERE Name =  '"+field+"' "
    cursor.execute(querry)
    rows = cursor.fetchall()
    connection.close()
    return render_template("getpicture.html",rows = rows)
#It will retrieve all the data from table
@app.route('/all', methods=['POST','GET'])
def fulllist():
    connection = sqlite3.connect('names.db')
    cursor = connection.cursor()
    querry="Select * from people "
    cursor.execute(querry)
    rows = cursor.fetchall()
    connection.close()
    return render_template("list.html",rows = rows)
#It will update keyword of the record from the table by using name
@app.route('/keyupdate',methods=['POST','GET'])
def update():
    if (request.method=='POST'):
        connection = sqlite3.connect('names.db')
        cursor = connection.cursor()
        name= str(request.form['name'])
        keyword= str(request.form['keyword'])
        querry="UPDATE people SET keywords = '"+keyword+"'   WHERE Name ='"+name+"' "
        cursor.execute(querry)
        connection.commit()
        querry2="Select * from people "
        cursor.execute(querry2)
        rows = cursor.fetchall()
        connection.close()
    return render_template("list.html",rows = rows)
#It will add picture to the record from the table by using name
@app.route('/addpic',methods=['POST','GET'])
def addpicture():
    if (request.method=='POST'):
        connection = sqlite3.connect('names.db')
        currsor = connection.cursor()
        name= str(request.form['name1'])
        pic= str(request.form['pic1'])
        querry="UPDATE people SET Picture = '"+pic+"'   WHERE Name ='"+name+"' "
        currsor.execute(querry)
        connection.commit()
        querry2="Select * from people "
        currsor.execute(querry2)
        rows = currsor.fetchall()
        connection.close()
    return render_template("list.html",rows = rows)
#It will update salary of the record from the table by using name
@app.route('/salaryupdate',methods=['POST','GET'])
def chnagesal():
    if (request.method=='POST'):
        connection = sqlite3.connect('names.db')
        cursor = connection.cursor()
        name= str(request.form['name'])
        keyword= str(request.form['sal'])
        querry="UPDATE people SET salary = '"+keyword+"'   WHERE Name ='"+name+"' "
        cursor.execute(querry)
        connection.commit()
        querry2="Select * from people "
        cursor.execute(querry2)
        rows = cursor.fetchall()
        connection.close()
    return render_template("list.html",rows = rows)
#It will delete the record from the table by using name
@app.route('/namedelete', methods=['GET', 'POST'])
def deleterecord():
    if (request.method=='POST'):
        connection = sqlite3.connect('names.db')
        cursor = connection.cursor()
        name= str(request.form['name'])
        querry="DELETE FROM people WHERE Name ='"+name+"' "
        cursor.execute(querry)
        connection.commit()
        querry2="Select * from people "
        cursor.execute(querry2)
        rows = cursor.fetchall()
        connection.close()
    return render_template("list.html",rows = rows)
#It will retrieve the record which is in the given range from the table by using max and min salary
@app.route('/sal', methods=['GET', 'POST'])
def notmatch():
    if (request.method=='POST'):
        connection = sqlite3.connect('names.db')
        cursor = connection.cursor()
        salrange= (request.form['range'])
        querry="select * from people WHERE Salary  <'"+salrange+"'"
        cursor.execute(querry)
        rows = cursor.fetchall()
        connection.close()
    return render_template("getpicture.html",rows = rows)

if __name__ =="__main__":
    app.run(debug=True)
    