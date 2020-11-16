from pprint import pprint

class poidepok:

    def getZoneVolume(req):
        return """
            select *, st_asgeojson(geom) as geomjson from data.poi
        """
