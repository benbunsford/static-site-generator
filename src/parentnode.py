from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError(f"error: parent node must have a tag - current tag is {self.tag}")
        if self.children is None:
            raise ValueError(f"error: parent node must have children - current value of children is {self.children}")
        html_string = ""
        for child in self.children:
            html_string += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{html_string}</{self.tag}>"
