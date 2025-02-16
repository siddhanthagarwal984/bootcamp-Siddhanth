from user import User

user = User("Alice", 30)
json_data = user.to_json()
print(f"Serialized: {json_data}")

new_user = User.from_json(json_data)
print(f"Deserialized: {new_user.name}, {new_user.age}")
