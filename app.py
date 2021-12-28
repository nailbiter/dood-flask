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
import subprocess
from jinja2 import Template

app = Flask(__name__)


@app.route('/', methods=["POST"])
def hello_world():
    obj = json.loads(request.data.decode())
    res = {}
    res["error_code"], res["output"] = subprocess.getstatusoutput(Template("""
    docker run {{image}} {{cmd}}
    """).render({
        **obj
    }).strip())
    return json.dumps(res)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
