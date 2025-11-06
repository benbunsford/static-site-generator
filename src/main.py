from update_public import update_public
from generate_page import generate_pages_recursive

def main():
    update_public()
    generate_pages_recursive("content", "template.html", "public")

main()
