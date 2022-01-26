import gzip
import json

def create_compression(data):
    compressed_data = gzip.compress(
        json.dumps(data,default=str).encode('utf8'),
    compresslevel=9)
    return compressed_data
