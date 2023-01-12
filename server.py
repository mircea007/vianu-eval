import json

ok_response_obj = {
    'points': 100,
    'verdict': 'Accepted',
    'time': 0,
    'memory': 250,
    'tests': [{ 'verdict': 'Accepted', 'points': 5, 'time': 0, 'memory': 250 }] * 20
}
ok_response = bytes( json.dumps( ok_response_obj ), "utf-8" )

def app( environ, start_response ):
    # https://stackoverflow.com/questions/530526/accessing-post-data-from-wsgi
    body= b"{'source':'#include<stdio.h>\nint main(){\n  return 0;\n}'}"
    try:
        length= int( environ.get('CONTENT_LENGTH', '0') )
    except ValueError:
        length= 0
    if length!=0:
        body = environ['wsgi.input'].read(length)

    req_json = json.loads( body )
    source = req_json['source']

    print( 'Got source for evaluation:\n' + source )

    status = '200 OK'
    response_headers = [
        ( 'Content-type', 'text/plain' ),
        ( 'Content-Length', str( len( ok_response ) ) )
    ]
    start_response( status, response_headers )
    return iter( [ok_response] )
