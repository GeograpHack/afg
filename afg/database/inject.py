import functools
import os
import glob
import psycopg2
import afg.database.geo as geo
import afg.database.dao as dao

def inject_dao(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        con = psycopg2.connect('dbname=afg user=afg password=afg host=127.0.0.1')
        geo.register_extensions(con)
        d = dao.Dao(con)
        query_pattern = os.path.join(os.path.dirname(__file__), 'queries/*.yaml')
        for path in glob.glob(query_pattern):
            d.load(path)
        result = func(d, *args, **kwargs)
        con.close()
        return result

    return wrapper
