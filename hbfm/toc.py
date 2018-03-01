# coding: utf-8

try:
    import urllib2
except ImportError:
    import urllib.parse as urllib2
import re


def slugify(value, separator):
    """ Slugify a string, to make it URL friendly. """
    value = re.sub(r"^[0-9\.]+", "", value)
    value = re.sub(r"^-", "", value)
    value = re.sub(r"^ +", "", value)
    value = value.encode("utf-8", "ignore")
    value = urllib2.quote(value)
    return re.sub('[%s\s]+' % separator, separator, value)
