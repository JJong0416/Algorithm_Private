import sys
# input = sys.stdin.readline

def preorder(r):
    if r != '.':
        print(r, end='')
        preorder(tree[r][0]) # left
        preorder(tree[r][1]) # right

def inorder(r):
    if r != '.':
        inorder(tree[r][0])
        print(r, end='')
        inorder(tree[r][1])

def postOrder(r):
    if r != '.':
        postOrder(tree[r][0])
        postOrder(tree[r][1])
        print(r, end='')

N = int(input())
tree ={}

for i in range(N):
    root, left, right = map(str,input().split())
    tree[root] = [left,right]

preorder('A')
print()
inorder('A')
print()
postOrder('A')