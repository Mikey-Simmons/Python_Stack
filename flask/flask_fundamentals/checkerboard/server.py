from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def eight_check():
    return render_template('index.html')
@app.route('/<x>')
def multiply_table(x):
    return render_template('multiply.html',x = int(x))




if __name__== "__main__":   
    app.run(debug=True)   