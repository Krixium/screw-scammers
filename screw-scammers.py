import os
import random
import requests
import string

random.seed = (os.urandom(1024))
chars = string.ascii_letters + string.digits + '!@#$%^&*()'
scammer_url = "https://classic-help.com/up.asp?ref=https%3A%2F%2Fus.battle.net%2Faccount%2Fmanagement%2Findex.xml&app=bam"

with open("fake_emails.txt") as emails:
    for email in emails:
        account = email.strip()
        password = ''.join(random.choice(chars) for i in range(random.randint(6, 16)))
        result = requests.post(scammer_url, allow_redirects=False, data={
            "accountName": account,
            "password": password
        })

        print("status[%s] email[%s] password[%s]" % (result.status_code, account, password))
