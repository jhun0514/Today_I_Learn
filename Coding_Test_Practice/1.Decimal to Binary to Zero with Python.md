# Decimal to Binary to Zero with Python

### 문제설영

Decimal 숫자(input)를 Binary로 변환 후 모든 binary 숫자를 0으로 바꿔서 바꾼과정을 count하여  return한다.

Rule 1: index [i] 숫자를 바꾸기 위해선 [i+1] = 1 AND all[i+1:] = 0 을 만족해야 한다.
Rule 2: 마지막 숫자는 자유롭게 변경가능하다.

ex) 100 -> 101 -> 111 -> 110 -> 010 -> 011 -> 001 -> 000 = 7 steps  / input: 100, output: 7


### Decimal to Binary

우선 10진수 숫자를 2진수로 변환시켜야 한다.

- Function 대신 for loop를 사용하였다.
- number = input decimal number

```python
arr = []
def tobin(den):
    if (den > 1):
        tobin(den // 2)
    arr.append(den % 2)
tobin(number)
```


### Binary to Zero

이부분은 몇가지 방법이 있겠지만 우선 숫자 규칙을 찾아 적용하였다.

- 1이 있는 부분의 binary 숫자에 2를 곱한 후 -1 해준다. 그렇게 모든 1 부분을 계산후 alternate fashion으로 +, -를 반복한다.
- ex) 1011의 경우 (2 * 8 - 1) - (2 * 2 - 1) + (2 * 1 - 1)

```python
# make binary number to zero and count it
for i in range(arrlen):
    if arr[i] == 1:
        power = 2**(arrlen - i - 1)
    else:
        power = 0
    step = arr[i]*(power*2 - 1)

    count += step*sign

    if arr[i] == 1:
        sign = sign * -1

return count
```



### 전체 코드

현재는 비공개로 결정했다.
혹시 필요하신 분은 이메일로 연락 바랍니다.



### 다른 방법

Gray code를 이용하는 방법도 있다.
차후 업로드 예정.
