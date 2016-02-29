#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Readers for the pke module. """

from xml.etree import ElementTree

class MinimalCoreNLPParser:
    """ Minimal CoreNLP XML Parser in Python. """
    def __init__(self, path):
        self.sentences = []
        tree = ElementTree.ElementTree(file=path)
        for sentence in tree.iterfind('./document/sentences/sentence'):
            self.sentences.append({
              "words" : [u.text for u in sentence.iterfind("tokens/token/word")],
              "lemmas" : [u.text for u in sentence.iterfind("tokens/token/lemma")],
              "POS" : [u.text for u in sentence.iterfind("tokens/token/POS")]
            })