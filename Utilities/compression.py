import gzip
import json
from flask import Response

def compress_json(data):
    
    #default is a function applied to objects that aren't serializable. In this case it's str,
    
    byte_data = json.dumps(data, default=str).encode('utf-8')
    compressed_result = gzip.compress(byte_data, compresslevel=9)
    response = Response(compressed_result,
    content_type="application/json"
    )
    response.content_encoding = 'gzip'
    return response
    

    