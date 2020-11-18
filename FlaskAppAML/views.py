"""
Routes and views for the flask application.
"""

from flask import render_template, request
from FlaskAppAML import app
from FlaskAppAML.forms import SubmissionForm
from datetime import datetime
import json
import urllib.request
import os
# import rdsconnection as db

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    # details = db.get_all()
    # # print(details)
    # for detail in details:
    #     var = detail
    
    return render_template("index.html")

@app.route('/basketball')
def basketball():
    bball_key = os.environ.get('API_KEY', "3ykY3j9WZDYvS0Dvf5VoJ1kA0yVT5HVzT+foY4SzKvD6LJhHoysBjlEQWaOniNQCGqsjKrytONq1kdxEWo3Scg==")
    bball_url = os.environ.get('URL', "https://ussouthcentral.services.azureml.net/workspaces/91af20abfc58455182eaaa615d581c59/services/da7cdb9359a443f0abdef36d30ce8f1c/execute?api-version=2.0&details=true")
    
    B_HEADERS = {'Content-Type':'application/json', 'Authorization':('Bearer '+ bball_key)}

    form = SubmissionForm(request.form)

    # Form has been submitted
    if request.method == 'POST' and form.validate():

        # Plug in the data into a dictionary object 
        #  - data from the input form
        #  - text data must be converted to lowercase
        data =  {
              "Inputs": {
                "input1": {
                  "ColumnNames": ["gender", "age", "size", "weight"],
                  "Values": [ [
                      0,
                      1,
                      form.title.data.lower(),
                      0

                    ]
                  ]
                }
              },
              "GlobalParameters": {}
            }

        # Serialize the input data into json string
        body = str.encode(json.dumps(data))
    
        req = urllib.request.Request(bball_url, body, B_HEADERS)

        # Send this request to the AML service and render the results on page
        try:
            # response = requests.post(URL, headers=HEADERS, data=body)
            response = urllib.request.urlopen(req)
            #print(response)
            respdata = response.read()
            result = json.loads(str(respdata, 'utf-8'))
            result = do_something_pretty(result)
            # result = json.dumps(result, indent=4, sort_keys=True)
            return render_template(
                'result.html',
                title="This is the result from AzureML running our Basketball Draft Prediction:",
                result=result)

        # An HTTP error
        except urllib.error.HTTPError as err:
            result="The request failed with status code: " + str(err.code)
            return render_template(
                'result.html',
                title='There was an error',
                result=result)
            #print(err)

    return render_template(
        'basketball.html',
        form = form,
        title = 'Run App',
        year=datetime.now().year,
        message = 'Will you be drafted?'
    )

@app.route('/football', methods=['GET', 'POST'])
def football():
    fball_key = os.environ.get('API_KEY', "Jur+v2F7MlT70r85jA7F3Ntt48vBoSkZGlg67g7VihkF+/jNwxI8mSOpqY1ADz4nz5+HUMLLB6LJ2gaDGalJwg==")
    fball_url = os.environ.get('URL', "https://ussouthcentral.services.azureml.net/workspaces/1bd82c355c1447d591afec4715a4b045/services/27f2c06eb9ad492db435e9999a272af4/execute?api-version=2.0&format=swagger")

    F_HEADERS = {'Content-Type':'application/json', 'Authorization':('Bearer '+ fball_key)}

    form = request.form

    # Form has been submitted
    if request.method == 'POST':

        # Plug in the data into a dictionary object 
        #  - data from the input form
        #  - text data must be converted to lowercase
        data = {
        "Inputs": {
                "input1": 
                [
                    {
                            'Pos': "",   
                            'School': "",   
                            'Player': "",   
                            'Ht': "",   
                            'Wt': "1",   
                            '40yd': "1",   
                            'Vertical': "1",   
                            'Bench': "1",   
                            'Broad Jump': "1",   
                            '3Cone': "1",   
                            'Shuttle': "1",   
                            'DraftedPickYear': "",   
                            'Drafted': "",   
                    }
                ],
            },
            "GlobalParameters":  {
            }
        }

        body = str.encode(json.dumps(data))
    
        req = urllib.request.Request(fball_url, body, F_HEADERS)

        # Send this request to the AML service and render the results on page
        try:
            # response = requests.post(URL, headers=HEADERS, data=body)
            response = urllib.request.urlopen(req)
            print(response)
            respdata = response.read()
            result = json.loads(str(respdata, 'utf-8'))
            result = do_something_pretty(result)
            # result = json.dumps(result, indent=4, sort_keys=True)
            return render_template(
                'fballResult.html',
                title="This is the result from AzureML running our Football Draft Prediction:",
                result=result)

        # An HTTP error
        except urllib.error.HTTPError as err:
            result="The request failed with status code: " + str(err.code)
            return render_template(
                'fballResult.html',
                title='There was an error',
                result=result)
        print(err)

    return render_template(
        'football.html',
        form = form,
        title = 'Football Draft Predictions',
        year=datetime.now().year,
        message = 'Will you be drafted?'
    )

def do_something_pretty(jsondata):
    """We want to process the AML json result to be more human readable and understandable"""
    import itertools # for flattening a list of tuples below

    # We only want the first array from the array of arrays under "Value" 
    # - it's cluster assignment and distances from all centroid centers from k-means model
    prediction = jsondata["Results"]["output1"][0]['Scored Labels']
    chance = jsondata["Results"]["output1"][0]['Scored Probabilities']
    #valuelen = len(value)
    print(prediction)
    print(chance)
    # Convert values (a list) to a list of tuples [(cluster#,distance),...]
    # valuetuple = list(zip(range(valuelen-1), value[1:(valuelen)]))
    # Convert the list of tuples to one long list (flatten it)
    # valuelist = list(itertools.chain(*valuetuple))

    # Convert to a tuple for the list
    # data = tuple(list(value[0]) + valuelist)

    # Build a placeholder for the cluster#,distance values
    #repstr = '<tr><td>%d</td><td>%s</td></tr>' * (valuelen-1)
    # print(repstr)
    output=f'For the provided information our algorithm would calculate a draft probability of: {chance}'
    # Build the entire html table for the results data representation
    #tablestr = 'Cluster assignment: %s<br><br><table border="1"><tr><th>Cluster</th><th>Distance From Center</th></tr>'+ repstr + "</table>"
    #return tablestr % data
    return output

