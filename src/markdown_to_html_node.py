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
        block_html_node = block_to_html_node(block, block_type)
        cleaned_block_text = clean_text(block, block_type)
        blocks_as_html_nodes.append(block_html_node)
        if block_type == BlockType.CODE:
            code_node = TextNode(cleaned_block_text, TextType.CODE)
            code_leaf_node = text_node_to_leaf_node(code_node)
            block_html_node.children.append(code_leaf_node)
        else:
            stripped_lines = strip_lines(cleaned_block_text)
            inline_nodes = text_to_children(stripped_lines)
            block_html_node.children.extend(inline_nodes)
    div = ParentNode("div", blocks_as_html_nodes)
    return div

def clean_text(block, block_type):
    match block_type:
        case BlockType.PARAGRAPH:
            return block
        case BlockType.HEADING:
            return block.lstrip('# ')
        case BlockType.CODE:
            stripped = block.strip("```")
            if stripped.startswith("\n"):
                stripped = stripped[1:]
            return stripped
        case BlockType.QUOTE:
            return block.strip("> ")
        case BlockType.UNORDERED_LIST:
            list_items = []
            lines = block.split("\n")
            for line in lines:
                m = re.match(r"^\s*[-*+]\s+(.*)$", line)
                if m:
                    stripped = m.group(1)
                    list_items.append(stripped)
            return "\n".join(list_items)
        case BlockType.ORDERED_LIST:
            list_items = []
            lines = block.split("\n")
            for line in lines:
                m = re.match(r"^\s*(\d+)\.\s+(.*)$", line)
                if m:
                    stripped = m.group(2)
                    list_items.append(stripped)
            return "\n".join(list_items)
        case _:
            raise TypeError("error: not a valid BlockType")

def strip_lines(text):
    lines = text.split("\n")
    stripped_list = []
    for line in lines:
        stripped = line.strip().lstrip("- >")
        if stripped:
            stripped_list.append(stripped)
    return " ".join(stripped_list)

def block_to_html_node(block, block_type):
    match block_type:
        case BlockType.PARAGRAPH:
            return ParentNode("p", [])
        case BlockType.HEADING:
            num_hashes = len(block) - len(block.lstrip('#'))
            return ParentNode(f"h{num_hashes}", [])
        case BlockType.CODE:
            pre_node = ParentNode("pre", [])
            return pre_node
        case BlockType.QUOTE:
            return ParentNode("blockquote", [])
        case BlockType.UNORDERED_LIST:
            list_items = []
            lines = block.split("\n")
            for line in lines:
                stripped_line = strip_lines(line)
                line_nodes = text_to_children(stripped_line)
                list_items.append(ParentNode("li", line_nodes))
            return ParentNode("ul", list_items)
        case BlockType.ORDERED_LIST:
            list_items = []
            lines = block.split("\n")
            for line in lines:
                stripped_line = strip_lines(line)
                line_nodes = text_to_children(stripped_line)
                list_items.append(ParentNode("li", line_nodes))
            return ParentNode("ol", list_items)
        case _:
            raise TypeError("error: not a valid BlockType")

def text_to_children(text):
    inline_text_nodes = text_to_textnodes(text)
    inline_html_nodes = []
    for node in inline_text_nodes:
        inline_html_nodes.append(text_node_to_leaf_node(node))
    return inline_html_nodes

