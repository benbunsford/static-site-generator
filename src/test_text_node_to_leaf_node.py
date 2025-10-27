import unittest

from textnode import TextNode, TextType
from leafnode import LeafNode
from text_node_to_leaf_node import text_node_to_leaf_node

class TestTextNodeToLeafNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        leaf_node = text_node_to_leaf_node(node)
        self.assertEqual(leaf_node.tag, None)
        self.assertEqual(leaf_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        leaf_node = text_node_to_leaf_node(node)
        self.assertEqual(leaf_node.tag, "b")
        self.assertEqual(leaf_node.value, "This is a text node")

    def test_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        leaf_node = text_node_to_leaf_node(node)
        self.assertEqual(leaf_node.tag, "i")
        self.assertEqual(leaf_node.value, "This is a text node")

    def test_code(self):
        node = TextNode("This is a text node", TextType.CODE)
        leaf_node = text_node_to_leaf_node(node)
        self.assertEqual(leaf_node.tag, "code")
        self.assertEqual(leaf_node.value, "This is a text node")

    def test_link(self):
        node = TextNode("This is a text node", TextType.LINK, "url.com")
        leaf_node = text_node_to_leaf_node(node)
        self.assertEqual(leaf_node.tag, "a")
        self.assertEqual(leaf_node.value, "This is a text node")
        self.assertEqual(leaf_node.props, {"href": "url.com"})
        
    def test_image(self):
        node = TextNode("This is a text node", TextType.IMAGE, "url.com")
        leaf_node = text_node_to_leaf_node(node)
        self.assertEqual(leaf_node.tag, "img")
        self.assertEqual(leaf_node.value, "")
        self.assertEqual(leaf_node.props, {"src": "url.com", "alt": "This is a text node"})

    def test_unknown(self):
        node = TextNode("This is a text node", None)
        with self.assertRaises(ValueError) as cm:
            text_node_to_leaf_node(node)
        self.assertEqual(
            str(cm.exception), "error: unknown TextType"
        )

if __name__ == "__main__":
    unittest.main()

