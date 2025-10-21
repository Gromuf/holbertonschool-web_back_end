#!/usr/bin/env python3
"""filtered_logger.py"""

import re
from typing import List
import logging

PII_FIELDS = (
    "name",
    "email",
    "phone",
    "ssn",
    "password",
)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Filters values in log records"""
        return filter_datum(
            self.fields,
            self.REDACTION,
            super().format(record),
            self.SEPARATOR
        )


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Returns the log message obfuscated"""
    pattern = f"({'|'.join(fields)})=.*?{separator}"
    return re.sub(
        pattern, lambda m: f"{m.group(1)}={redaction}{separator}", message)


def get_logger() -> logging.Logger:
    """Creates and returns a logger"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    sh = logging.StreamHandler()
    sh.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(sh)
    return logger
