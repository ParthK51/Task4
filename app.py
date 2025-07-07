from flask import Flask, jsonify
import json
import os
#first project
app = Flask(__name__)

DATA_FILE = 'D:\DEVo\python\Flaskwork\data.json'

@app.route('/')
def home():
    return "MY first Flask Project"
@app.route('/api')
def get_data():
  
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
