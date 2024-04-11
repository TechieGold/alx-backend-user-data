#!/usr/bin/env python3
"""
This modules contains functions that:
     that returns the log message obfuscated:
"""
from re import sub
import logging
from typing import List, Tuple


def filter_datum(fields: List, redaction: str,
                 message: str, separator: str) -> str:
    """ Returns the log message obfuscated."""
    for field in fields:
        message = sub(f'{field}=.+?{separator}',
                      f'{field}={redaction}{separator}', message)

    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Set the format of the record

        Return:
            The function overloaded to make a new log with all items
        """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)

        return (super(RedactingFormatter, self).format(record))
