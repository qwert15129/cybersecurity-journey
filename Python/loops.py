login_attempts = [
    "success",
    "failed",
    "failed",
    "success",
    "failed",
    "failed",
    "failed"
]

successful_logins = 0
failed_logins = 0
attempt_number = 0

for attempt in login_attempts:
    attempt_number += 1

    if attempt == "success":
        successful_logins += 1

    elif attempt == "failed":
        failed_logins += 1

    print(f"Attempt {attempt_number}: {attempt}")

print(f"Successful logins: {successful_logins}")
print(f"Failed logins: {failed_logins}")

if failed_logins > 3:
    print("SECURITY ALERT: High number of failed login attempts")
