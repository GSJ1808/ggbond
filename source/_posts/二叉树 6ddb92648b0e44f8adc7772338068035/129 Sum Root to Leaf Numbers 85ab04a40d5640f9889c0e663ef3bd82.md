---
title: 129. Sum Root to Leaf Numbers
categories: Tree
---
# 129. Sum Root to Leaf Numbers

Tags: Depth-First Search

# 题目

You are given the `root` of a binary tree containing digits from `0` to `9` only.

Each root-to-leaf path in the tree represents a number.

- For example, the root-to-leaf path `1 -> 2 -> 3` represents the number `123`.

Return *the total sum of all root-to-leaf numbers*. Test cases are generated so that the answer will fit in a **32-bit** integer.

A **leaf** node is a node with no children.

## **Example 1:**

![num1tree.jpg](129%20Sum%20Root%20to%20Leaf%20Numbers%2085ab04a40d5640f9889c0e663ef3bd82/num1tree.jpg)

```
Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
```

## **Example 2:**

![num2tree.jpg](129%20Sum%20Root%20to%20Leaf%20Numbers%2085ab04a40d5640f9889c0e663ef3bd82/num2tree.jpg)

```
Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
```

# 解题思路

解法同**[257. Binary Tree Paths](257%20Binary%20Tree%20Paths%208e8a4a797a1b4941a77d21665f9cd04e.md)。257**是求出所有的二叉树路径，该题只用在257的基础上将其转换为数字即可。

```cpp
class Solution {
public:
    void DFS(TreeNode* node, int& res, int out)
    {
        if(!node)return;
        out *= 10;
        out+=node->val;
        if (!node->left and !node->right) res += out;
        DFS(node->left,res,out);
        DFS(node->right,res,out);
    }
    int sumNumbers(TreeNode* root) {
        int res = 0;
        DFS(root,res,0);
        return res;
    }
};
```