dict1 = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
for k in list(dict1.keys()):
    k_temp = k
    k_val = dict1[k]
    dict1.pop(k)
    k_temp += str(len(str(k)))
    dict1[k_temp] = k_val
print(dict1)

my_keys = list(dict1.keys())
while len(my_keys) > 0:
    k_temp = my_keys[0]
    k_val = dict1[k_temp]
    dict1.pop(k_temp)
    k_temp += str(len(str(k)))
    dict1[k_temp] = k_val
    my_keys.pop(0)
print(dict1)

