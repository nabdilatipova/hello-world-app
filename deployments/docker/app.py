from flask import Flask,  jsonify 
import os 
app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({
        'message': 'Hello I am a developer my name is Nasyikat',
        'environment': os.environ.get('ENVIRONMENT'),
        'owner': 'nasyikat',
        'namespace': os.environ.get('NAMESPACE')
    })

@app.route('/nasyikat')
def comming_soon():
    return jsonify({
        'message': 'This Nasyikats page'
    })


@app.route('/soon')
def comming_soon():
    return jsonify({
        'message': 'This is comming soon page!!'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)