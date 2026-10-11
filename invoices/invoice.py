from dataclasses import dataclass, field
from datetime import date


@dataclass
class Invoice:
    number: str
    customer: str
    issued: date
    lines: list = field(default_factory=list)
    paid: bool = False
