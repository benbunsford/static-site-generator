from textnode import TextNode, TextType
from extract_md_links_and_images import extract_markdown_images, extract_markdown_links


def split_images(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        original_text = node.text
        matches = extract_markdown_images(original_text)
        if not matches:
            new_nodes.append(node)
            continue
        for i in range(len(matches)):
            match = matches[i]
            image_alt = match[0]
            image_link = match[1]
            sections = original_text.split(f"![{image_alt}]({image_link})", maxsplit=1)
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            if image_alt or image_link:
                new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
            original_text = sections[1]
        if original_text:
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def split_links(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        original_text = node.text
        matches = extract_markdown_links(original_text)
        if not matches:
            new_nodes.append(node)
            continue
        for i in range(len(matches)):
            match = matches[i]
            link_anchor = match[0]
            link_url = match[1]
            sections = original_text.split(f"[{link_anchor}]({link_url})", maxsplit=1)
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            if link_anchor or link_url:
                new_nodes.append(TextNode(link_anchor, TextType.LINK, link_url))
            original_text = sections[1]
        if original_text:
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes
