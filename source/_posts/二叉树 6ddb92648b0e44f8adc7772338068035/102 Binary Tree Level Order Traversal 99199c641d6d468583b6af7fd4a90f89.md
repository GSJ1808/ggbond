---
title: 102. Binary Tree Level Order Traversal
categories: Tree
---
# 102. Binary Tree Level Order Traversal

Tags: Breadth-First Search, Depth-First Search
link: https://leetcode.com/problems/binary-tree-level-order-traversal/

# 题目

Given the `root`of a binary tree, return *the level order traversal of its nodes' values*. (i.e., from left to right, level by level).

给定二叉树的根，返回其节点值的级别顺序遍历。 （即从左到右，逐级）。

## **Example 1:**

![tree1.jpg](102%20Binary%20Tree%20Level%20Order%20Traversal%2099199c641d6d468583b6af7fd4a90f89/tree1.jpg)

```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
```

## **Example 2:**

```
Input: root = [1]
Output: [[1]]
```

# 解题思路

该题的解题思路和**[637. Average of Levels in Binary Tree](637%20Average%20of%20Levels%20in%20Binary%20Tree%203a05327e6d5541eabb45a2e27526bdeb.md)** 一样，可以通过DFS、BFS两种方法进行求解。

```cpp
class Solution {
public:
    void DFS(TreeNode* node, int height, vector<vector<int>> &res)
    {
        if(!node)return;
        if(res.size() < height)
        {
            res.push_back(vector<int>{node->val});
        }
        else res[height - 1].push_back(node->val);
        DFS(node->left,height+1,res);
        DFS(node->right,height+1,res);
    }
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        DFS(root,1,res);
        return res;
    }
};
```