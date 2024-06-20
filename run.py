from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a route to handle POST requests
@app.route('/run-script', methods=['POST'])
def run_script():
    # Assuming the script expects some input data from the request
    data = request.get_json()

    # Example: Process the input data (you can modify this part as per your script's logic)
    if 'name' in data:
        result = f"Hello, {data['name']}!"
    else:
        result = "Hello, anonymous!"

    # Return the result as JSON
    return jsonify({'result': result})

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True, host='https://run-yhq1.onrender.com', port=5000)
