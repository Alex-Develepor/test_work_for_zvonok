# Задание 1
# SELECT article.id, article.title, article.text
#     FROM article
#     LEFT JOIN comment ON article.id = comment.article_id
#     WHERE comment.id is NULL;


# Задание 2

import re

result: dict[str: list[int]] = {}


def get_employer_info(text: str):
    regex = r'(.*) (\d+)'
    match = re.match(regex, text)
    name = match.group(1)
    hours = int(match.group(2))
    return name, hours


def count_hours(name: str, hours: int):
    if name not in result:
        result[name] = [hours]
    else:
        result[name].append(hours)


def main():
    with open('input.txt', "r") as file:
        for text in file:
            count_hours(*get_employer_info(text))
    for emloyer, hours in result.items():
        print(f"{emloyer}: {', '.join(map(str, hours))}; sum: {sum(hours)}")


main()
