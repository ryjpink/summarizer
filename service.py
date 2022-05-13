#
# Author: Ya-Juan Ruan
# Date: 5/13/2022
#
# Quick solution to the following assignment:
#   > Accept a POST request to the route "/test", which accepts one argument "string_to_cut"
#   > Return a JSON object with the key "return_string" and a string containing every third letter from the original string
#   > (e.g.) If you POST {"string_to_cut": "iamyourlyftdriver"}, it will return: {"return_string": "muydv"}.
#
# Note: To try it out, start a local server and make a request:
# 1. Bring up the server from terminal 1:
#    $ python ./service.py
# 2. Invoke the REST API from terminal 2:
#    $ curl -X POST http://127.0.0.1:5000/test --data '{"string_to_cut": "iamyourlyftdriver"}' -H 'Content-Type: application/json'
#

from flask import Flask, jsonify, request, Response

app = Flask(__name__)

def cut_string(s: str, k: int = 3) -> str:
    '''
    Summarizes a string by keeping only every k'th letter.
    Returns the resulting string.
    '''
    return "".join([s[i] for i in range(k - 1, len(s), k)])

@app.route('/test', methods = ['POST'])
def summarize_text():
    string_to_cut = request.json.get("string_to_cut")
    if string_to_cut is None:
        return Response(
            "Bad request: Required parameter string_to_cut missing",
            status=400)
    skipLength = request.args.get('skipLength', default=3, type=int)
    return_string = cut_string(string_to_cut, skipLength)
    return jsonify({'return_string': return_string})

if __name__ == '__main__':
    app.run(debug = True)