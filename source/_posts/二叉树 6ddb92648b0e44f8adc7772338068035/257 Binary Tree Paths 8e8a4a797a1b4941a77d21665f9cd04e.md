---
title: 257. Binary Tree Paths
categories: Tree
---
# 257. Binary Tree Paths

Tags: Backtracking, Depth-First Search
link: https://leetcode.com/problems/binary-tree-paths/

# 题目

Given the `root` of a binary tree, return *all root-to-leaf paths in **any order***.

A **leaf** is a node with no children.

给定二叉树的根，以任意顺序返回所有从根到叶的路径。
叶是没有子节点的节点。

## **Example 1:**

```
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
```

## **Example 2:**

```
Input: root = [1]
Output: ["1"]
```

# 解题思路

玩树的题目，十有八九都是递归，而递归的核心就是不停的 DFS 到叶结点，然后在回溯回去。在递归函数中，当遇到叶结点的时候，即没有左右子结点，那么此时一条完整的路径已经形成了，加上当前的叶结点后存入结果 res 中，然后回溯。注意这里结果 res 需要 reference，而 out 是不需要引用的，不然回溯回去还要删除新添加的结点，很麻烦。为了减少判断空结点的步骤，我们在调用递归函数之前都检验一下非空即可，代码而很简洁，参见如下：

```cpp
class Solution {
public:
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> res;
        helper(root,"",res);
        return res;
    }
    void helper(TreeNode* node,string out,vector<string>& res)
    {
        if(!node)return;
        if(!node->left and !node->right) res.push_back(out + to_string(node->val));
        if(node->left)helper(node->left,out+to_string(node->val)+"->",res);
        if(node->right)helper(node->right,out+to_string(node->val)+"->",res);
    }
};
```