from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('main.html')

@app.route('/cestarovne1')
def cestarovne1():
    return render_template('cestarovne1.html')

@app.route('/krizovatka1')
def krizovatka1():
    return render_template('krizovatka1.html')

@app.route('/cestarovnevedenaslepou')
def cestarovnevedenaslepou():
    return render_template('cestarovnevedenaslepou.html')

@app.route('/cestarovne2')
def cestarovne2():
    return render_template('cestarovne2.html')

@app.route('/deadend1')
def deadend1():
    return render_template('deadend1.html')

@app.route('/krizovatka2')
def krizovatka2():
    return render_template('krizovatka2.html')

@app.route('/deadend2')
def deadend2():
    return render_template('deadend2.html')

@app.route('/konec')
def konec():
    return render_template('konec.html')