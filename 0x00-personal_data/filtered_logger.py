#!/usr/bin/env python3
"""`filtered_logger.py` defines a method `filter_datum`
which obfuscates specific fields from an input string."""


from typing import List


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """obfuscate specified fields from input string."""
    out_str = ""
    messages = message.split(separator)
    for msg in messages:
        if not msg:
            continue
        field, val = msg.split("=")
        if field not in fields:
            out_str += "{field}={val};".format(field=field, val=val)
            continue
        out_str += "{field}={val};".format(field=field, val=redaction)
    return out_str
