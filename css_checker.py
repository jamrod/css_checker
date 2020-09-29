# read css file and compile a list of classes and a list of ids


def read_css(css):
    ids = []
    classes = []
    with open(css, 'r') as file:
        for line in file:
            if "#" in line:
                s = line.strip()
                s = s[1:-2]
                ids.append(s)
            if '.' in line and '{' in line:
                s = line.strip()
                s = s[1:-2]
                classes.append(s)
    return (tuple(ids), tuple(classes))


def read_file(source):
    ids = []
    classes = []
    with open(source, 'r') as file:
        for line in file:
            if 'id=' in line:
                start = line.index("id=") + 1
                temp = line[start:]
                end = temp.index("\"")
                s = temp[:end]


print(read_css("testFiles/style.css"))
