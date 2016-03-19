import binascii
import codecs
from shapely.geometry import Point, Polygon, LineString
import shapely.wkb
import psycopg2
import psycopg2.extensions as pgext

def adapt_wkt(value):
    return pgext.AsIs("ST_GeomFromText('%s')" % value.wkt)

def cast_wkb(value, cur):
    if value is None:
        return None

    return shapely.wkb.loads(codecs.decode(value, 'hex_codec'))

def register_extensions(con):
    pgext.register_adapter(Polygon, adapt_wkt)
    pgext.register_adapter(Point, adapt_wkt)
    pgext.register_adapter(LineString, adapt_wkt)

    with con.cursor() as c:
        c.execute('select null::point, null::polygon, null::geometry')
        point_oid, poly_oid = c.description[0][1], c.description[1][1]
        geom_oid = c.description[2][1]

    point = pgext.new_type((point_oid,), 'POINT', cast_wkb)
    polygon = pgext.new_type((poly_oid,), 'POLYGON', cast_wkb)
    geom = pgext.new_type((geom_oid,), 'GEOMETRY', cast_wkb)
    pgext.register_type(point)
    pgext.register_type(polygon)
    pgext.register_type(geom)
