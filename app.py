from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Dummy database for demonstration purposes
customers = {
    "1": {"accountId": "1", "firstName": "John", "lastName": "Doe", "kycStatus": "verified"},
    "2": {"accountId": "2", "firstName": "Jane", "lastName": "Doe", "kycStatus": "pending"},
}

@app.route('/customer/<accountId>', methods=['GET'])
def get_customer_by_id(accountId):
    """
    Retrieve a customer by account id.
    """
    customer = customers.get(accountId)
    if not customer:
        # If the customer is not found, return a 404 error
        abort(404, description="Unable to find the Customer")
    return jsonify(customer), 200

@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

if __name__ == '__main__':
    app.run(debug=True, port=8080)