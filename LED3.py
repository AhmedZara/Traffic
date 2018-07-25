from flask import Flask,request,render_template,jsonify
from gpiozero import LED
import time

app = Flask(__name__)
RED=LED(15)
YELLOW= LED(17)
GREEN= LED(18)

@app.route('/',methods=['GET'])
def index():
        return render_template('index.html')

@app.route('/redpin_on', methods=['GET', 'POST'])
def redpin_on():
    if request.method == 'POST':
        body=request.get_json()
        RED.on()
        return jsonify({'status' : ' RED LED_ON(body[])'})
    else:
        return jsonify({'status: unavailable'})
@app.route('/redpin_off', methods=['GET', 'POST'])
def redpin_off():
    if request.method == 'POST':
        body=request.get_json()
        RED.off()
        return jsonify({'status' : 'RED LED_OFF(body[])'})
    else:
        return jsonify({'status: unavailable'})
@app.route('/yellowpin_on', methods=['GET', 'POST'])
def yellowpin_on():
    if request.method == 'POST':
        body=request.get_json()
        YELLOW.on()
        return jsonify({'status' : 'YELLOW LED_ON(body[])'})
    else:
        return jsonify({'status: unavailable'})
@app.route('/yellowpin_off', methods=['GET', 'POST'])
def yellowpin_off():
    if request.method == 'POST':
        body=request.get_json()
        YELLOW.off()
        return jsonify({'status' : 'YELLOW LED_OFF(body[])'})
    else:
        return jsonify({'status: unavailable'})
@app.route('/greenpin_on', methods=['GET', 'POST'])
def greenpin_on():
    if request.method == 'POST':
        body=request.get_json()
        GREEN.on()
        return jsonify({'status' : ' GREEN LED_ON(body[])'})
    else:
        return jsonify({'status: unavailable'})
@app.route('/greenpin_off', methods=['GET', 'POST'])
def greenpin_off():
    if request.method == 'POST':
        body=request.get_json()
        GREEN.off()
        return jsonify({'status' : ' GREEN LED_OFF(body[])'})
    else:
        return jsonify({'status: unavailable'})

@app.route('/leds_on', methods=['GET', 'POST'])
def leds_on():
        RED1=LED(15)
        YELLOW1= LED(17)
        GREEN1= LED(18)
    if request.method == 'POST':
        body=request.get_json()
        for i in range(0,5):
            RED1.on()
            time.sleep(3)
            RED1.off()
            time.sleep(0.5)
            YELLOW1.on()
            time.sleep(2)
            YELLOW1.off()
            time.sleep(0.5)
            GREEN1.on()
            time.sleep(2)
            GREEN1.off()
            time.sleep(0.5)
        return jsonify({'status' : 'LEDs_ON(body[])'})
    else:
        return jsonify({'status: unavailable'})

if __name__ =='__main__':
    app.run(host='0.0.0.0', debug=True)

