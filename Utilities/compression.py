import gzip
import json

def create_compression(data):
    compressed_data = gzip.compress(
        json.dumps(data).encode('utf8'),
    compresslevel=9)
    return compressed_data
