class Road:
    def __init__(self, id, geom):
        self.id = id
        self.geom = geom

    @property
    def __geo_interface__(self):
        return {
            "geometry": self.geom.__geo_interface__,
            "type": "Feature",
            "properties": {
                "id": self.id
            }
        }

