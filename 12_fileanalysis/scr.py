import re

from collections import defaultdict

EMAIL_PATTERN=r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

def get_email_pattern(text):
    return re.findall(EMAIL_PATTERN, text)

def get_sorted_emails():
    freq_email = defaultdict(int)
    with open('enron_3000.csv') as ifile:
        for iline in ifile.readlines():
            for email in get_email_pattern(iline):
                freq_email[email] += 1

    sorted_emails = sorted(freq_email.items(), key=lambda x: x[1], reverse=True)
    return sorted_emails

sorted_emails = get_sorted_emails()
for email, count in sorted_emails[:20]:
    print(f"{email} {count}")
