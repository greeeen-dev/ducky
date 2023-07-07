import json
import os

totp = []

accounts = json.load(open('authy-to-bitwarden-export.json','r',encoding='utf-8'))

for account in accounts['items']:
    totp.append(account['login']['totp']+'\n')

writer = open('auth_codes.txt','w+',encoding='utf-8')
writer.writelines(totp)
writer.close()

print('Saved to ' + os.getcwd() + '/auth_codes.txt')
