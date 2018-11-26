import sys
import re
import os
import ssl
import json
import urllib.parse
import urllib.request


if len(sys.argv) != 3:
    print(f"Usage: python3 {sys.argv[0]} endpoint_url sparql_directory")
    exit()

sparql_endpoint = sys.argv[1]
sparql_dir = sys.argv[2]
files = [f for f in os.listdir(sparql_dir) if re.match(r'.*\.sparql', f)]
for sparql_file in files:
    with open(sparql_dir + "/" + sparql_file, "r") as f:
        query = f.read()
        query = urllib.parse.quote_plus(query)
        context = ssl._create_unverified_context()
        request = urllib.request.Request(sparql_endpoint + "?query=" + query)
        request.add_header("Accept", "application/sparql-results+json")
        result = urllib.request.urlopen(request, context=context).read()
        obj = json.loads(result)
        with open(sparql_dir + "/" + sparql_file + ".out.json", "w") as out:
            out.write(json.dumps(obj, indent=4, sort_keys=True))
