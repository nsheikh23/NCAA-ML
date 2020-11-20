import urllib.request
import json
data = {
        "Inputs": {
                "input1":
                [
                    {
                            'player': "",
                            'position': "",
                            'team': "",
                            'gp': "1",
                            'mpg': "1",
                            'fgm': "1",
                            'fga': "1",
                            'fg_pct': "1",
                            'threepm': "1",
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
url = 'https://ussouthcentral.services.azureml.net/workspaces/0f1aebe5b0944e9c831c80acc2aa6ee7/services/4c90f9399d64471bb0dc293c2c00b5e0/execute?api-version=2.0&format=swagger'
api_key = 'J/YazlXkBmLjs+GGrAst0pfD6hxd3l5FQCQ6I7g4pMs/3Dv898Xf/Ra6qjm3sQ72utOXCyC3enYO/1rT1cQytg=='
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