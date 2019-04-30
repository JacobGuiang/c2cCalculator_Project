from flask import Flask, request, render_template
import math
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    # found in ../templates/
    return render_template("index.html")

@app.route('/process_inputsQ', methods=['POST'])
def process_inputsQ():
    aStr = request.form.get('qInput_a', '')
    bStr = request.form.get('qInput_b', '')
    cStr = request.form.get('qInput_c', '')
    a = float(aStr)
    b = float(bStr)
    c = float(cStr)
    d = b**2 - 4*a*c
    if d < 0:
        return render_template("index.html", scroll= "quadratics", output2= "no real solutions")
    elif d == 0:
        x = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
        return render_template("index.html", scroll= "quadratics", output2= "x = " + str(x))
    elif a == 0:
        return render_template("index.html", scroll= "quadratics", output2= "a cannot be 0")
    else:
        x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
        x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
        return render_template("index.html", scroll= "quadratics", output2= "x = " + str(x1) + "<br>" + "x = " + str(x2))

@app.route('/process_inputsK', methods=['POST'])
def process_inputsK():
    xStr = request.form.get('kInput_displacement', '')
    vNaughtStr = request.form.get('kInput_vNaught', '')
    vStr = request.form.get('kInput_v', '')
    aStr = request.form.get('kInput_a', '')
    tStr = request.form.get('kInput_t', '')

    if all([xStr, vNaughtStr, vStr, aStr, tStr]):
        return render_template("index.html", scroll= "kinematics", output= "displacement = " + xStr + "<br>" + "initial velocity = " + vNaughtStr + "<br>" + "final velocity = " + vStr + "<br>" + "acceleration = " + aStr + "<br>" + "time = " + tStr)
    elif all([vNaughtStr, aStr, tStr]):
        vNaught = float(vNaughtStr)
        a = float(aStr)
        t = float(tStr)
        try:
            v = vNaught + a*t
            x = ((v + vNaught)/2)*t
            return render_template("index.html", scroll= "kinematics", output= "displacement = " + str(x) + "<br>" + "initial velocity = " + str(vNaught) + "<br>" + "final velocity = " + str(v) + "<br>" + "acceleration = " + str(a) + "<br>" + "time = " + str(t))
        except ValueError:
            return render_template("index.html", scroll= "kinematics", output = "invalid inputs; re-enter values")
    elif all([vStr, aStr, tStr]):
        v = float(vStr)
        a = float(aStr)
        t = float(tStr)
        try:
            vNaught = v-(a*t)
            x = ((v + vNaught)/2)*t
            return render_template("index.html", scroll= "kinematics", output= "displacement = " + str(x) + "<br>" + "initial velocity = " + str(vNaught) + "<br>" + "final velocity = " + str(v) + "<br>" + "acceleration = " + str(a) + "<br>" + "time = " + str(t))
        except ValueError:
            return render_template("index.html", scroll= "kinematics", output = "invalid inputs; re-enter values")
    elif all([vNaughtStr, vStr, aStr]):
        vNaught = float(vNaughtStr)
        v = float(vStr)
        a = float(aStr)
        try:
            if a != 0:
                t = (v-vNaught)/a
                x = ((v + vNaught)/2)*t
                return render_template("index.html", scroll= "kinematics", output= "displacement = " + str(x) + "<br>" + "initial velocity = " + str(vNaught) + "<br>" + "final velocity = " + str(v) + "<br>" + "acceleration = " + str(a) + "<br>" + "time = " + str(t))
            else:
                return render_template("index.html", scroll= "kinematics", output= "initial velocity = " + str(vNaught) + "<br>" + "final velocity = " + str(v) + "<br>" + "acceleration = " + str(a))
        except ValueError:
            return render_template("index.html", scroll= "kinematics", output = "invalid inputs; re-enter values")
    elif all([vNaughtStr, vStr, tStr]):
        vNaught = float(vNaughtStr)
        v = float(vStr)
        t = float(tStr)
        try:
            if t != 0:
                a = (v-vNaught)/t
                x = ((v + vNaught)/2)*t
                return render_template("index.html", scroll= "kinematics", output= "displacement = " + str(x) + "<br>" + "initial velocity = " + str(vNaught) + "<br>" + "final velocity = " + str(v) + "<br>" + "acceleration = " + str(a) + "<br>" + "time = " + str(t))
            else:
                return render_template("index.html", scroll= "kinematics", output= "initial velocity = " + str(vNaught) + "<br>" + "final velocity = " + str(v) + "<br>" + "time = " + str(t))
        except ValueError:
            return render_template("index.html", scroll= "kinematics", output = "invalid inputs; re-enter values")
    elif all([xStr, vStr, vNaughtStr]):
        x = float(xStr)
        v = float(vStr)
        vNaught = float(vNaughtStr)
        try:
            if v+vNaught != 0:
                t = x*2/(v+vNaught)
                if t != 0:
                    a = (v-vNaught)/t
                else:
                    a = 0
            else:
                t = "&infin;"
                a = 0
            return render_template("index.html", scroll= "kinematics", output= "displacement = " + str(x) + "<br>" + "initial velocity = " + str(vNaught) + "<br>" + "final velocity = " + str(v) + "<br>" + "acceleration = " + str(a) + "<br>" + "time = " + str(t))
        except ValueError:
            return render_template("index.html", scroll= "kinematics", output = "invalid inputs; re-enter values")
    elif all([xStr, vStr, tStr]):
        x = float(xStr)
        v = float(vStr)
        t = float(tStr)
        try:
            if t != 0:
                vNaught = x/t*2-v
                a = (v-vNaught)/t
                return render_template("index.html", scroll= "kinematics", output= "displacement = " + str(x) + "<br>" + "initial velocity = " + str(vNaught) + "<br>" + "final velocity = " + str(v) + "<br>" + "acceleration = " + str(a) + "<br>" + "time = " + str(t))
            else:
                return render_template("index.html", scroll= "kinematics", output= "displacement = " + str(x) + "<br>" + "final velocity = " + str(v) + "<br>" + "time = " + str(t))
        except ValueError:
            return render_template("index.html", scroll= "kinematics", output = "invalid inputs; re-enter values")
    elif all([xStr, vNaughtStr, tStr]):
        x = float(xStr)
        vNaught = float(vNaughtStr)
        t = float(tStr)
        try:
            if t != 0:
                v = x/t*2-vNaught
                a = (v-vNaught)/t
                return render_template("index.html", scroll= "kinematics", output= "displacement = " + str(x) + "<br>" + "initial velocity = " + str(vNaught) + "<br>" + "final velocity = " + str(v) + "<br>" + "acceleration = " + str(a) + "<br>" + "time = " + str(t))
            else:
                return render_template("index.html", scroll= "kinematics", output= "displacement = " + str(x) + "<br>" + "initial velocity = " + str(vNaught) + "<br>" + "time = " + str(t))
        except ValueError:
            return render_template("index.html", scroll= "kinematics", output = "invalid inputs; re-enter values")
    elif all([vNaughtStr, aStr, xStr]):
        vNaught = float(vNaughtStr)
        a = float(aStr)
        x = float(xStr)
        try:
            v = math.sqrt(vNaught**2+2*a*x)
            if (v+vNaught) != 0:
                t = x*2/(v+vNaught)
                return render_template("index.html", scroll= "kinematics", output= "displacement = " + str(x) + "<br>" + "initial velocity = " + str(vNaught) + "<br>" + "final velocity = " + str(v) + "<br>" + "acceleration = " + str(a) + "<br>" + "time = " + str(t))
            else:
                return render_template("index.html", scroll= "kinematics", output= "displacement = " + str(x) + "<br>" + "initial velocity = " + str(vNaught) + "<br>" + "final velocity = " + str(v) + "<br>" + "acceleration = " + str(a))
        except ValueError:
            return render_template("index.html", scroll= "kinematics", output = "invalid inputs; re-enter values")
    elif all([vStr, aStr, xStr]):
        v = float(vStr)
        a = float(aStr)
        x = float(xStr)
        try:
            vNaught = math.sqrt(v**2-2*a*x)
            if (v+vNaught) != 0:
                t = x*2/(v+vNaught)
                return render_template("index.html", scroll= "kinematics", output= "displacement = " + str(x) + "<br>" + "initial velocity = " + str(vNaught) + "<br>" + "final velocity = " + str(v) + "<br>" + "acceleration = " + str(a) + "<br>" + "time = " + str(t))
            else:
                return render_template("index.html", scroll= "kinematics", output= "displacement = " + str(x) + "<br>" + "initial velocity = " + str(vNaught) + "<br>" + "final velocity = " + str(v) + "<br>" + "acceleration = " + str(a))
        except ValueError:
            return render_template("index.html", scroll= "kinematics", output = "invalid inputs; re-enter values")
    else:
        return render_template("index.html", scroll= "kinematics", output = "invalid inputs; re-enter values")