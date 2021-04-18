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

        try:
            robot.baseMover(int(base))
        except:
            try:
                robot.xarmMover(int(first))
            except:
                try:
                    robot.sxarmMover(int(second))
                except:
                    try:
                        robot.txarmMover(int(third))
                    except:
                        try:
                            robot.inverseKiematics(int(x), int(y), int(phi))
                        except:
                            print("fuck it")

    
    return render_template('GUI.html')

if __name__ == '__main__':
    app.run(host='192.168.1.224', port=5000)