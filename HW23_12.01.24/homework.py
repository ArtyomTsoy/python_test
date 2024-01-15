import time

def file(output):
    time.sleep(1)
    with open(output, 'w') as file:
        file.write('file is created')
    print(f'File {output} is created')

start = time.time()

for i in range(100):
    file(f'file_{i}.txt')

end = time.time()

elapsed_time = end - start
print(elapsed_time)