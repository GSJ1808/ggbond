---
title: 117. Populating Next Right Pointers in Each Node II
categories: Tree
---
# 117. Populating Next Right Pointers in Each Node II

Tags: Breadth-First Search
link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

# 题目

Given a binary tree

```
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

```

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to `NULL`.

Initially, all next pointers are set to `NULL`.

## **Example 1:**

![117_sample.png](117%20Populating%20Next%20Right%20Pointers%20in%20Each%20Node%20II%20c2df4935bd9147fb8600bb18e88b6ecd/117_sample.png)

```
Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
```

## **Example 2:**

```
Input: root = []
Output: []
```

# 解题思路

使用BFS遍历，将每一层的结点用next指针相连。

```cpp
class Solution
{
public:
    Node *connect(Node *root)
    {
        if(!root) return root;
        queue<Node *> q;
        q.push(root);
        while (!q.empty())
        {
            int N = q.size();
            Node *pre = new Node();
            for (size_t i = 0; i < N; i++)
            {
                Node *tmp = q.front();
                q.pop();
                if (i > 0)
                {
                    pre->next = tmp;
                }
                pre = tmp;
                if (tmp->left)
                    q.push(tmp->left);
                if (tmp->right)
                    q.push(tmp->right);
            }
        }
        return root;
    }
};
```