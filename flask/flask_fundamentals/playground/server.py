from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play')
def play_page():
    return render_template('index.html')

@app.route('/play/<x>')
def box_multiply(x):
    return render_template('multiply.html', x =int(x))
@app.route('/play/<x>/<color>')
def color_page(x,color):
    return render_template('color.html', x=int(x),color= color )


if __name__=="__main__":    
    app.run(debug=True)   