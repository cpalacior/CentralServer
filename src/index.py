from flask import Flask
import json
from flask import jsonify
from flask import request
import os

absolute_path = os.path.dirname(__file__)
relative_path = "src/lib"
full_path = os.path.join(absolute_path, relative_path)

# instance of flask application
app = Flask(__name__)

def listResources():
    file = ''
    with open(os.path.dirname(__file__) + '/database/resources.json') as resources:
        file = json.load(resources)
    return file

def getResourcePath(file, resourceName):
    for peer in file:
        for resource in file[peer]["resources"]:
            print(resource)
            if resource == resourceName:
                return 'http://' + file[peer]["url"] + ':' + file[peer]["port"]
    return '404'

# home route that returns below text 
# when root url is accessed

@app.route("/download" , methods=['GET', 'POST'])
def downloadResource():
    try:
        data = request.json
        print(data["body"])
        resourcesFile = listResources()
        resourcePath = getResourcePath(resourcesFile, data["body"])
        print(resourcePath)
    except Exception as e:
        resourcePath = {"error": e}
        print(e)
    return jsonify(resourcePath)

@app.route("/upload")
def uploadResource():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(debug=True, port=3002)