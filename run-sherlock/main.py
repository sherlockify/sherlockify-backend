import sys
sys.path.append('sherlock/sherlock')
import sherlock

def endpoint(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',  # Allow your function to be called from any domain
            'Access-Control-Allow-Methods': '*',  # Allow all HTTP methods
            'Access-Control-Allow-Headers': 'Content-Type', 
            'Access-Control-Max-Age': '3600',
        }
        return ('', 204, headers)

    headers = {
        'Access-Control-Allow-Origin': '*',
    }

    request_json = request.get_json()
    if 'username' in request_json:
        sherlock_json = sherlock.req_json(request_json['username'])
        return sherlock_json, 200, headers
    else:
        return 'Invalid username', 400, headers
