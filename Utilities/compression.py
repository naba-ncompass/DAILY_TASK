import gzip
import json
from flask import Response


def make_compress(data):
    byte_data = json.dumps(data, default=str).encode('utf-8')
    compressed_data = gzip.compress(byte_data, compresslevel=9)
    response = Response(compressed_data, content_type="application/json")
    response.content_encoding = 'gzip'
    return response