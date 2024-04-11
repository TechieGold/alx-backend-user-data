#!/usr/bin/env python3
"""
This modules contains functions that:
     that returns the log message obfuscated:
"""
import re
from typing import List, Tuple


def filter_datum(fields: List, redaction: str,
                 message: str, separator: str) -> str:
    """ Returns the log message obfuscated."""
    for field in fields:
        message = message = re.sub(
            fr'(?<={field}\=)(.*?)(?={separator})', redaction, message)
    return message
