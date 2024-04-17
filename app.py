from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! small change here for testii</p>"
def get_data():
    data = {'message':'FLASKIN VIESTI!'}
    return jsonify(data)

if  __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port = 8080) #4x0 answers for any user