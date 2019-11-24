"""
Found online @ 
https://stackoverflow.com/questions/27907633/multiple-json-objects-in-one-file-extract-by-python
"""
from json import JSONDecoder, JSONDecodeError
import re

NOT_WHITESPACE = re.compile(r'[^\s]')

def decode_stacked(document, pos = 0, decoder = JSONDecoder()):
    """Decodes a stacked file.
    
    Arguments:
        document {os.path()} -- path object to document file
    
    Keyword Arguments:
        pos {int} -- where to start in the document (default: {0})
        decoder {decoder} -- a decoder for the document type (default: {JSONDecoder()})
    
    Raises:
        Exception: something went wrong
    
    Yields:
        string -- a singular json string
    """
    while True:
        match = NOT_WHITESPACE.search(document, pos)
        if not match:
            return
        pos = match.start()

        try:
            obj, pos = decoder.raw_decode(document, pos)
        except JSONDecodeError:
            raise Exception('Something went wrong.')
        yield obj