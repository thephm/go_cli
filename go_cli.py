import requests
from argparse import ArgumentParser
import json

import go_api
import go_train
import go_bus

# Parse the command line arguments
def get_arguments():

    parser = ArgumentParser()

    parser.add_argument("-k", "--key", dest="key", default="",
                        help="Your API key")
    
    parser.add_argument("-f", "--keyFile", dest="key_file", default="",
                        help="The file containing your API key")

    parser.add_argument("-s", "--stop", dest="stop", default="",
                        help="The stop you're interested in")
    
    parser.add_argument("-d", "--direction", dest="direction", default="",
                        help="The direction you want to go")
    
    parser.add_argument("-v", "--vehicle", dest="vehicle", default="",
                        help="The vehicle you're interested in")

    parser.add_argument("-c", "--config", action="store_true", default=False,
                        help="Dump the configuration")
    
    args = parser.parse_args()

    return args

args = get_arguments()
key = args.key

if args.config:
    print(go_train.Lines)
    print(go_bus.Stops)

if args.stop:
    stop_code = args.stop

    api_url = go_api.GO_API_NEXT_SERVICE + str(stop_code) + go_api.KEY_FIELD + str(key)
    response = requests.get(api_url)

    # if request was successful
    if response.status_code == go_api.OK:
        # parse JSON response
        data = response.json()
        # do something with the data
        print(data)
    else:
        print("Failed to retrieve data. Status code:", response.status_code)
