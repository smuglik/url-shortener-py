from dataclasses import dataclass
from datetime import datetime


@dataclass
class ShortUrl:
    """Short url entity"""

    original_url: str
    short_url: str
    created_at: datetime
