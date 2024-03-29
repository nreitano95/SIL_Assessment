from flask import Flask, request    # Using flask to serve API Endpoint
import os                           # Using os to identify port
import json                         # Using json module to manipulate json data 
import pandas as pd                 # Using Pandas to faciltate data querying in .csv files

# Configuration
app = Flask(__name__)

 
@app.route('/')
def root():
   """ 
   Root of Flask Application. Could be used in future development.
   """
   return "Web Interface Not Used. Request POST data from http://localhost:8545/post-data."


@app.route('/post-data')
def get_data():
    """ 
    Method to handle GET request to the '/post-data' endpoint. 
    GET not used; therefore, returns a help message.
    """
    return "Web Interface Not Used. Obtain POST response data via command line."


@app.route('/post-data', methods=['POST'])
def post_data():
    """
    Receives a POST request and calls the query_csv method with the request data as the parameter.
    Returns the JSON data of all of the entries related to the title or author.
    """
    # Interpret application/json content type only
    if (request.headers.get('Content-Type') == 'application/json'):
        data = request.json
        data = query_csv(data)
        return data

    else:
        return json.dumps({"Failure": "Content-Type not supported."}), 201


def query_csv(request_data):
    """ 
    Given a POST request JSON object, query the .csv file located in the root folder. 
    Return JSON object containing all entries related to the title or author.
    """
    
    # Use Pandas to read .csv file
    data = pd.read_csv("dataForPart2B.csv", encoding="UTF-32")

    # Query the .CSV file based on the user-defined JSON input.
    if {'title', 'author'} <= request_data.keys():
        # Author or title
        data = data[(data['title'].str.contains(request_data['title'], na=False)) | (data['author'].str.contains(request_data['author'], na=False))]

    elif request_data.__contains__('author'):
        # Author only
        data = data[data['author'].str.contains(request_data['author'], na=False)]

    elif request_data.__contains__('title'):
        # Title only
        data = data[data['title'].str.contains(request_data['title'], na=False)]

    else: 
        # Invalid Input
        return "\n**** Incorrect JSON format used. Please see correct usage. ****\n"
    
    # Use the Pandas module to format the data 
    data = data.to_json(orient='records', lines=True)
    
    # If the queried data contains at least one entry, return the data.
    if data.__contains__('id'):
        return data
    else: 
        return "\n**** No entries related to requested title or author. ****\n"


# Listener 
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8545))
    app.run(port=port, debug=True) 


