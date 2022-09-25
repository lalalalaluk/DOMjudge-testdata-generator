import subprocess
import os
import random

#############################################################################

# 1. 請先把解答程式放在ans.py
# 2. 確定terminal開在generator.py同一層的資料夾 ex: C:/xxx/xxx/a001
# 3. 設定sample的資料
# 4. 設定測資範本

sample = [
    "5 10",
    "1 3",
]

# 在這邊定義測資數量!!!
secret_count = 10

# 產生測資
secret = []
for i in range(secret_count):
    # 在這邊定義測資!!!
    r_rample = random.sample(range(0,10000), 2)
    sample_input = ""
    for r in r_rample:
        sample_input += str(r) + ' '
    secret.append(sample_input.strip())
    
    
###############################################################################


# 把測資跟secret放進ans.py並取出output
def generate_in_ans_file(input, path, number):
    p = subprocess.Popen(os.getcwd() + "\\ans.py",
                        stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf-8', shell=True)

    output, error = p.communicate(input=input)
    print(input, output, path, number)
    with open(f"{path}\\{number}.in",'w', encoding = 'utf-8') as f:
        f.write(input)
    with open(f"{path}\\{number}.ans",'w', encoding = 'utf-8') as f:
        f.write(output)

# 定義路徑
sample_path = os.getcwd() + "\\data\\sample"
secret_path = os.getcwd() + "\\data\\secret"
path = [
    os.getcwd() + "\\data",
    sample_path,
    secret_path
]

# 建立sample跟secret資料夾
for p in path:
    if not os.path.isdir(p):
        os.mkdir(p)

# 產生input跟ans
number = 0
for i, d in enumerate(sample):
    number += 1
    generate_in_ans_file(d, sample_path, number)
for i, d in enumerate(secret):
    number += 1
    generate_in_ans_file(d, secret_path, number)

