import os

f = r'C:\Users\ПК\Desktop\ruspythoh\Programming-p2\week5'
print(f'Exist: {os.access(f,os.F_OK)}')
print(f'Rreadability: {os.access(f,os.R_OK)}')
print(f'Writability: {os.access(f,os.W_OK)}')
print(f'Executability: {os.access(f,os.X_OK)}')

