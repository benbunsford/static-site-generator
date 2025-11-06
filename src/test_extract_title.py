import unittest

from extract_title import extract_title


class TestExtractTitle(unittest.TestCase):

    def test_success(self):
        md = '''# This is a valid heading with some extra whitespace.        

## An irrelevant heading.

With a paragraph too.

### Another irrelevant heading.

'''
        self.assertEqual("This is a valid heading with some extra whitespace.", extract_title(md))

    def test_no_heading(self):
        md = '''
## An irrelevant heading.

With a paragraph too.

### Another irrelevant heading.

'''
        with self.assertRaises(Exception):
            extract_title(md)

    def test_wrong_heading(self):
        md = '''
This is an invalid heading with some extra whitespace.        

#This heading is in the wrong place.

## An irrelevant heading.

With a paragraph too.

### Another irrelevant heading.

'''
        with self.assertRaises(Exception):
            extract_title(md)

    def test_blank_first_line(self):
        md = '''

#This heading is in the wrong place.

## An irrelevant heading.

With a paragraph too.

### Another irrelevant heading.

'''
        with self.assertRaises(Exception):
            extract_title(md)

if __name__ == 'main':
    unittest.main()
