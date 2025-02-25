from django.contrib.auth.models import User, Group

# Fetch the user instance
user = User.objects.get(username='your_username')  # Replace 'your_username' with the actual username

# Fetch the admin group instance
admin_group = Group.objects.get(name='admin')  # Ensure the group 'admin' exists

# Add the user to the admin group
user.groups.add(admin_group)

# Mark the user as staff
user.is_staff = True

# Save the changes
user.save()

print(f"User {user.username} has been added to the admin group and marked as staff.")
