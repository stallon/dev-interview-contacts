'''
This is an example class for a python unittest
'''

__author__ = '홍성봉'

import unittest

class Contacts:

    def __init__(self):
        self.contact_map = dict()


    def clear(self):
        self.contact_map.clear()