#!/usr/bin/env python3
"""`filtered_logger.py` defines a method `filter_datum`
which obfuscates specific fields from an input string."""


import re
from typing import List
import logging


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        filtered_msg = filter_datum(
            self.fields, self.REDACTION, record.getMessage(), self.SEPARATOR)
        record.msg = filtered_msg
        return super().format(record)


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """obfuscate specified fields from input string."""
    pattern = re.compile(
        r"(?P<field>{})=(?P<value>[^{}]+)".format("|".join(fields), separator)
    )
    out = re.sub(
        pattern, lambda m: m.group("field") + "=" + redaction, message)
    return out


if __name__ == "__main__":
    message = "name=Bob;email=bob@dylan.com;ssn=000-123-0000;\
    password=bobby2019;"
    log_record = logging.LogRecord(
        "my_logger", logging.INFO, None, None, message, None, None)
    formatter = RedactingFormatter(fields=("email", "ssn", "password"))
    print(formatter.format(log_record))
