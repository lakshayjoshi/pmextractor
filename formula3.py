import json
 
def extract_urls(swagger_file):
    with open(swagger_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    paths = data.get("paths", {}).keys()
    print("Extracted API URLs:")
    for path in paths:
        print(path)
 
# Replace 'swagger.json' with the actual file name
swagger_file = "swagger.json"
extract_urls(swagger_file)
