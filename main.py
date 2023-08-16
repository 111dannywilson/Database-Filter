from functools import wraps


def authenticate(func):
    def wrapper():
        data = func()
        print("Data added")
        remove_keys = [
            key for key, value in data.items() if not value or value.strip() == ""
        ]
        for key in remove_keys:
            data.pop(key, None)
        # Add code to Append to database
        return database

    return wrapper


@authenticate
def receive_data():
    data = {
        "name": input("name: "),
        "gender": input("gender: "),
        "age": input("age: "),
    }
    database.append(data)
    return data


# Loca Database
# database = []
output = receive_data()
print(output)
