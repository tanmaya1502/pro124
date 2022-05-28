from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {
         "id":1,
        "Name":u'angella',
        "contact":"982142625",
        "done":False
    }
]

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    contact = {
        'id': tasks[-1]['id'] + 1,
        'name': request.json['name',""],
        'contact': request.json.get('contact', ""),
        'done': False
    }
    tasks.append(contact)
    return jsonify({
        "status":"success",
        "message": "Contact added succesfully!"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : tasks
    }) 

if(__name__ == "__main__"):
    app.run(debug=True)