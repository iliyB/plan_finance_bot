from typing import Dict

from core.database import Base
from sqlalchemy import inspect


def object_to_dict(obj: Base) -> Dict:
    return {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs}
