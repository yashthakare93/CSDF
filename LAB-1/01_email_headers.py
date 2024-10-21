import email
from email.parser import HeaderParser

with open('email.eml', 'r') as f:
    msg = email.message_from_file(f)

headers = HeaderParser().parsestr(msg.as_string())

print('Headers Found:')
for key, value in headers.items():
    print(f'{key}: {value}')

spf_dkim = headers.get('Authentication-Results', 'Not found')
print(f'SPF and DKIM: {spf_dkim}')
