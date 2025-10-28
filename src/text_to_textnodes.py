from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter
from split_images_and_links import split_images, split_links


def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    bolded = split_nodes_delimiter([node], "**", TextType.BOLD)
    italicized = split_nodes_delimiter(bolded, "_", TextType.ITALIC)
    code_formatted = split_nodes_delimiter(italicized, "`", TextType.CODE)
    image_split = split_images(code_formatted)
    link_split = split_links(image_split)
    return link_split
