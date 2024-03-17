import pandas as pd
import requests
import json

#read provided files for countries and the airport 
countrydf = pd.read_csv('countries.csv')
airportdf = pd.read_csv('airports.csv')
#filter countries which has airport
countries_with_airports = countrydf[countrydf['code'].isin(airportdf['iso_country'])]
# Filter countries that have at least one airport
countries_with_no_airports = countrydf[~countrydf['code'].isin(airportdf['iso_country'])]

#function to get next gene data from broker platform ( check for json error)
def get_country_data(iso_code):
    url = f'http://code001.ecsbdp.com/countries/{iso_code}'
    response = requests.get(url)
    try:
        response_data = response.json()
        return response_data
    except json.JSONDecodeError:
        return {'error': 'Invalid JSON response'}

# get country data from broker platform and check which country are missing 
country_on_platform = []
missing_countries = []
for iso_code in countries_with_airports['code']:
    country_info = get_country_data(iso_code)
    if 'error' in country_info:
        missing_countries.append(iso_code)
    else:
        country_on_platform.append(country_info)

#now conver country data to data frame and dump it on json as requested in assignment
country_data = pd.DataFrame(country_on_platform)
country_data.to_json('country_data.json', orient='records', indent=4)

# now countries missing from the broker next gene platform
if missing_countries:
    print("Countries missing from the  platform- showing ISO code:", missing_countries)
else:
    print("Check json file for other country data")


#SOLUTION 2B - File Upload 

# provided Endpoint details
client_id = 'abc123'
host_address = 'code001.ecsbdp.com'
upload_path = f'/revenues?client={client_id}'

# File to upload # first create filein dir other wise geting error
file_data = open('revenues.txt', 'rb')  #open reveneues file 

# Construct URL end point to upload file
url = f'http://{host_address}{upload_path}'

# make post request to upload the empty file 
response = requests.post(url, files={'file': file_data})

# Check if the request was successful
if response.status_code == 200:
    print('Reveneu file uploaded successfully')
else:
    print(f'Error uploading revenues file')
