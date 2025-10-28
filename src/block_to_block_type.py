import re

from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(markdown_block):
    stripped_md_block = markdown_block.strip()
    if re.match(r"^#{1,6} .*$", stripped_md_block):
        return BlockType.HEADING

    elif re.match(r"^```.*```$", stripped_md_block, flags=re.DOTALL):
        return BlockType.CODE

    lines = stripped_md_block.split("\n")

    for i in range(len(lines)):
        if not re.match(r"^> .*$", lines[i]):
            break
        if i == len(lines)-1:
            return BlockType.QUOTE

    for i in range(len(lines)):
        if not re.match(r"^- .*$", lines[i]):
            break
        if i == len(lines)-1:
            return BlockType.UNORDERED_LIST

    j = 1
    for i in range(len(lines)):
        if not re.match(rf"^{j}\. .*$", lines[i]):
            break
        if i == len(lines)-1:
            return BlockType.ORDERED_LIST
        j += 1

    return BlockType.PARAGRAPH
