---
title: 98. Validate Binary Search Tree
categories: Tree
---
# 98. Validate Binary Search Tree

Tags: recursion
link: https://leetcode.com/problems/validate-binary-search-tree/

# 题目

Given the `root` of a binary tree, *determine if it is a valid binary search tree (BST)*.

A **valid BST** is defined as follows:

- The left subtree of a node contains only nodes with keys **less than** the node's key.
- The right subtree of a node contains only nodes with keys **greater than** the node's key.
- Both the left and right subtrees must also be binary search trees.

给定二叉树的根，确定它是否是有效的二叉搜索树 (BST)。
有效的 BST 定义如下：
节点的左子树仅包含键小于节点键的节点。
节点的右子树只包含键大于节点键的节点。
左右子树也必须是二叉搜索树。

## **Example 1:**

![tree1.jpg](98%20Validate%20Binary%20Search%20Tree%205f34a97bb1bc4a339b5055beafd68e1d/tree1.jpg)

```
Input: root = [2,1,3]
Output: true
```

## **Example 2:**

![tree2.jpg](98%20Validate%20Binary%20Search%20Tree%205f34a97bb1bc4a339b5055beafd68e1d/tree2.jpg)

```
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
```

# 解题思路

该题可以用递归法来求解，首先判断左右两科子树是否都是BST。然后判断根节点的值是否大于左子树的最大值和是否小于右子树的最小值。

```cpp
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        if(!root)return true;
        bool left = isValidBST(root->left);
        bool right = isValidBST(root->right);
        TreeNode* max = root->left;
        TreeNode* min = root->right;
        if(max)
        {
            while (max->right)
            {
                max = max->right;
            }
            
        }
        if(min)
        {
            while (min->left)
            {
                min = min->left;
            }
            
        }
        if(root->left and root->right)
        {
            return right and left and
            root->val > max->val and
            min->val > root -> val;
        }
        else if(root->left)
        {
            return right and left and
            root->val > max->val;
        }
        else if(root->right)
        {
            return right and left and
            min->val > root->val;
        }
        else return true;
        
    }
};
```

解法2：用一个vector来保存中序遍历之后的结果，判断该vector是否是严格递增的。

```cpp
// Recursion
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        if (!root) return true;
        vector<int> vals;
        inorder(root, vals);
        for (int i = 0; i < vals.size() - 1; ++i) {
            if (vals[i] >= vals[i + 1]) return false;
        }
        return true;
    }
    void inorder(TreeNode* root, vector<int>& vals) {
        if (!root) return;
        inorder(root->left, vals);
        vals.push_back(root->val);
        inorder(root->right, vals);
    }
};
```

解法3：也是利用BST的性质

```cpp
// Recursion without inorder traversal
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        return isValidBST(root, LONG_MIN, LONG_MAX);
    }
    bool isValidBST(TreeNode* root, long mn, long mx) {
        if (!root) return true;
        if (root->val <= mn || root->val >= mx) return false;
        return isValidBST(root->left, mn, root->val) && isValidBST(root->right, root->val, mx);
    }
};
```