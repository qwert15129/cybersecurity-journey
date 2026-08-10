username = "admin"
failed_attempts = 4
account_type = "administrator"

if failed_attempts >= 5:
    print(f"ALERT: Account locked for {username}")
elif failed_attempts >= 3:
    print(f"WARNING: Multiple failed login attempts for {username}")
else:
    print(f"Login activity normal for {username}")

if account_type == "administrator" and failed_attempts >= 3:
    print(f"SECURITY ALERT: {username} account may be under attack")
