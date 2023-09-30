import sys
sys.path.append('sherlock/sherlock')
import sherlock

def hello_world(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """

    request_json = request.get_json()
    if 'username' in request_json:
        sherlock_json = sherlock.req_json(request_json['username'])
        return sherlock_json
    else:
        return 'Invalid username', 400
