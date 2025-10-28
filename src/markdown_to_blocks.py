def markdown_to_blocks(markdown):
    paragraphs = markdown.split("\n\n")
    result = []
    for pg in paragraphs:
        stripped = pg.strip()
        if stripped and stripped != "\n":
            result.append(stripped)
    return result

