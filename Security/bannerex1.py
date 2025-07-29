def print_box_banner(text):
    """Prints text within a box using Unicode characters."""
    lines = text.split('\n')
    max_len = max(len(line) for line in lines)
    
    print("┏" + "━" * (max_len + 2) + "┓")
    for line in lines:
        print("┃ " + line.ljust(max_len) + " ┃")
    print("┗" + "━" * (max_len + 2) + "┛")

print_box_banner("System Status:\nAll good!")

