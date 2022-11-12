import sys
import os
import requests
import json
import webbrowser

usage_string = "USAGE: {} [--delete-non-original] -a=API_KEY FILENAME".format(sys.argv[0])

#Process arguments
if len(sys.argv) < 3: #Sanity check to see if we have enough arguments, should at a bare minimum have an API key and a filename
    sys.exit("ERROR: Expected at least two arguments, got {}.\n{}".format(len(sys.argv)-1, usage_string))

no_original = False
api_key = None
i = 1
while i < len(sys.argv):
    if sys.argv[i] == "--delete-non-original":
        no_original = True
        i += 1
    elif sys.argv[i][:3] == "-a=":
        api_key = sys.argv[i][3:]
        i += 1
    else:
        break
filename = " ".join(sys.argv[i:])

#Check if arguments make sense
if not os.path.isfile(filename):
    sys.exit("ERROR: {} is not a file.\n{}".format(filename, usage_string))

if not api_key:
    sys.exit("ERROR: No API key passed.\n{}".format(usage_string))

#Handle the duplicate filtered screenshot if necessary
if no_original:
    os.remove(filename)
    
    #Get the filename of the non-filtered screenshot
    i = filename.rfind(".")
    if i == -1:
        i = len(filename)
    orig_filename = "{} original{}".format(filename[:i], filename[i:])
    
    if not os.path.isfile(orig_filename): #New file means new sanity checks
        sys.exit("ERROR: {} is not a file.\n{}".format(filename, usage_string))
    
    os.rename(orig_filename, filename) #Rename the file to read the correct timestamp
    

#Prepare for sending the image
url = "https://api.nightlight.gg/v1/upload"

image = open(filename, 'rb')
headers = {"Authorization": "Bearer {}".format(api_key)}
payload = {"file": image}

#Send the image
response = requests.post(url, files=payload, headers=headers)

image.close() #Don't need the image anymore

#Parse the response
if response.status_code == 200:
    try:
        formatted_response = json.loads(response.text)
    except JSONDecodeError:
        sys.exit("ERROR: Image was successfully uploaded but an invalid response was recieved, check your matches.\nResponse: {}".format(response.text))
    match_url = formatted_response["data"]["url"]
else:
    try:
        formatted_response = json.loads(response.text)
    except JSONDecodeError:
        sys.exit("ERROR: Something went wrong when uploading the image and an invalid response was recieved.\nResponse: {}".format(response.text))
    sys.exit("ERROR: Something went wrong when uploading the image.\nError message from server: {}".format(formatted_response["error"]["message"]))

#Open the match
webbrowser.open(match_url, new=0, autoraise=True)
