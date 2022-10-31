
from email.mime import image
from flask import Flask, render_template, request, redirect, url_for, session
import ibm_db
import re 
app = Flask(__name__)

ibm_db.connect("DATABASE=bludb;HOSTNAME=9938aec0-8105-433e-8bf9-0fbb7e483086.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32459;PROTOCOL=TCPIP;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA;UID=dfx98071;PWD:CLKbL1aESH8UhzHO;","","")

@app.route('/')
@app.route('/login', methods =['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        username = request.form['email']
        password = request.form['password']
        stmt = ibm_db.exec_immediate(conn,'SELECT * FROM GIRIJA_DB WHERE email = % s AND password = % s', (email, password, ))
        account = ibm_db.fetch_both(stmt)
        if username==password:
            session['loggedin'] = True
            session['id'] = account['id']
            session['email'] = account['email']
            msg = 'Logged in successfully !'
            return render_template('Loginform1.html', msg = msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('Loginform1.html', msg = msg)

@app.route('/register', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form and 'roll_no' in request.form :
        roll_no = request.form['roll_no']
        username = request.form['username']
        password = request.form['password']
        cpassword = request.form['cpassword']
        email = request.form['email']
        ibm_db.connect("DATABASE=bludb;HOSTNAME=125f9f61-9715-46f9-9399-c8177b21803b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=30426;PROTOCOL=TCPIP;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA;UID=jvl11334;PWD:nfWTlHOgWXhnGx41;","","")
 
        stmt = ibm_db.exec_immediate(conn,'SELECT * FROM GIRIJA_DB')
        if email==cpassword:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not email:
            msg = 'Please fill out the form !'
        else:
            sql=ibm_db.exec_immediate(conn,'INSERT INTO GIRIJA_DB (roll_no, username, email, password, cpassword) VALUES (%s, % s, % s, % s)')
            msg = 'You have successfully registered !'
            print("you have successfully registered!")
            return redirect(url('/login'))
    elif request.method == 'POST':
            msg = 'Please fill out the form !'
    return render_template('registrationform.html', msg = msg)

if __name__=='__main__':
    app.run(debug=True)
