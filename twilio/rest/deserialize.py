import datetime
from decimal import Decimal, BasicContext
from email.utils import parsedate
import pytz


def iso8601_datetime(s):
    """
    Parses an ISO 8601 date string and returns a UTC datetime object,
    or the string if parsing failed.
    :param s: ISO 8601-formatted string date
    :return: datetime or str
    """
    format = "%Y-%m-%dT%H:%M:%SZ"
    try:
        return datetime.datetime.strptime(s, format).replace(tzinfo=pytz.utc)
    except ValueError:
        return s


def rfc2822_datetime(s):
    """
    Parses an RFC 2822 date string and returns a UTC datetime object,
    or the string if parsing failed.
    :param s: RFC 2822-formatted string date
    :return: datetime or str
    """
    date_tuple = parsedate(s)
    if date_tuple is None:
        return None
    return datetime.datetime(*date_tuple[:6]).replace(tzinfo=pytz.utc)


def decimal(d):
    """
    Parses a decimal string into a Decimal
    :param d: decimal string
    :return: Decimal
    """
    if not d:
        return d
    return Decimal(d, BasicContext)


def integer(i):
    """
    Parses an integer string into an int
    :param i: integer string
    :return: int
    """
    try:
        return int(i)
    except (TypeError, ValueError):
        return i
