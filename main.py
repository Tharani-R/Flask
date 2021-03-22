from flask import Flask

app = Flask(__name__)

@app.route('/')
def base_route():
    return "Hello world"

@app.route('/hello/<int:number>')
def hello(number):
    if number <= 10: return f"hello {number}", 200
    if number >= 11: return f"hello {number}", 206

if __name__=="__main__":
    app.run(debug=True)
