# https://algospot.com/judge/problem/read/TRAVERSAL

def printPostOrder(preorder, inorder):
        if len(preorder) == 0:
            return
        root = preorder[0]
        l_tree = inorder.index(root)
        printPostOrder(preorder[1: l_tree+1], inorder[:l_tree])
        printPostOrder(preorder[l_tree+1:], inorder[l_tree+1:])
        
        print(root, end=' ')

c = int(input())

for _ in range(c):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))

    printPostOrder(preorder, inorder)