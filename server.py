from flask import Flask, request, jsonify,json
import util

app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():

    data = json.loads(request.data)
    print(data)
    sqft = data['total_sqft']
    location = data['location']
    bhk = data['bhk']
    bath = data['bath']





    response = jsonify({
        'estimated_price': util.get_estimated_price(location,sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artefacts()
    app.run(debug=True)