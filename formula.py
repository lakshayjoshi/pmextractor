import json
 
# Load the Postman collection JSON
with open('your-collection.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
 
# Iterate through each request and extract the URLs
endpoints = []
for item in data['item']:
    if 'request' in item and 'url' in item['request']:
        endpoints.append(item['request']['url']['raw'])
 
# Print the extracted endpoints
for endpoint in endpoints:
    print(endpoint)
