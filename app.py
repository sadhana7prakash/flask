from flask import Flask,render_template, request
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def hello_world():
    return render_template('index.html',name = '')
@app.route('/input', methods =['POST'])
def input():
    if request.method == 'POST':
        name = request.form['name']
        return 'Hello ' + name
@app.route('/home')
def home():
    return "Welcome to home page.."
@app.route('/about')
def about():
    return 'about'
if __name__ == '__main__':
    app.run(debug = True)
