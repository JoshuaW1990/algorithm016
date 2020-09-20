# 学习笔记

## 第二周课程

### 第五课 哈希表、映射、集合

- 概念
    - 哈希函数
    - 哈希表
- 工程实践：LRU cache、Redis
- hash collision
    - 链表解决
- 时间复杂度
    - 查询、插入、删除：O(1)



### 第六课 树、二叉树、二叉搜索树

#### 二叉树遍历

- 前序遍历：中左右
- 中序遍历：左中右
- 后续遍历：左右中

代码模板：

三种遍历方式仅需调整遍历顺序, 以中序遍历为例

迭代: 基于DFS迭代
```python
def do_somthing(node):
    pass

def dfs(node):
    if node is None:
        return
    dfs(node.left)
    do_somthing(node)
    dfs(node.right)
```
递归：基于DFS递归+色彩标记stack节点, 注意递归的时候节点插入顺序要反过来
```python
def do_something(node):
    pass

def dfs(root):
    stack = [(1, root)]
    while len(stack) > 0:
        color, node = stack.pop()
        if node is None:
            continue
        if color == 1:
            stack.append((1, node.right))
            stack.append((0, node))
            stack.append((1, node.left))
        else:
            do_something(node)
```

#### 二叉搜索树
1. 空树是二叉搜索树
2. 左子树所有节点小于根节点，右子树所有节点大于根节点

常见操作：插入、删除、查询

复杂度：均为O(logN)


### 第六课 堆和二叉堆

- 大根堆
- 小根堆

常见操作:
- find-max: O(1)
- delete-max: O(logN)
- insert-max: O(logN) or O(1)

性质：
1. 是完全树
2. 任意节点值大于（或小于）子节点值

二叉堆：通过数组实现
- 左子节点index: `2i+1`
- 右子节点index: `2i+2`
- 父节点index: `floor((i-1)/2)`


### 第六课 图

DFS算法与BFS算法

DFS
```python
visited = set()
def do_something(node):
    pass

def dfs(node):
    if node in visited:
        return
    visited.add(node)
    do_something(node)
    for ch in node.children:
        dfs(ch)
```

BFS
```python
def do_something(node):
    pass

def bfs(start):
    queue = []
    queue.append(start)
    visited = set()
    while len(queue) > 0:
        node = queue.pop(0)
        if node in visited:
            continue
        visited.add(node)
        do_something(node)
        for ch in node.childre:
            queue.append(ch)
```