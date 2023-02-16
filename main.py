def parse_file_line(line: str):
    line = line.strip().split()
    _, *name, money, category = line
    name = ' '.join(name)
    money = float(money[:-1])

    return name, money, category


def total_by_categories(file_path):
    categories = {}
    with open(file_path, 'r') as file:
        for line in file:
            _, money, category = parse_file_line(line)
            if category not in categories:
                categories[category] = money
            else:
                categories[category] += money

    return categories


if __name__ == '__main__':
    res = total_by_categories('hw_10_test.txt')
    for key, value in res.items():
        print(f'{key}: {value:.2f}$')
