import unittest

from markdown_to_html_node import markdown_to_html_node

class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_headings(self):
        md = """
# Heading 1

## Heading 2

### Heading 3 with **bold**

#### Heading 4
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading 1</h1><h2>Heading 2</h2><h3>Heading 3 with <b>bold</b></h3><h4>Heading 4</h4></div>",
        )

    def test_quote_block(self):
        md = """
> This is a quote
> with multiple lines
> and **bold** text
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote with multiple lines and <b>bold</b> text</blockquote></div>",
        )

    def test_unordered_list(self):
        md = """
- First item
- Second item with **bold**
- Third item with _italic_
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>First item</li><li>Second item with <b>bold</b></li><li>Third item with <i>italic</i></li></ul></div>",
        )

    def test_ordered_list(self):
        md = """
1. First item
2. Second item
3. Third item with `code`
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>First item</li><li>Second item</li><li>Third item with <code>code</code></li></ol></div>",
        )

    def test_mixed_content(self):
        md = """
# Main Heading

This is a paragraph with **bold** and _italic_ text.

## Subheading

- List item 1
- List item 2

> A quote block here

```
code block
with multiple lines
```

Another paragraph at the end.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        # Just verify it doesn't crash and returns a div
        self.assertTrue(html.startswith("<div>"))
        self.assertTrue(html.endswith("</div>"))
        self.assertIn("<h1>Main Heading</h1>", html)
        self.assertIn("<h2>Subheading</h2>", html)
        self.assertIn("<ul>", html)
        self.assertIn("<blockquote>", html)
        self.assertIn("<pre><code>", html)

    def test_empty_markdown(self):
        md = ""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div></div>")

    def test_single_paragraph(self):
        md = "Just a simple paragraph"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><p>Just a simple paragraph</p></div>")

    def test_multiple_inline_formats(self):
        md = "This has **bold** and _italic_ and `code` and **_bold italic_** text"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertIn("<b>bold</b>", html)
        self.assertIn("<i>italic</i>", html)
        self.assertIn("<code>code</code>", html)

    def test_heading_levels(self):
        md = """
# H1

## H2

### H3

#### H4

##### H5

###### H6
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        for i in range(1, 7):
            self.assertIn(f"<h{i}>H{i}</h{i}>", html)

    def test_code_block_preserves_newlines(self):
        md = """
```
line 1
line 2
line 3
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertIn("line 1\nline 2\nline 3", html)

    def test_nested_list_items(self):
        md = """
- Item with **bold**
- Item with _italic_
- Item with `code`
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html.count("<li>"), 3)
        self.assertIn("<b>bold</b>", html)
        self.assertIn("<i>italic</i>", html)
        self.assertIn("<code>code</code>", html)

    def test_quote_with_inline_formatting(self):
        md = "> Quote with **bold** and _italic_ and `code`"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertIn("<blockquote>", html)
        self.assertIn("<b>bold</b>", html)
        self.assertIn("<i>italic</i>", html)
        self.assertIn("<code>code</code>", html)

if __name__ == 'main':
    unittest.main()
