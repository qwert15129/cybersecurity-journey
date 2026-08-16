users = [
    "joel",
    "admin",
    "sarah",
    "root",
    "david",
    "superuser",
    "emma"
]

sensitive_accounts = [
    "admin",
    "root",
    "superuser"
]

flagged_accounts = []

for user in users:
    print(f"Checking account: {user}")
    if user in sensitive_accounts:
        print(f"SECURITY NOTICE: {user} is a sensitive account")
        flagged_accounts.append(user)

print(f"Flagged accounts: {flagged_accounts}")

print(f"Total accounts checked: {len(users)}")
print(f"Total sensitive accounts found: {len(flagged_accounts)}")
