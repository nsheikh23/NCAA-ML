import urllib.request
import json

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

url = 'https://ussouthcentral.services.azureml.net/workspaces/1bd82c355c1447d591afec4715a4b045/services/27f2c06eb9ad492db435e9999a272af4/execute?api-version=2.0&format=swagger'
api_key = 'Jur+v2F7MlT70r85jA7F3Ntt48vBoSkZGlg67g7VihkF+/jNwxI8mSOpqY1ADz4nz5+HUMLLB6LJ2gaDGalJwg==' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))