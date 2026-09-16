n = 122333444

freq = {}

while n > 0:
    digit = n % 10
    freq[digit] = freq.get(digit, 0) + 1
    n //= 10

print(freq)