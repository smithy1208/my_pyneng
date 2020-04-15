import yaml

users_l = []

for i in range(10):
    users_l.append(f'ppp{i}')

users={'users': users_l}

print(users)

with open('users.yml', 'w', encoding='utf-8') as f:
    yaml.dump(users, f)