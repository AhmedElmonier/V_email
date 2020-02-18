import pandas as pd
from validate_email import validate_email

file = pd.read_csv('emails.csv', delimiter=',', encoding='unicode_escape')
emails = list(file['Email'])
#print(emails)

count = 1
for email in emails:
    print(count)
    count = count +1
    print("Validating email", email)
    is_valid = validate_email(email)
    is_valid = validate_email('example@example.com',check_mx=True)
    is_valid = validate_email('example@example.com',verify=True)