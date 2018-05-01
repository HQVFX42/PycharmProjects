# 로또번호 1~45 6개 생성 중복안되게
# random.randrange random.randint(1,45)

import random
result = []
num = 0

for i in range(6):
    while True:
        num = random.randint(1, 45)
        if num not in result:
            result.append(num)
            break

print(result)