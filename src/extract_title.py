import re

def extract_title(markdown):
    split = markdown.split("\n")
    match = re.match(r"^# (.*)", split[0])
    if match is not None:
        return match.group(1).strip()
    raise Exception("NoTitleError: Markdown document needs a title.")

