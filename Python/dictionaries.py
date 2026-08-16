failed_logins ={
    "joel": 1,
    "admin": 5,
    "sarah": 0,
    "root": 7,
    "david": 2,
    "superuser": 4,
    "emma": 1
}

suspicious_accounts = {}

highest_failed_logins = 0
most_suspicious_user = ""

for user, attempt in failed_logins.items():
    print(f"{user} has {attempt} failed login attempts")
    if attempt >= 5:
        print(f"ALERT: {user} account should be locked")
        suspicious_accounts[user] = attempt
    if attempt > highest_failed_logins:
        highest_failed_logins = attempt
        most_suspicious_user = user
    elif attempt >= 3:
        print(f"WARNING: {user} has multiple failed login attempts")
        suspicious_accounts[user] = attempt

print(f"Suspicious accounts: {suspicious_accounts}")

print(f"Total accounts checked: {len(failed_logins)}")
print(f"Total suspicious accounts: {len(suspicious_accounts)}")

print(f"Account with most failed logins: {most_suspicious_user}")
print(f"Failed attempts: {highest_failed_logins}")
