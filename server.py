import json

ok_response_obj = [{ 'verdict': 'Accepted', 'time': 0, 'memory': 250 }] * 20
ok_response = bytes( json.dumps( ok_response_obj ), "utf-8" )

def app( environ, start_response ):
    status = '200 OK'
    response_headers = [
        ( 'Content-type', 'text/plain' ),
        ( 'Content-Length', str( len( ok_response ) ) )
    ]
    start_response( status, response_headers )
    return iter( [ok_response] )
