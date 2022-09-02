---
title: 199. Binary Tree Right Side View
categories: Tree
---
# 199. Binary Tree Right Side View

Tags: Breadth-First Search
link: https://leetcode.com/problems/binary-tree-right-side-view/

# 题目

Given the `root` of a binary tree, imagine yourself standing on the **right side** of it, return *the values of the nodes you can see ordered from top to bottom*.

给定二叉树的根，想象你站在它的右边，返回你可以看到从上到下排列的节点的值。

## **Example 1:**

![tree.jpg](199%20Binary%20Tree%20Right%20Side%20View%20c7b66489352746a99c453e4ee4b720c6/tree.jpg)

```
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
```

## **Example 2:**

```
Input: root = [1,null,3]
Output: [1,3]
```

# 解题思路

该题可以使用BFS遍历，然后将每一层的最后元素添加到结果中即可。

```cpp
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> res;
        if(!root) return res;
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty())
        {
            int N = q.size();
            for (size_t i = 0; i < N; i++)
            {
                auto tmp = q.front();
                q.pop();
                if(tmp->left)q.push(tmp->left);
                if(tmp->right)q.push(tmp->right);
                if(i == N-1) res.push_back(tmp->val);
            }
        }
        return res;
    }
};
```