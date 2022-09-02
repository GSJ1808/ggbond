---
title: 230. Kth Smallest Element in a BST
categories: Tree
---
# 230. Kth Smallest Element in a BST

Tags: Depth-First Search
link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# 题目

Given the `root` of a binary search tree, and an integer `k`, return *the* `kth` *smallest value (**1-indexed**) of all the values of the nodes in the tree*.

给定二叉搜索树的根和一个整数 k，返回树中所有节点值的第 k 个最小值（从 1 开始）。

## **Example 1:**

![kthtree1.jpg](230%20Kth%20Smallest%20Element%20in%20a%20BST%20a8e2da571fd640fdb2078ee3792edd73/kthtree1.jpg)

```
Input: root = [3,1,4,null,2], k = 1
Output: 1
```

## **Example 2:**

![kthtree2.jpg](230%20Kth%20Smallest%20Element%20in%20a%20BST%20a8e2da571fd640fdb2078ee3792edd73/kthtree2.jpg)

```
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
```

# 解题思路

该题要求输出第k个最小值。中序遍历可以将BST升序遍历，因此每遍历一个节点就对该节点进行编号，当该节点的编号和k相同时，节点的值是第k个最小值。

```cpp
class Solution {
public:
    void inorder(TreeNode* node,int& res,int& k,int& i)
    {
        if(!node) return;
        inorder(node->left,res,k,i);
        if(++i == k) res = node->val;
        inorder(node->right,res,k,i);
    }
    int kthSmallest(TreeNode* root, int k) {
        int res = 0;
        int i = 0;
        inorder(root,res,k,i);
        return res;
    }
};
```