import unittest

from textnode import TextNode, TextType
from split_images_and_links import split_links, split_images

class TestSplitImagesAndLinks(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_images([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images_with_whitespace(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)    and another ![second image](https://i.imgur.com/3elNhQu.png)   ",
            TextType.TEXT,
        )
        new_nodes = split_images([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode("    and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode("   ", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_images_empty(self):
        node = TextNode(
            "This is text with an ![]() and another ![](https://i.imgur.com/3elNhQu.png) and a third ![third image]()",
            TextType.TEXT,
        )
        new_nodes = split_images([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(" and a third ", TextType.TEXT),
                TextNode("third image", TextType.IMAGE, ""),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_links([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links_with_whitespace(self):
        node = TextNode(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png)    and another [second link](https://i.imgur.com/3elNhQu.png)   ",
            TextType.TEXT,
        )
        new_nodes = split_links([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode("    and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode("   ", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_links_empty(self):
        node = TextNode(
            "This is text with an []() and another [](https://i.imgur.com/3elNhQu.png) and a third [third link]()",
            TextType.TEXT,
        )
        new_nodes = split_links([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(" and a third ", TextType.TEXT),
                TextNode("third link", TextType.LINK, ""),
            ],
            new_nodes,
        )

    def test_split_image_no_images(self):
        node = (TextNode("This sentence has no images or links.", TextType.TEXT))
        new_nodes = split_images([node])
        self.assertListEqual([TextNode("This sentence has no images or links.", TextType.TEXT)], new_nodes)

    def test_split_link_no_links(self):
        node = (TextNode("This sentence has no images or links.", TextType.TEXT))
        new_nodes = split_links([node])
        self.assertListEqual([TextNode("This sentence has no images or links.", TextType.TEXT)], new_nodes)

    def test_split_image_given_link(self):
        node = (TextNode("This sentence has one [link](link.com)", TextType.TEXT))
        new_nodes = split_images([node])
        self.assertListEqual([TextNode("This sentence has one [link](link.com)", TextType.TEXT)], new_nodes)

    def test_split_link_given_image(self):
        node = (TextNode("This sentence has one ![image](picture.com)", TextType.TEXT))
        new_nodes = split_links([node])
        self.assertListEqual([TextNode("This sentence has one ![image](picture.com)", TextType.TEXT)], new_nodes)

    def test_both_image_and_link_given(self):
        node = (TextNode("This sentence has one ![image](picture.com) and one [link](link.com)", TextType.TEXT))
        new_nodes = split_links([node])
        new_nodes1 = split_images(new_nodes)
        self.assertListEqual([
            TextNode("This sentence has one ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "picture.com"),
            TextNode(" and one ", TextType.TEXT),
            TextNode("link", TextType.LINK, "link.com")
        ], new_nodes1)

if __name__ == "__main__":
    unittest.main()

