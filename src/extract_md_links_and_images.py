import re


def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)]\(([^\(\)]*)\)", text)
    return matches


print(extract_markdown_links("This is text with an [link](https://www.website.com) and a [secondlink](link.com) and an ![image](pictures.com)"))
print(extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a ![secondimage](pictures.com) and a [link](link.com)"))
