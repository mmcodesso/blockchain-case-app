import hashlib
import time
from flask import Flask, request, render_template
import json

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

def calculate_hash(index, previous_hash, timestamp, data):
    value = str(index) + str(previous_hash) + str(timestamp) + str(data)
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

def create_genesis_block():
    return Block(0, "0", int(time.time()), {"student_name": "NA", "course_name": "NA", "professor_name": "NA"}, calculate_hash(0, "0", int(time.time()), "Genesis Block"))

def create_new_block(previous_block, student_name, course_name, professor_name):
    index = previous_block.index + 1
    timestamp = int(time.time())
    data = {
        "student_name": student_name,
        "course_name": course_name,
        "professor_name": professor_name
    }
    hash = calculate_hash(index, previous_block.hash, timestamp, str(data))
    return Block(index, previous_block.hash, timestamp, data, hash)

blockchain = [create_genesis_block()]
previous_block = blockchain[0]

app = Flask(__name__)

@app.route('/blockchain')
def get_chain():
    chain_data = []
    for block in blockchain:
        chain_data.append({
            "index": block.index,
            "previous_hash": block.previous_hash,
            "timestamp": block.timestamp,
            "data": block.data,
            "hash": block.hash
        })
    return json.dumps({"length": len(chain_data), "chain": chain_data}, default=str)



@app.route('/add', methods=['GET', 'POST'])
def add_block():
    if request.method == 'POST':
        data = request.get_json()
        previous_block = blockchain[len(blockchain) - 1]
        new_block = create_new_block(previous_block, data["student_name"], data["course_name"], data["professor_name"])
        blockchain.append(new_block)
        return "Block added to the blockchain", 200
    else:
        return "Error: Invalid request" + str(request.method), 400

@app.route('/view')
def view_form():
    return render_template('index.html')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/assignment')
def assignment():
    return render_template('assignment.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
