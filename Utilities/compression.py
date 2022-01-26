from flask import make_response, json ,Response
import gzip

def make_compress(data):
    byte_data = json.dumps(data, indent=4, sort_keys=True, default=str).encode('utf-8')
    compressed_data = gzip.compress(byte_data, compresslevel=9)
    response = Response(compressed_data,
    content_type="application/json"
    )
    response.content_encoding = 'gzip'
    return response

