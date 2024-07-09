import json
from shapely.geometry import Point, mapping
from datetime import datetime

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Point):
            return mapping(obj)
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)