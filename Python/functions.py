username = "admin"
failed_attempts = 5

def check_account(username, failed_attempts):
    if failed_attempts >= 5:
        return(f"ALERT: {username} account should be locked")
    elif failed_attempts >= 3:
        return(f"WARNING: {username} has multiple failed login attempts")
    else:
        return(f"{username} login activity is normal")

admin_result = check_account("admin", 5)
joel_result = check_account("joel", 1)
root_result = check_account("root", 3)

print(admin_result)
print(joel_result)
print(root_result)

login_attempts = [
    "success",
    "failed",
    "failed",
    "success",
    "failed",
    "failed",
    "failed"
]

def count_failed(login_attempts):
    failed_count = 0
    for attempt in login_attempts:
        if attempt == "failed":
            failed_count += 1
    return failed_count

failed_count = count_failed(login_attempts)
print(f"Total failed login attempts: {failed_count}")

login_records = [
    ["admin", "failed"],
    ["joel", "success"],
    ["admin", "failed"],
    ["root", "failed"],
    ["sarah", "success"],
    ["admin", "failed"],
    ["root", "failed"],
    ["admin", "success"],
    ["root", "failed"]
]

def analyse_logins(login_records):
    successful_logins = 0
    failed_logins = 0
    failed_by_user = {}
    for record in login_records:
        username, status = record
        if status == "success":
            successful_logins += 1
        elif status == "failed":
            failed_logins += 1
            if username in failed_by_user:
                failed_by_user[username] += 1
            else:
                failed_by_user[username] = 1
    return successful_logins, failed_logins, failed_by_user

successful, failed, failed_by_user = analyse_logins(login_records)
print(f"Successful logins: {successful}")
print(f"Failed logins: {failed}")
print(f"Failed logins by user: {failed_by_user}")
