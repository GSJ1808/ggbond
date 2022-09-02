---
title: 938. Range Sum of BST
categories: Tree
---
# 938. Range Sum of BST

Tags: Depth-First Search
link: https://leetcode.com/problems/range-sum-of-bst/

# 题目

Given the `root`node of a binary search tree and two integers `low`and `high`, return *the sum of values of all nodes with a value in the **inclusive** range* `[low, high`.

给定二叉搜索树的根节点和两个整数 low 和 high，返回包含范围 [low, high] 内的所有节点的值之和。

## **Example 1:**

![bst1.jpg](938%20Range%20Sum%20of%20BST%20cb87f07a66d84ff0a9047eae8b90b9ba/bst1.jpg)

```
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
```

## **Example 2:**

![bst2.jpg](938%20Range%20Sum%20of%20BST%20cb87f07a66d84ff0a9047eae8b90b9ba/bst2.jpg)

```
Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
```

# 解题思路

使用DFS遍历每一个节点，如果该节点值在区间范围内，那么久将该值加到结果上。

```cpp
class Solution {
public:
    void inorder(TreeNode* node,int&res,int low,int high)
    {
        if(!node)return;
        if(node->left)inorder(node->left,res,low,high);
        if(node->val >= low and high >= node->val) res+=node->val;
        if(node->right)inorder(node->right,res,low,high);
    }
    int rangeSumBST(TreeNode* root, int low, int high) {
        int res = 0;
        inorder(root,res,low,high);
        return res;
    }
};
```