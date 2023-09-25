#!/usr/bin/python3

import sys

def safe_function(fct, *args):
    try:
        result = fct(*args)
        return (resul)t
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return (None)
