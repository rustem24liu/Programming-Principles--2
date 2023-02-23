import json

with open("sample-data.json") as f:
    data = json.load(f,)

print("Interface Status")
print('='*80)
print("DN", ' '*47, "Description"," "*9, "Speed", " "*2, "MTU", ' ')
print('-'*50, '-'*20, '', '-'*6, '', '-'*6)

for i in range(18):
    for n, m in data["imdata"][i]["l1PhysIf"]["attributes"].items():
        if n == 'dn':
            print(m, end ='                              ')
        if n == 'speed':
            print(m, end = '   ')
        if n == 'mtu':
            print(m, end ='  ')
    print()


