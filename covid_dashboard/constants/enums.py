import enum

from ib_common.constants import BaseEnumClass


class DistrictZones(BaseEnumClass, enum.Enum):
    RED = "RED"
    GREEN = "GREEN"
    ORANGE = "ORANGE"

class DateFormat(BaseEnumClass, enum.Enum):
    DATEFORMAT = "%d/%m/%Y"
