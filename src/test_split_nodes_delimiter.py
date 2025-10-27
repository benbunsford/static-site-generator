import unittest

from textnode import TextNode, TextType
from split_nodes_delimiter import *

class TestTextNodeToLeafNode(unittest.TestCase):
    def test_split_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes,
        [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ])

    def test_split_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes,
        [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bolded", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ])

    def test_split_italic(self):
        node = TextNode("This is text with a _italicized_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes,
        [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italicized", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ])

    def test_split_varied_list(self):
        node1 = TextNode("This is text with a _italicized_ word", TextType.TEXT)
        node2 = TextNode("This is text with a **bolded** word", TextType.TEXT)
        node3 = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes1 = split_nodes_delimiter([node1, node2, node3], "_", TextType.ITALIC)
        new_nodes2 = split_nodes_delimiter(new_nodes1, "**", TextType.BOLD)
        new_nodes3 = split_nodes_delimiter(new_nodes2, "`", TextType.CODE)
        self.assertEqual(new_nodes3,
        [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italicized", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bolded", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ])

    def test_split_varied_list_reverse(self):
        node1 = TextNode("This is text with a _italicized_ word", TextType.TEXT)
        node2 = TextNode("This is text with a **bolded** word", TextType.TEXT)
        node3 = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes1 = split_nodes_delimiter([node1, node2, node3], "`", TextType.CODE)
        new_nodes2 = split_nodes_delimiter(new_nodes1, "**", TextType.BOLD)
        new_nodes3 = split_nodes_delimiter(new_nodes2, "_", TextType.ITALIC)
        self.assertEqual(new_nodes3,
        [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italicized", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bolded", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ])

    def test_split_nested(self):
        node = TextNode("This is text with a _italicized and **bolded**_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes,
        [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italicized and **bolded**", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ])

if __name__ == "__main__":
    unittest.main()

