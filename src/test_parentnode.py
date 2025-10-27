import unittest

from parentnode import ParentNode 
from leafnode import LeafNode
import parentnode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_child_props(self):
        child_node = LeafNode("span", "child", {"href": "www.site.com"})
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span href='www.site.com'>child</span></div>")

    def test_to_html_mutation(self):
        child_node = LeafNode("span", "child", {"href": "www.site.com"})
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), parent_node.to_html())

    def test_to_html_50_children(self):
        child_list = [LeafNode(None, 'x') for i in range(50)]
        parent_node = ParentNode("div", child_list)
        self.assertEqual(parent_node.to_html(), f"<div>{'x' * 50}</div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_no_children(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError) as cm:
            parent_node.to_html()
        self.assertEqual(
            str(cm.exception), f"error: parent node must have children - current value of children is {parent_node.children}"
        )

    def test_to_html_no_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError) as cm:
            parent_node.to_html()
        self.assertEqual(
            str(cm.exception),
            f"error: parent node must have a tag - current tag is {parent_node.tag}"
        )

    def test_many_mixed_children(self):
        kids = []
        for i in range(25):
            kids.append(LeafNode(None, "x"))
            kids.append(LeafNode("b", "y"))
        parent = ParentNode("div", kids)
        expected = "<div>" + ("x<b>y</b>" * 25) + "</div>"
        self.assertEqual(parent.to_html(), expected)

if __name__ == "__main__":
    unittest.main()

