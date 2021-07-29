s = [100, 48, 50, 164, 352]
print(s)
for i in range(len(s)):
    s[i] *= -2

print(s)

j = 0
while j < len(s):
    s[j] *= -2
    j += 1
print(s)
