from flask import Flask
from flask import render_template
from flask import request
from robotArm import RobotArm

robot = RobotArm()

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    
    if request.method == 'POST':
        base = request.form['base']
        first = request.form['first']
        second = request.form['second']
        third = request.form['third']
        claw = request.form['claw']

        x = request.form['x']
        y = request.form['y']
        phi = request.form['phi']

        
        robot.baseMover(base)
        robot.xarmMover(first)
        robot.sxarmMover(int(second))
        robot.txarmMover(int(third))
        robot.inverseKiematics(int(x), int(y), int(phi))
        
    return render_template('GUI.html')

if __name__ == '__main__':
    app.run(host='192.168.1.224', port=5000)