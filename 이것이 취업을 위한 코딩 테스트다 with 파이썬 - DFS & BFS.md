# 이것이 취업을 위한 코딩 테스트다 with 파이썬 - DFS & BFS

- 스택 (LIFO)

```python
stack = [] 

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)

print(stack[::-1]) #최상단 원소부터 출력
print(stack)  # 최하단 원소부터 출력
```



- 큐 (FIFO)

```python
from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력
```



- 재귀 함수 : 자기 자신을 다시 호출하는 함수

```python
def recursive_function():
	print("재귀 함수 호출")
	recursive_function()
```

종료 조건 명시

```python
def recursive_function(i):
    if i == 100:
        return
	print(i,"재귀함수에서",(i+1)"재귀함수를 호출합니다.")
	recursive_function(i+1)
```



- 팩토리얼 구현 예제

  n! = 1 * 2 * 3 * ... * (n-1) * n

```python
def factorial_iterative(n):
    resut = 1
    
    for 1 in range(1, n+1):
        result *= u
    return result

def factorial_recursive(n):
    if n <= 1:
        return 1
    
    return n * factorial_recursive(n-1)
```



- dfs

```python
# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end = ' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            
# 각 노드가 연결된 정보를 표현 (2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]  
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
```

실행 결과 

1 2  7 6 8 3 4 5

![image-20201217204032164](C:\Users\3kist_000\AppData\Roaming\Typora\typora-user-images\image-20201217204032164.png)



- BFS

```python
from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v, end=' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
# 각 노드가 연결된 정보를 표현 (2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]  
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)

1 2 3 8 7 4 5 6
```



https://www.youtube.com/watch?v=PqzyFDUnbrY&list=PLRx0vPvlEmdBFBFOoK649FlEMouHISo8N&index=3