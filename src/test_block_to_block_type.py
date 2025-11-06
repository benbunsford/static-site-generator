import unittest

from block_to_block_type import BlockType, block_to_block_type


class TestBlockToBlockType(unittest.TestCase):
    def test_paragraph(self):
        md = '''This is a regular block.
With a second line.'''
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_heading(self):
        md = '''# This is a heading block.'''
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_heading_two_lines(self):
        md = '''# This is a heading block.
With a second line.'''
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.PARAGRAPH)


    def test_heading_more(self):
        md = '''### This is a heading block.'''
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_heading_too_many(self):
        md = '''######### This is a heading block.'''
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_heading_no_space(self):
        md = '''#This is a heading block.'''
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_code(self):
        md = '''```This is a code block.```'''
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.CODE)

    def test_code_multiline(self):
        md = '''```
This is a code block.
With multiple lines.
```'''
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.CODE)

    def test_quote(self):
        md = '''> This is a quote block.'''
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_quote_blank_middle(self):
        md = '''> This is a quote block.
>
> -- Big Albert
'''
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_quote_multiline_no_space(self):
        md = '''>This is a quote block.
>With a second line.'''
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.PARAGRAPH)
        
    def test_quote_partial(self):
        md = '''>This is a quote block.
With a second line.'''
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_unordered_list(self):
        md = '''- This is an unordered list.'''
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_unordered_list_multiple(self):
        md = '''- This is an unordered list.
- With a second item.'''
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_unordered_partial(self):
        md = '''- This is an unordered list.
With a second item.'''
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_ordered_list(self):
        md = '''1. This is an ordered list.'''
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_ordered_list_multiple(self):
        md = '''1. This is an ordered list.
2. With a second item.'''
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_ordered_list_partial(self):
        md = '''1. This is an ordered list.
With a second item.'''
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_ordered_list_no_space(self):
        md = '''1.This is an ordered list.
2. With a second item.'''
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def ordered_wrong_numbers(self):
        md = '''1. This is an ordered list.
3. With an out of sequence number.'''
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

if __name__ is 'main':
    unittest.main()
