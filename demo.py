from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/", methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/greet_get", methods=['GET'])
def greet_by_get():
    return "Hello"

@app.route("/greet_post", methods=['POST'])
def greet_by_post():
    name = request.json['Name']
    age = request.json['Age']
    univ = request.json['University']
    return name + "\n" + age + "\n" + univ
    
if __name__ == '__main__':
    app.run(debug=True)