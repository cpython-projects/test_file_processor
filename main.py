def parse_file_line(line: str):
    line = line.strip().split()
    _, *name, money, category = line
    name = ' '.join(name)
    money = float(money[:-1])

    return name, money, category