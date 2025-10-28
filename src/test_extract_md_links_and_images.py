import unittest

from extract_md_links_and_images import extract_markdown_images, extract_markdown_links

class TestParentNode(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with an [link](https://www.website.com)"
        )
        self.assertListEqual([("link", "https://www.website.com")], matches)

    def test_extract_markdown_empty_link(self):
        matches = extract_markdown_links(
            "This is text with no link"
        )
        self.assertListEqual([], matches)

    def test_extract_markdown_empty_image(self):
        matches = extract_markdown_images(
            "This is text with no image"
        )
        self.assertListEqual([], matches)

    def test_extract_mixed_alternating(self):
        matches = extract_markdown_links("This is text with an [link](https://www.website.com)")
        matches.extend(extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")) 
        matches.extend(extract_markdown_links("This is text with an [link](https://www.website.com)")) 
        matches.extend(extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")) 
        self.assertListEqual([
            ("link", "https://www.website.com"),
            ("image", "https://i.imgur.com/zjjcJKZ.png"),
            ("link", "https://www.website.com"),
            ("image", "https://i.imgur.com/zjjcJKZ.png")
            ], matches
        )

    def test_extract_find_multiple_per_line_mixed(self):
        matches = extract_markdown_links(
            "This is text with an [link](https://www.website.com) and a [secondlink](link.com) and an ![image](pictures.com)"
        )
        matches.extend(extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a ![secondimage](pictures.com) and a [link](link.com)")
                       )
        self.assertListEqual([
            ("link", "https://www.website.com"),
            ("secondlink", "link.com"),
            ("image", "https://i.imgur.com/zjjcJKZ.png"),
            ("secondimage", "pictures.com")
            ], matches
        )
    def test_empty_text_only(self):
        self.assertListEqual(extract_markdown_links("[](url)"), [("", "url")])
        self.assertListEqual(extract_markdown_images("![](url)"), [("", "url")])

    def test_empty_url_only(self):
        self.assertListEqual(extract_markdown_links("[txt]()"), [("txt", "")])
        self.assertListEqual(extract_markdown_images("![txt]()"), [("txt", "")])

if __name__ == "__main__":
    unittest.main()

