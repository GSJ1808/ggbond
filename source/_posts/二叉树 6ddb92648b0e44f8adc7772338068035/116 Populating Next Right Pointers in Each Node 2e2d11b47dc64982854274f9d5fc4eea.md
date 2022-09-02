---
title: 116. Populating Next Right Pointers in Each Node
categories: Tree
---
# 116. Populating Next Right Pointers in Each Node

Tags: Breadth-First Search
link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

# 题目

You are given a **perfect binary tree** where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

```cpp
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
```

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to `NULL`.

Initially, all next pointers are set to `NULL`.

给你一棵完美的二叉树，其中所有叶子都在同一级别，每个父母都有两个孩子。二叉树的定义如下：

```cpp
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
```

填充每个 next 指针以指向其下一个右节点。如果没有下一个右节点，则下一个指针应设置为 NULL。
最初，所有下一个指针都设置为 NULL。

## **Example 1:**

![116_sample.png](116%20Populating%20Next%20Right%20Pointers%20in%20Each%20Node%202e2d11b47dc64982854274f9d5fc4eea/116_sample.png)

```
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
```

## **Example 2:**

```
Input: root = []
Output: []
```

# 解题思路

首先对该树进行BFS遍历，将队列中的元素都用next指针相连。这样每一层的元素能练到了一起，最后一个元素也与下一层的第一个元素也相连了。

因此将每一层的最后一个元素的next元素置空即可。

```cpp
class Solution {
public:
    Node* connect(Node* root) {
        if (!root)
            return nullptr;
        queue<Node*> node;
        Node *pre = new Node(),*cur;
        node.push(root);
        while (!node.empty())
        {
            cur = node.front();
            node.pop();
            if (cur->left)
                node.push(cur->left);
            if(cur->right) node.push(cur->right);
            
            pre->next = cur;
            pre = cur;
        }
        pre = root;
        while(pre)
        {
            pre->next = nullptr;
            pre = pre->right;
        }
        return root;
    }
};
```