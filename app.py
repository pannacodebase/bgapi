from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/call', methods=['GET'])
def call_api():
    message = "hello api called"
    
    # Save the message to a text file
    with open('output.txt', 'a') as file:
        file.write(message + '\n')
    
    return jsonify({"message": message})

if __name__ == '__main__':
    app.run(debug=True)
