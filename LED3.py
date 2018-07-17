from flask import Flask,request,render_template,jsonify
from gpiozero import LED
#from led_on import LED_ON
#from led_off import LED_OFF

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
if __name__ =='__main__':
    app.run(host='0.0.0.0', debug=True)

