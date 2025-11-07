import sys

from update_public import update_public
from generate_page import generate_pages_recursive


def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    update_public()
    generate_pages_recursive("content", "template.html", "docs", basepath)

main()
