#Dependencies
import requests
import json

# Set up device dictionary for later use
devices = {}

# Import file for reading
f = open('ip.txt')

#read devices into variable 
for line in f :
    device = line.split()

#Clean up and close file
f.close()

#obtain the token for each device
for i in range(len(device)) :
    url = "https://" + device[i] + ":55443/api/v1/auth/token-services"

    payload = ""
    headers = {
        'Accept': "application/json",
        'Authorization': "Basic Y2lzY286Y2lzY28=",
        'cache-control': "no-cache",
        'Postman-Token': "b35758cc-06e8-4c6a-a2c4-92690b61e2f2"
        }

    response = requests.request("POST", url, data=payload, headers=headers, verify = False)

    # Convert json text to a list
    token = json.loads(response.text)
    
    # Append ip address and token to device dictionary for later use
    devices.update ( {'IP Address' : device[i], 'token-id' : token['token-id']} )
    print (devices)