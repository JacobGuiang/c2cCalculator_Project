from flask import Flask, request, render_template
import math
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    # found in ../templates/
    return render_template("index.html")

@app.route('/process_inputs', methods=['POST'])
def process_inputs():
    aStr = request.form.get('input_a', '')
    bStr = request.form.get('input_b', '')
    cStr = request.form.get('input_c', '')
    a = float(aStr)
    b = float(bStr)
    c = float(cStr)
    d = b**2 - 4*a*c
    if d < 0:
        return render_template("index.html", output= "no real solutions")
    elif d == 0:
        x = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
        return render_template("index.html", output= "x = " + str(x))
    elif a == 0:
        return render_template("index.html", output= "a cannot be 0")
    else:
        x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
        x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
        return render_template("index.html", output= "x = " + str(x1) + " x = " + str(x2))
