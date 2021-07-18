# Number of Islands

### 문제설영

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water. (leetcode 200)

ex)
- Input: grid = [
          ["1","1","1","1","0"],
          ["1","1","0","1","0"],
          ["1","1","0","0","0"],
          ["0","0","0","0","0"]
        ]
- Output: 1


### DFS with recursion

recursion을 이용하여 DFS 검색을 한다.
주변의 연결부를 모두 검색하여 1일 경우 체크 해준다.

```python
def dfs(self,grid,i,j):
    if (i<0 or j<0 or i>=len(grid) or j>=len(grid[0])) or grid[i][j] != '1':
        return
    grid[i][j] = '#'
    self.dfs(grid,i+1,j)
    self.dfs(grid,i-1,j)
    self.dfs(grid,i, j+1)
    self.dfs(grid,i, j-1)
```


### 전체 코드

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    self.dfs(grid,i,j)
                    count += 1
        return count
    def dfs(self,grid,i,j):
        if (i<0 or j<0 or i>=len(grid) or j>=len(grid[0])) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid,i+1,j)
        self.dfs(grid,i-1,j)
        self.dfs(grid,i, j+1)
        self.dfs(grid,i, j-1)
```


### 다른 풀이

map function 을 이용하여 단계를 생략하였다.

```python
def numIslands(self, grid):
    def sink(i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
            grid[i][j] = '0'
            map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1))
            return 1
        return 0
    return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))
```
