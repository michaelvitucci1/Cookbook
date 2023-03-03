from flask import Flask, jsonify, request

app = Flask(__name__)

pantry = [
    {'type': 'food',
     'name': 'onions',
     'date-purchased': '02-23-2023',
     'quantity': 5
     },
     {'type': 'food',
     'name': 'carrots',
     'date-purchased': '02-23-2023',
     'quantity': 5
     },
     {'type': 'beverage',
     'name': 'milk',
     'date-purchased': '02-23-2023',
     'quantity': 2
     },
     {'type': 'food',
     'name': 'onions',
     'date-purchased': '02-23-2023',
     'quantity': 5
     }
]

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/pantry",methods=["POST", "GET"])
def hello_name():
    if request.method == "GET":
        return jsonify(pantry)
    if request.method == "POST":
        return jsonify(pantry)

@app.route("/pantry/<type>")
def get_food_by_type(type):
    types = []
    for item in pantry:
        if type == item['type']:
            types.append(item)
    return jsonify(types)
