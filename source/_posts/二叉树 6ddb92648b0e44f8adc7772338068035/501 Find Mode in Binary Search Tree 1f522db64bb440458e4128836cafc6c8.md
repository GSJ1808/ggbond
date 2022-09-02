---
title: 501. Find Mode in Binary Search Tree
categories: Tree
---
# 501. Find Mode in Binary Search Tree

Tags: Breadth-First Search, Depth-First Search
link: https://leetcode.com/problems/find-mode-in-binary-search-tree/

# 题目

Given the `root` of a binary search tree (BST) with duplicates, return *all the [mode(s)](https://en.wikipedia.org/wiki/Mode_(statistics)) (i.e., the most frequently occurred element) in it*.

If the tree has more than one mode, return them in **any order**.

Assume a BST is defined as follows:

- The left subtree of a node contains only nodes with keys **less than or equal to** the node's key.
- The right subtree of a node contains only nodes with keys **greater than or equal to** the node's key.
- Both the left and right subtrees must also be binary search trees.

给定具有重复项的二叉搜索树 (BST) 的根，返回其中的所有众数（即最常出现的元素）。
如果树有多个众数，则以任意顺序返回它们。
假设 BST 定义如下：
节点的左子树仅包含键小于或等于节点键的节点。
节点的右子树仅包含键大于或等于节点键的节点。
左右子树也必须是二叉搜索树。

## **Example 1:**

```
Input: root = [1,null,2,2]
Output: [2]
```

## **Example 2:**

```
Input: root = [0]
Output: [0]
```

# 解题思路

使用DFS遍历节点，并用一个map记录每一个节点出现的次数。

```cpp
class Solution {
public:
    map<int,int> mode;
    void helper(TreeNode *node)
    {
        if(!node)return;
        ++mode[node->val];
        if(node->left)helper(node->left);
        if(node->right)helper(node->right);
    }
    vector<int> findMode(TreeNode* root) {
        helper(root);
        int max_vaule=mode[root->val];
        for(auto a:mode)
        {
            max_vaule=max(a.second,max_vaule);
        }
        vector<int> res;
        for(auto a:mode)
        {
            if(a.second == max_vaule)
            res.push_back(a.first);
        }
        return res;
    }
};
```