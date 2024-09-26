import time
import random

#checking pypy runtimes
t0 = time.perf_counter()
'''
def dynamically_create_greeting(greet_style):
    def inner(name):
        countin =0
        print(f'{greet_style} {name}')

    return inner

for j in range(100000):

    say_hello = dynamically_create_greeting(greet_style='hello')
    say_hello('John')
'''
count = 0
summation = 0
'''
for i in range(10000):
    summation = summation + random.choice([1,2,3,4,5,6,77,90])
    count = count +1
'''

#containers like a dictionary

for k in range(100000):
    '''
    dict = {1:32, "two":"banana", 3.5:"cherry", (5,6):"jackfruit", None: "fig", -1: (9876,"fg"), 8+2j: "honey", frozenset([9,10]):"guava", False: "blueberry", "final fruit":"tomato"}
   '''
    dict = {12:"lion", 145:"sealion",534:"tiger", 5641433:"Bear", 896:"hippo", 3479: "dog", 23255: "cat", 654:"fish", 767: "deer", 997:"bengal tiger"}
    key_list = list(dict.keys())
    nthkey = key_list[6]
    print(f'nth element in dict: {dict[nthkey]}')
    


t1 = time.perf_counter()
print(f'counted for: {count}')
total = t1 - t0

print(f'time took: {total}')
