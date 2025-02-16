from decorators import role_required

@role_required("admin")
def delete_user(user, username):
    print(f"User {username} deleted.")

admin_user = {"name": "Alice", "role": "admin"}
regular_user = {"name": "Bob", "role": "user"}

delete_user(admin_user, "Charlie")  # Allowed
delete_user(regular_user, "Charlie")  # Access denied
