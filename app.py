from flask import Flask, jsonify, send_file

app = Flask(__name__)

@app.route('/api/call', methods=['GET'])
def call_api():
    message = "hello api called"
    
    # Save the message to a text file
    with open('output.txt', 'a') as file:
        file.write(message + '\n')
    
    return jsonify({"message": message})

@app.route('/api/view', methods=['GET'])
def view_file():
    try:
        # Send the output.txt file for download/viewing
        return send_file('output.txt', as_attachment=False)
    except FileNotFoundError:
        return jsonify({"error": "File not found!"}), 404

if __name__ == '__main__':
    app.run(debug=True)
