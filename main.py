from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def recieve_data():
    email = request.form['email']
    password = request.form['password']
    message = request.form['msg']
    
    
    MY_EMAIL = 'anshsoni702@gmail.com'
    PASSWORD = 'hnae syae ioqr rney'
            
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        encoded_string = message.encode('utf-8')
        connection.sendmail(from_addr=email, to_addrs=MY_EMAIL, msg=encoded_string)

    return f'<h2>Message Sent Successfully!</h2>'
    
if __name__=='__main__':
    app.run(debug=True)