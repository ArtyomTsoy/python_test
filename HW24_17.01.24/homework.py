import time
import random

def create_file(output):
    time.sleep(1)
    random_number = random.randint(1, 1000)
    with open(output, 'w') as file:
        file.write(str(random_number))

start = time.time()
for i in range(1000):
    create_file(f'{i}.txt')
end = time.time()

elapsed_time = end - start
print(elapsed_time)