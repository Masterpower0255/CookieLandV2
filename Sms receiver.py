from flask import Flask, request
from flask_ngrok import run_with_ngrok
import re

app = Flask(__name__)
run_with_ngrok(app)
@app.route('/')

def index():
    return 'Receiving SMS.....'

@app.route('/', methods=['GET', 'POST'])

def inbound_sms():

    Body = request.values.get('Body')
    txt = Body
    x = re.findall('[0-9]+', txt)
    print(x)
    otp = open("OTP.txt", "w")
    otp.write(",".join(x))
    otp.close()
    return 'Body'

if __name__ == '__main__':
    app.run()
