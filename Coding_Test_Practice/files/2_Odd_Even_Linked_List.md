# Odd Even Linked List

### 문제설영

Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list. (leetcode 328)

Rule 1: The first node is considered odd, and the second node is even, and so on.
Rule 2: Note that the relative order inside both the even and odd groups should remain as it was in the input.
Rule 3: You must solve the problem in O(1) extra space complexity and O(n) time complexity.

ex) [2,1,3,5,6,4,7] -> [2,3,6,7,1,5,4]

- input: [2,1,3,5,6,4,7]
- output: [2,3,6,7,1,5,4]


### Even 포인터 노드 생성

우선 이름을 정해진 숫자로 변환시켜야 한다.

- 빈 linkedlist를 생성한 뒤 even 노드들을 저장해준다.

```python
temp = ListNode(0)
current = temp
```


### odd, even 나누기

odd 와 even 을 나누어 준다

- odd 리스트를 따로 만들지 않고 head 자체를 바꾸어 준다.

```python
while(pointer):
    if (ind%2 != 0):
        pointer = pointer.next
        ind += 1
    else:
        ind += 1
        current.next = ListNode(pointer.val)
        current = current.next
        pointer = pointer.next
        head.next = head.next.next
        if(pointer):
            head = head.next
```


### odd, even 합치기

나누어진 odd 와 even을 합쳐준다.

- even 리스트가 없다면 합치지 않고 리턴한다.

```python
if (temp.next == None):
    return answer
head.next = temp.next
```



### 전체 코드

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        temp = ListNode(0)
        current = temp
        pointer = head
        answer = head
        ind = 1
        while(pointer):
            if (ind%2 != 0):
                pointer = pointer.next
                ind += 1
            else:
                ind += 1
                current.next = ListNode(pointer.val)
                current = current.next
                pointer = pointer.next
                head.next = head.next.next
                if(pointer):
                    head = head.next
        if (temp.next == None):
            return answer
        head.next = temp.next


        return answer

```


### 다른 방법

- 더 짧은 방법 (thanks to Aris94)
- 더 깔끔 (클린코드) 하다.
- 포인터를 만들필요 없이 head 자체를 포인터로 쓴다. (대신 odd리스트를 만들어야 한다)

```python
def oddEvenList(self, head):
    odds = ListNode(0)
    evens = ListNode(0)
    oddsHead = odds
    evensHead = evens
    isOdd = True
    while head:
        if isOdd:
            odds.next = head
            odds = odds.next
        else:
            evens.next = head
            evens = evens.next
        isOdd = not isOdd
        head = head.next
    evens.next = None
    odds.next = evensHead.next
    return oddsHead.next
```
