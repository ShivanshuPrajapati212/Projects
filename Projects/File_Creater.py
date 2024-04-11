import os

os.mkdir('File Creater Result')

for i in range(0,100):
    os.mkdir(f'File Creater Result\\Day {i+1}')


for file in range(0,100):
    f = open(f'File Creater Result\\Day {file+1}\\main.py','w')
    f.write("""# Welcome To Python
 
print("Hello world")
""")
    f.close()
