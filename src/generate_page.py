import os
import re

from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    with open(from_path, "r") as f:
        markdown = f.read()
    with open(template_path, "r") as t:
        template = t.read()
    html_node = markdown_to_html_node(markdown)
    title = extract_title(markdown)
    title_added = template.replace('{{ Title }}', title)
    content_added = title_added.replace('{{ Content }}', html_node.to_html())
    parent_dir = os.path.dirname(dest_path)
    os.makedirs(parent_dir, exist_ok=True)
    with open(dest_path, "w") as d:
        d.write(content_added)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    content_items = os.listdir(dir_path_content)
    for item in content_items:
        content_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item.replace(".md", ".html"))
        if os.path.isdir(content_path):
            generate_pages_recursive(
                content_path,
                template_path,
                dest_path
            )
        elif (
            os.path.isfile(content_path) and
            re.search(r"\.md$", content_path)
        ):
            generate_page(content_path, template_path, dest_path)
        else:
            print(content_path, os.path.isfile(content_path), re.search(r"\.md$", content_path))
