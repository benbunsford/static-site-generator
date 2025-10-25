import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_2(self):
        node = TextNode("This is a text node", TextType.LINK)
        node2 = TextNode("This is a text node", TextType.IMAGE)
        self.assertNotEqual(node, node2)

    def test_eq_3(self):
        node = TextNode("This is a txt node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_4(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_5(self):
        node = TextNode("This is a text node", TextType.BOLD, "abc.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "abc.com")
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
