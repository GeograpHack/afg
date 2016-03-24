import functools
import os
import glob

from flask import g
import psycopg2

import blokskenom.database.geo as geo
import blokskenom.database.dao as dao

def inject_dao(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(g.dao, *args, **kwargs)

    return wrapper
