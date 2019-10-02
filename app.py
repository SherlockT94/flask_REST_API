from flask import Flask, jsonify, request

app = Flask(__name__)
# stores must be a dictionary to be converted to a JSON string
# JSON is used to transmit data over internet via a perfect defined format
# Always using "" instead of ''
stores = [{
    "name": "My Wonderful Store",
    "items": [{
        "name": "My Item",
        "price": 15.99
    }]
}]
# From server view:
# POST - used to receive data
# Get - used to send data back only

# @app.route("/")
# def home():
# return "hello, world!"


# POST /store data:{name:}
@app.route("/store", methods=["POST"])
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": request_data["items"]}
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string:name>
@app.route("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify(store)
    return jsonify({"message": "store not found"})


# GET /store
@app.route("/store")
def get_stores():
    #TODO(SherlockTang): Finishing the funtion that reture a list of stores
    return jsonify({"stores": stores})


# POST /store/<string:name>/item {name:, price:}
@app.route("/store/<string:name>/item", methods=["POST"])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store[name] == name:
            new_item = {
                "name": request_data["name"],
                "price": request_data["price"]
            }
            store["items"].append(new_item)
            return jsonify(new_item)
    return jsonify({"message": "store not found"})


# get /store/<string:name>/item
@app.route("/store/<string:name>/item")
def get_item_in_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify({"items": store["items"]})
    return jsonify({"message": "store not found"})


app.run(port=5000)
