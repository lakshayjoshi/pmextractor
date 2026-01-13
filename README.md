# pmextractor
This is a simple python script to extract unique urls/endpoints from a postman collection. This caters to extensions of all kinds (e.g. '.json', '.postman', '.swagger'). This comes in handy for penetration testers while documenting their findings.

Just download v1.0 if you have a simple postman collection in json format and none of the urls belong to any folder. Replace 'your-collection.json' with your current file path (or filename if the script and collection are in the same folder) and run formula.py from your terminal.

Download v1.1 if you have one of multiple folders in your collection. This script skims through those folders to extract the urls. Replace 'your-collection.json' with your current file path (or filename if the script and collection are in the same folder) and run formula2.py from your terminal. Works with both '.json' and '.postman_collection'.

Download v1.2 if your file is a swagger file. Replace 'swagger.json' with your current file path (or filename if the script and collection are in the same folder) and run formula3.py from your terminal.
