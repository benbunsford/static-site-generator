from update_public import update_public
from generate_page import generate_page

def main():
    update_public()
    generate_page("content/index.md", "template.html", "public/index.html")

main()
