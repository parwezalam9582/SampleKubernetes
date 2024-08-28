from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        print(f"Received data: {data}")
        
        # Extract and convert the numbers from the received JSON data
        Number1 = int(data.get('Number1', 0))
        Number2 = int(data.get('Number2', 0))
        Number3 = int(data.get('Number3', 0))
        Number4 = int(data.get('Number4', 0))
        
        # Calculate the sum of the two numbers
        answer = Number1 + Number2 +Number3 +Number4
        
        # Return the result as a JSON response
        return jsonify({'answer': answer})

    except KeyError as e:
        print(f"KeyError: {e}")
        return jsonify({'error': f"KeyError: {e}"}), 400
    except Exception as e:
        print(f"Exception: {e}")
        return jsonify({'error': f"Exception: {e}"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

