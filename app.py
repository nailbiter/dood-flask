"""===============================================================================

        FILE: app.py

       USAGE: (not intended to be directly executed)

 DESCRIPTION: 

     OPTIONS: ---
REQUIREMENTS: ---
        BUGS: ---
       NOTES: ---
      AUTHOR: Alex Leontiev (alozz1991@gmail.com)
ORGANIZATION: 
     VERSION: ---
     CREATED: 2021-12-21T13:58:15.870367
    REVISION: ---

==============================================================================="""
from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/',methods=["POST"])
def hello_world():
    print(request.data,flush=True)
    obj = json.loads(request.data.decode())
    print(obj.keys())
    return json.dumps(obj)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
