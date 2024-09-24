# Loads the GO-GTFS.zip file and creates `.py` files for stops

from argparse import ArgumentParser
import requests
import zipfile
import io
import pandas as pd
import json
import os

# parse the command line arguments
def get_arguments():

    parser = ArgumentParser()

    parser.add_argument("-f", "--folder", dest="folder", default="config",
                        help="where to put the output file, default is `config`")

    parser.add_argument("-w", "--which", dest="which", default="stops",
                        help="Which data to convert, default is `stops` for `stops.txt`")
    
    parser.add_argument("-u", "--url", dest="url", default="https://assets.metrolinx.com/raw/upload/Documents/Metrolinx/Open%20Data/GO-GTFS.zip",
                        help="Source for the GTFS.zip file")
    
    args = parser.parse_args()

    return args

args = get_arguments()

# download the ZIP file from the URL
response = requests.get(args.url)

# unzip the contents
with zipfile.ZipFile(io.BytesIO(response.content)) as the_zip:
    # extract all contents
    the_zip.extractall("go_gtfs_data")

# load the CSV file into a Pandas DataFrame
csv_file_path = "go_gtfs_data/" + args.which + ".txt" 
trips_df = pd.read_csv(csv_file_path)

# convert DataFrame to JSON
trips_json = trips_df.to_json(orient='records')

# save the JSON data to a file
output_filename = os.path.join(args.folder, args.which + ".json")
with open(output_filename, "w") as json_file:
    json.dump(json.loads(trips_json), json_file, indent=4)

print(args.which + ".csv has been converted to " + args.which + ".json")
