import io
import logging
import os
import pathlib
import re

logging.basicConfig(level=logging.INFO)

__version__ = '1.0.0'

VERSION = tuple([int(v) for v in __version__.split('.')])

NEWLINE = '\n'
RE_KEY_VAL = '^\s*([\w.-]+)\s*=\s*(.*)?\s*$'

SRC_MUST_BE_IO_OR_STRING_ERROR = 'src must be IO or string'

class pyenvarException(Exception):
    pass

'''
parse given input into env dict
'''
def parse(src):
    content = ''
    envs = {}
    if isinstance(src, io.IOBase):
        content = src.read()
    else:
        content = src
    for c in content.splitlines():
        match = re.match(RE_KEY_VAL, c)
        if match:
            # if match, split with '='
            key_val_list = re.split('=', c)
            key = key_val_list[0]
            val = key_val_list[1] or ''

            # calculate variable len without last character
            end = len(val) - 1

            # determine if val uses single quote
            is_single_quoted = val.startswith("'") and val.endswith("'")
            # determine if val uses double quote
            is_double_quoted = val.startswith('"') and val.endswith('"')
            if is_single_quoted or is_double_quoted:
                # remove single quote or double quote with slicing
                val = val[1:end]
            else:
                # remove whitespace
                val = val.strip()
            envs[key] = val
    return envs

'''
load .env file and parse into environment variables
'''
def load(**kwargs):
    logging.info('load env.....')
    encoding = 'utf-8'
    cwd = pathlib.Path.cwd()
    dotenv_path = pathlib.Path.joinpath(cwd, '.env')
    if 'path' in kwargs:
        dotenv_path = kwargs.get('path')
    if 'encoding' in kwargs:
        encoding = kwargs.get('encoding')

    dotenv_content = open(dotenv_path, 'r', encoding=encoding)
    envs = parse(dotenv_content)
    
    for key, val in envs.items(): 
        if key not in os.environ.keys():
            os.environ[key] = val
        else:
            logging.info('key {0} already defined')
    dotenv_content.close()
    return envs