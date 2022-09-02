---
title: 637. Average of Levels in Binary Tree
categories: Tree
---
# 637. Average of Levels in Binary Tree

Tags: Backtracking, Breadth-First Search, Depth-First Search
link: https://leetcode.com/problems/average-of-levels-in-binary-tree/

# 题目

Given the `root`of a binary tree, return *the average value of the nodes on each level in the form of an array* Answers within `10-5`of the actual answer will be accepted.

给定二叉树的根，以数组的形式返回每一层节点的平均值。将接受实际答案 10-5 以内的答案。

## **Example 1:**

![avg1-tree.jpg](637%20Average%20of%20Levels%20in%20Binary%20Tree%203a05327e6d5541eabb45a2e27526bdeb/avg1-tree.jpg)

```
Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].
```

## **Example 2:**

![avg2-tree.jpg](637%20Average%20of%20Levels%20in%20Binary%20Tree%203a05327e6d5541eabb45a2e27526bdeb/avg2-tree.jpg)

```
Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]
```

# 解题思路

DSF

通过DFS遍历节点，并用map记录每一层的节点值sum和节点的个数。

```cpp
class Solution
{
public:
    map<int, double> height_sum;
    map<int, int> height_num;
    int height = 0;
    void inorder(TreeNode *node)
    {
        if (!node)
            return;
        height++;
        if (node->left)
            inorder(node->left);
        height_sum[height] += node->val;
        height_num[height]++;
        if (node->right)
            inorder(node->right);
        height--;
    }
    vector<double> averageOfLevels(TreeNode *root)
    {
        inorder(root);
        vector<double> res;
        for (auto average : height_sum)
        {
            res.push_back(average.second / height_num[average.first]);
        }
        return res;
    }
};
```

BFS

```cpp
class Solution {
public:
    vector<double> averageOfLevels(TreeNode* root) {
        queue<TreeNode*> q;
        vector<double> res;
        double temp;
        int size, i;
        TreeNode* curr;
        
        q.push(root);
        
        while (!q.empty()) {
            temp = 0;
            size = q.size();
            
            for (i = 0; i < size; i++) {
                
                curr = q.front();
                q.pop();
                
                if (curr->left) q.push(curr->left);
                if (curr->right) q.push(curr->right);
                
                temp += curr->val;
            }
            
            res.push_back((double)temp / size);
        }
        
        return res;
    }
};
```