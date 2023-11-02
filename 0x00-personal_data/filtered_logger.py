#!/usr/bin/env python3
"""`filtered_logger.py` defines a method `filter_datum`
which obfuscates specific fields from an input string."""


import re
from typing import List


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """obfuscate specified fields from input string."""
    pattern = re.compile(
        r"(?P<field>{})=(?P<value>[^{}]+)".format("|".join(fields), separator))
    out = re.sub(
        pattern, lambda m: m.group("field") + "=" + redaction, message)
    return out
