from files import JSON_FILE_PATH
from files import CSV_FILE_PATH
from csv import DictReader
import json


def select_field_from_csv(csv_file) -> list:
    with open(csv_file, newline='') as file:
        reader = DictReader(file)
        return [
            {
                'title': row['Title'],
                'author': row['Author'],
                'pages': int(row['Pages']),
                'genre': row['Genre']

            }
            for row in reader
        ]


def select_field_from_json(json_file) -> list:
    with open(json_file, 'r') as file:
        users_list = json.load(file)
        return [
            {
                'name': user['name'],
                'gender': user['gender'],
                'address': user['address'],
                'age': user['age']
            }
            for user in users_list
        ]


def generator_books(books_list: list):
    for boo in books_list:
        yield boo


def add_books_in_users(users_list: list, gener) -> list:
    try:
        while True:
            for user in users_list:
                book = next(gener)
                user.setdefault('books', []).append(book)
    except StopIteration:
        pass
    return users_list


def main():
    books = select_field_from_csv(CSV_FILE_PATH)
    users = select_field_from_json(JSON_FILE_PATH)
    generator = generator_books(books)
    with open('result.json', 'w') as f:
        s = json.dumps(add_books_in_users(users, generator), indent=4)
        f.write(s)


if __name__ == '__main__':
    main()
