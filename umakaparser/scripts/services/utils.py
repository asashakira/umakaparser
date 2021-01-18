# coding:utf-8

from rdflib.plugins.parsers.ntriples import r_literal
from rdflib import Literal, URIRef
from mimetypes import guess_type
import os
import i18n
import six


IGNORE_CLASSES = set([
    URIRef(c)
    for c in [
        "http://www.w3.org/2002/07/owl#Class",
        "http://www.w3.org/2002/07/owl#ObjectProperty",
        "http://www.w3.org/2002/07/owl#Ontology",
        "http://www.w3.org/2002/07/owl#Thing",
        "http://www.w3.org/2002/07/owl#NamedIndividual"
    ]])


def parse_literal(literal):
    return Literal(*[v if v else None for v in r_literal.match(literal).groups()])


def get_type(file_path):
    mimetype, _ = guess_type(file_path)
    if mimetype:
        return mimetype.split('/')[1]

    _, ext = os.path.splitext(file_path)
    if ext == '.ttl':
        return 'turtle'
    elif ext in ('.n3', '.nt'):
        return 'n3'


def i18n_t(key, **kwargs):
    return i18n.t(key, **kwargs).encode('utf-8') if six.PY2 else i18n.t(key, **kwargs)
