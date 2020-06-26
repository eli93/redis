numbers = input('a b x = ')

numbers = numbers.split(' ')

a = int(numbers[0])
b = int(numbers[1])
x = int(numbers[2])

# for i in range(len(numbers)):
#     if numbers[i] != ' ' and numbers[i+1] == ' ':

#**** maghsoom alayhaye a

i = 1
m_a = []
while i <= a:
    if a % i == 0:
        m_a.append(i)
    i += 1

#**** maghsoom alayhaye b

i = 1
m_b = []
while i <= b:
    if b % i == 0:
        m_b.append(i)
    i += 1

# *********
count = 0
for a in m_a:
    for b in m_b:
        if a + b <= x:
            count += 1


print(f'answer is {count}')
