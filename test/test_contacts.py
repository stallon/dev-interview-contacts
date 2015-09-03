__author__ = '홍성봉'

import unittest
from main.contacts import Contacts
from main.parser import CsvParser
from main.parser import JsonParser


class TestContacts(unittest.TestCase):

    def setUp(self):
        self.contacts = Contacts()

    def tearDown(self):
        self.contacts.clear()

    def testCsvFormat(self):
        self.contacts.load('row-3-dup.csv', CsvParser())
        result = self.contacts.findByName('홍길동')

        self.assertEqual(len(result), 2)
        self.assertEqual('010-1111-2222', result[0])
        self.assertEqual('010-1234-5678', result[1])

    def testJsonFormat(self):
        self.contacts.load('row-3-dup.json', JsonParser())
        result = self.contacts.findByName('홍길동')

        self.assertEqual(len(result), 2)
        self.assertEqual('010-1111-2222', result[0])
        self.assertEqual('010-1234-5678', result[1])


if __name__ == '__main__':
    unittest.main()

