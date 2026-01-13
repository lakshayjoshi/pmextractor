import json
 
def extract_endpoints(items, endpoints):
    for item in items:
        if 'request' in item and 'url' in item['request']:
            endpoints.append(item['request']['url']['raw'])
        if 'item' in item:  # Check for nested folders
            extract_endpoints(item['item'], endpoints)
 
# Load the Postman collection JSON
with open('your-collection.postman_collection', 'r', encoding='utf-8') as file:
    data = json.load(file)
 
endpoints = []
extract_endpoints(data['item'], endpoints)
 
# Print the extracted endpoints
for endpoint in endpoints:
    print(endpoint)
