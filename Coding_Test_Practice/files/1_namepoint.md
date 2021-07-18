# name points for a couple with Python

### 문제설영

영어이름 궁합을 계산하여 결과를 return한다. (백준 17296)

Rule 1: 'A':3,'B':2,'C':1,'D':2,'E':4,'F':3,'G':1,'H':3,'I':1,'J':1,'K':3,'L':1,'M':3,'N':2,'O':1,'P':2,'Q':2,'R':2,'S':1,'T':2,'U':1,'V':1,'W':1,'X':2,'Y':2,'Z':1
Rule 2: 알파벳을 번갈아서 쓴 후 점수를 더해준다 (한명의 이름이 더 길면 번갈아 쓴뒤 나머지 이름을 한번에 쓴다)
Rule 3: 점수는 양옆(i, i+1)의 알파벳을 더해준다 ex) A B C -> 3 2 1 -> 5 3

ex) LEESIYUN, MIYAWAKISAKURA ->
-> L M E I E Y S A I W Y A U K N I S A K U R A

- input: 8 14 \n LEESIYUN, MIYAWAKISAKURA
- output: 27%


### 이름 숫자로 변환

우선 이름을 정해진 숫자로 변환시켜야 한다.

- arr에 저장한다.
- nlen = lengths of two names
- names = two names

```python
if int(nlen[0]) < int(nlen[1]):
      namelen = int(nlen[0])
      pointer = 1
else:
    namelen = int(nlen[1])
    pointer = 0

arr = []
for i in range(0,namelen):
    arr.append(point[names[0][i]])
    arr.append(point[names[1][i]])

for i in range(namelen,int(nlen[pointer])):
    arr.append(point[names[pointer][i]])

```


### Get sums

점수를 더해준다

- def로 구현하였다

```python
def addnumber(numbers):
  results = []
  for i in range(0, len(numbers)-1):
      subtotal = int(numbers[i])+int(numbers[i+1])
      subtotal = subtotal%10
      results.append(subtotal)

  return results
```



### 전체 코드

```python
def namepoints(nlen, names):
    def addnumber(numbers):
        results = []
        for i in range(0, len(numbers)-1):
            subtotal = int(numbers[i])+int(numbers[i+1])
            subtotal = subtotal%10
            results.append(subtotal)

        return results

    point = {'A':3, 'B':2,'C':1,'D':2,'E':4,'F':3,'G':1,'H':3,'I':1,'J':1,'K':3,'L':1,'M':3,'N':2,'O':1,'P':2,'Q':2,'R':2,'S':1,'T':2,'U':1,'V':1,'W':1,'X':2,'Y':2,'Z':1}

    if int(nlen[0]) < int(nlen[1]):
        namelen = int(nlen[0])
        pointer = 1
    else:
        namelen = int(nlen[1])
        pointer = 0

    arr = []
    for i in range(0,namelen):
        arr.append(point[names[0][i]])
        arr.append(point[names[1][i]])

    for i in range(namelen,int(nlen[pointer])):
        arr.append(point[names[pointer][i]])

    while len(arr) > 2:
        arr = addnumber(arr)

    percen = ''

    for i in arr:
        percen += str(i)

    if len(percen) > 1 and percen[0] == '0':
        percen = percen[1:]

    percen += '%'

    return percen

nlengths = input().split(" ")
names = input().split(" ")
print(namepoints(nlengths,names))
```



### 다른 방법

- 더 짧은 방법 (thanks to faang12594)

```python
table = {'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 4, 'F': 3, 'G': 1, 'H': 3,
         'I': 1, 'J': 1, 'K': 3, 'L': 1, 'M': 3, 'N': 2, 'O': 1, 'P': 2,
         'Q': 2, 'R': 2, 'S': 1, 'T': 2, 'U': 1, 'V': 1, 'W': 1, 'X': 2,
         'Y': 2, 'Z': 1}

N, M = map(int, input().split())
A, B = map(lambda s: [table[i] for i in s], input().split())

temp = []
for i in range(min(N, M)):
    temp += [A[i], B[i]]

if N > M:
    temp += A[M:]
elif N < M:
    temp += B[N:]

while len(temp) != 2:
    save = []
    for i in range(len(temp) - 1):
        save.append((temp[i] + temp[i+1]) % 10)
    temp = save

print(f'{temp[0] * 10 + temp[1]}%')
```
