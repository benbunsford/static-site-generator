import unittest

from htmlnode import HTMLNode

class TestTextNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(None, None, None, {'href': 'wings.com', 'target': 'dingaling'})
        self.assertEqual(
            " href='wings.com' target='dingaling'", node.props_to_html()
        )

    def test_props2(self):
        node = HTMLNode(None, None, None, None)
        self.assertEqual(
            "", node.props_to_html()
        )

    def test_repr(self):
        node = HTMLNode('tag', 'value', ['child1', 'child2', 'child3'], {'href': 'wings.com', 'target': 'dingaling'})
        self.assertEqual(
            f'''
            HTMLNode
            tag: tag
            value: value
            children: ['child1', 'child2', 'child3']
            props: {{'href': 'wings.com', 'target': 'dingaling'}}
            ''',
            repr(node)
        )

if __name__ == "__main__":
    unittest.main()

