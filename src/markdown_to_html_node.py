import re

from block_to_block_type import block_to_block_type, BlockType
from markdown_to_blocks import markdown_to_blocks
from text_node_to_leaf_node import text_node_to_leaf_node
from text_to_textnodes import text_to_textnodes
from parentnode import ParentNode

from textnode import TextNode, TextType


def markdown_to_html_node(markdown_doc):
    blocks = markdown_to_blocks(markdown_doc)
    blocks_as_html_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        tag = get_tag(block, block_type)
        stripped_block = strip_block(block, block_type)
        block_node = block_to_nodes(stripped_block, block_type, tag)
        blocks_as_html_nodes.append(block_node)
    div = ParentNode("div", blocks_as_html_nodes)
    return div

def get_tag(block, block_type):
    match block_type:
        case BlockType.PARAGRAPH:
            return "p"
        case BlockType.HEADING:
            num_hashes = len(block) - len(block.lstrip('#'))
            return f"h{num_hashes}"
        case BlockType.CODE:
            return "pre"
        case BlockType.QUOTE:
            return "blockquote"
        case BlockType.UNORDERED_LIST:
            return "ul"
        case BlockType.ORDERED_LIST:
            return "ol"
        case _:
            raise TypeError("error: not a valid BlockType")

def strip_block(block, block_type):
    block = block.strip()
    match block_type:
        case BlockType.PARAGRAPH:
            return strip_paragraph(block)
        case BlockType.HEADING:
            return block.lstrip('# ')
        case BlockType.CODE:
            stripped = block[4:-3]
            if stripped.startswith("\n"):
                stripped = stripped[1:]
            return stripped
        case BlockType.QUOTE:
            return strip_quote(block)
        case _:
            return block

def strip_list_items(block, block_type):
    list_items = []
    lines = block.split("\n")
    for l in lines:
        line = l.strip()
        match = None
        if block_type == BlockType.UNORDERED_LIST:
            match = re.match(r"^- (.*)", line)
        elif block_type == BlockType.ORDERED_LIST:
            match = re.match(r"^\d\. (.*)", line)
        if match:
            stripped = match.group(1)
            list_items.append(stripped)
    return list_items

def strip_quote(block):
    line_list = []
    lines = block.split("\n")
    for line in lines:
        match = re.match(r"^> (.*)", line)
        if match:
            stripped = match.group(1)
            line_list.append(stripped)
    return " ".join(line_list)

def strip_paragraph(block):
    line_list = []
    lines = block.split("\n")
    for line in lines:
        stripped = line.strip()
        if stripped:
            line_list.append(stripped)
    return " ".join(line_list)

def text_to_children(text):
    inline_text_nodes = text_to_textnodes(text)
    inline_html_nodes = []
    for node in inline_text_nodes:
        inline_html_nodes.append(text_node_to_leaf_node(node))
    return inline_html_nodes

def block_to_nodes(block, block_type, tag):
    if block_type == BlockType.UNORDERED_LIST or block_type == BlockType.ORDERED_LIST:
        line_nodes = []
        stripped_lines = strip_list_items(block, block_type)
        for line in stripped_lines:
            line_nodes.append(ParentNode("li", text_to_children(line)))
        return ParentNode(tag, line_nodes)
    elif block_type == BlockType.CODE:
        code_node = TextNode(block, TextType.CODE)
        code_leaf_node = text_node_to_leaf_node(code_node)
        return ParentNode(tag, [code_leaf_node])
    else:
        return ParentNode(tag, text_to_children(block))

