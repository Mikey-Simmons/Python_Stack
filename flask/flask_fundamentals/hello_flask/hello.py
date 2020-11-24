from flask import Flask, render_template 
app = Flask(__name__)   
@app.route('/')          
def hello_world():
    return render_template('index.html', phrase="hello", times = 5)
@app.route('/dojo')
def dojo():
    return "Dojo!" 
@app.route('/<name>')
def hello(name):
    print(name)
    return "Hello, " + name
@app.route('/repeat/<num>/<word>')
def repeat(num,word):
    print(word)
    print(num)
    return word * int(num)
if __name__=="__main__":    
    app.run(debug=True)   