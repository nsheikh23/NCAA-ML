"""
Routes and views for the flask application.
"""

from flask import render_template, request
from FlaskAppAML import app
from FlaskAppAML.forms import SubmissionForm
# from FlaskAppAML import rdsconnection as db
from datetime import datetime
import json
import urllib.request
import os

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():

    return render_template("index.html", year=datetime.now().year)

# @app.route('/DB')
# def DB():
#     # Table name you want to view
#     table = 'nbadraft'

#     # Extracting all the data from PostgreSQL
#     # details = db.get_all(table)
#     # print(details)
    
#     table = "<table>\n"

#     # Creating the table's row data
#     for line in details:
#         print(line)
#         row = line.split(",")
#         table += "  <tr>\n"
#         for column in row:
#             table += "      <td>{0}</td>\n".format(column.strip())
#         table += "  </tr>\n"

#     table += "</table"
#         # var = detail
#         # row.append(var)
#     # result = pretty_table(row)
#     return render_template(
#         "DB.html",
#         year=datetime.now().year, 
#         result=table)
    
    

@app.route('/basketball', methods=['GET', 'POST'])
def basketball():
    bball_key = os.environ.get('API_KEY', "J/YazlXkBmLjs+GGrAst0pfD6hxd3l5FQCQ6I7g4pMs/3Dv898Xf/Ra6qjm3sQ72utOXCyC3enYO/1rT1cQytg==")
    bball_url = os.environ.get('URL', "https://ussouthcentral.services.azureml.net/workspaces/0f1aebe5b0944e9c831c80acc2aa6ee7/services/4c90f9399d64471bb0dc293c2c00b5e0/execute?api-version=2.0&format=swagger")
    
    B_HEADERS = {'Content-Type':'application/json', 'Authorization':('Bearer '+ bball_key)}

    form = SubmissionForm(request.form)
    
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
                            'player': "",
                            'position': form.position.data.upper(),
                            'team': "",
                            'gp': form.gp.data,
                            'mpg': "1",
                            'fgm': form.fgm.data,
                            'fga': "1",
                            'fg_pct': "1",
                            'threepm': form.three.data,
                            'threepa': "1",
                            'three_pct': "1",
                            'ftm': "1",
                            'fta': "1",
                            'ft_pct': "1",
                            'tov': "1",
                            'pf': "1",
                            'orb': "1",
                            'drb': "1",
                            'rpg': "1",
                            'apg': "1",
                            'spg': "1",
                            'bpg': "1",
                            'ppg': "1",
                            'pick': "1",
                            'conference': "",
                            'college': "",
                            'School': "",
                            'Country': "",
                            'State': "",
                            'Latitude': "1",
                            'Longitude': "1",
                            'Revenue_Men': "",
                            'Expenses_Men': "",
                    }
                ],
                },
            "GlobalParameters":  {
            }
        }
        body = str.encode(json.dumps(data))
    
        req = urllib.request.Request(bball_url, body, B_HEADERS)

        # Send this request to the AML service and render the results on page
        try:
            # response = requests.post(URL, headers=HEADERS, data=body)
            response = urllib.request.urlopen(req)
            #print(response)
            respdata = response.read()
            result = json.loads(str(respdata, 'utf-8'))
            result = bball_pretty(result)
            # result = json.dumps(result, indent=4, sort_keys=True)
            return render_template(
                'bballResult.html',
                title="This is the result from AzureML running our Basketball Conference Prediction:",
                year=datetime.now().year,
                result=result)

        # An HTTP error
        except urllib.error.HTTPError as err:
            result="The request failed with status code: " + str(err.code)
            return render_template(
                'bballResult.html',
                title='There was an error',
                year=datetime.now().year,
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
    fball_key = os.environ.get('API_KEY', "mjYhDRm7ZyrlHWvAE726VK30whTi+2zu4uxLfLRVCVcryfCXgtwFiFOlfXVmNfW0Gch3QmF1YSIAd9xXod5YtA==")
    fball_url = os.environ.get('URL', "https://ussouthcentral.services.azureml.net/workspaces/1bd82c355c1447d591afec4715a4b045/services/7a19aada667c40a1851c13ab20d7df38/execute?api-version=2.0&format=swagger")

    F_HEADERS = {'Content-Type':'application/json', 'Authorization':('Bearer '+ fball_key)}

    form = SubmissionForm(request.form)
    
    # Form has been submitted
    if request.method == 'POST':

        # Plug in the data into a dictionary object 
        #  - data from the input form
        data = {
        "Inputs": {
                "input1":
                [
                    {
                            'Position': form.position.data.upper(),   
                            'School': form.school.data,   
                            'Height': form.height.data,   
                            'Weight': form.weight.data,   
                            '40yd': "0",   
                            'Vertical': form.vert.data,   
                            'Bench': form.bench.data,   
                            'Broad Jump': form.broad.data,   
                            '3Cone': "0",   
                            'Shuttle': "0",   
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
            result = fball_pretty(result)
            # result = json.dumps(result, indent=4, sort_keys=True)
            return render_template(
                'fballResult.html',
                title="This is the result from AzureML running our Football Draft Prediction:",
                year=datetime.now().year,
                result=result)

        # An HTTP error
        except urllib.error.HTTPError as err:
            result="The request failed with status code: " + str(err.code)
            return render_template(
                'fballResult.html',
                title='There was an error',
                year=datetime.now().year,
                result=result)
        print(err)

    return render_template(
        'football.html',
        form = form,
        title = 'Football Draft Predictions',
        year=datetime.now().year,
        message = 'Will you be drafted?'
    )

def fball_pretty(jsondata):
    """We want to process the AML json result to be more human readable and understandable"""
    import itertools # for flattening a list of tuples below

    # We only want the first array from the array of arrays under "Value" 
    # - it's cluster assignment and distances from all centroid centers from k-means model
    # prediction = jsondata["Results"]["output1"][0]['Scored Labels']
    chance = jsondata["Results"]["output1"][0]['Scored Probabilities for Class "Y"']
    pct = round(float(chance) * 100,4)
    #valuelen = len(value)
    # print(prediction)
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
    fball=f'For the provided information our algorithm would calculate a draft probability of: {pct} %'
    # bball=f'For the provided information our algorithm would suggest going to conference: {prediction} %'
    # Build the entire html table for the results data representation
    #tablestr = 'Cluster assignment: %s<br><br><table border="1"><tr><th>Cluster</th><th>Distance From Center</th></tr>'+ repstr + "</table>"
    #return tablestr % data
    return fball

def bball_pretty(jsondata):
    """We want to process the AML json result to be more human readable and understandable"""
    import itertools # for flattening a list of tuples below

    # We only want the first array from the array of arrays under "Value" 
    # - it's cluster assignment and distances from all centroid centers from k-means model
    prediction = jsondata["Results"]["output1"][0]['Scored Labels']
    #valuelen = len(value)
    print(prediction)
    # Convert values (a list) to a list of tuples [(cluster#,distance),...]
    # valuetuple = list(zip(range(valuelen-1), value[1:(valuelen)]))
    # Convert the list of tuples to one long list (flatten it)
    # valuelist = list(itertools.chain(*valuetuple))

    # Convert to a tuple for the list
    # data = tuple(list(value[0]) + valuelist)

    # Build a placeholder for the cluster#,distance values
    #repstr = '<tr><td>%d</td><td>%s</td></tr>' * (valuelen-1)
    # print(repstr)
    bball=f'{prediction}'
    # Build the entire html table for the results data representation
    #tablestr = 'Cluster assignment: %s<br><br><table border="1"><tr><th>Cluster</th><th>Distance From Center</th></tr>'+ repstr + "</table>"
    #return tablestr % data
    return bball

