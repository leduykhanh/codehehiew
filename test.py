totalCrates = 3
truckCapacity = 4
allLocations = [[1,2], [3,4], [-1,1]]
def closestLocations(totalCrates, allLocations, truckCapacity):
    if truckCapacity >= totalCrates:
        return allLocations
    sorted_by_distance = sorted(allLocations, key=lambda cord: cord[0] ** 2 + cord[1] ** 2)
    return sorted_by_distance[:truckCapacity]

#print(closestLocations(totalCrates, allLocations, truckCapacity))
# sorted_by_distance = sorted(allLocations, key=lambda cord: cord[0]**2 + cord[1]**2)
#print(sorted_by_second[:2])

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val

def binary_insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.left is None:
                root.left = node
            else:
                binary_insert(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                binary_insert(root.right, node)

def path_to_node(root, path, k):

    if root is None:
        return False

    path.append(root.data)

    if root.data == k :
        return True

    if ((root.left is not None and path_to_node(root.left, path, k)) or
            (root.right is not None and path_to_node(root.right, path, k))):
        return True
    path.pop()
    return False

def distance(root, data1, data2):
    if root:
        path1 = []
        path_to_node(root, path1, data1)

        path2 = []
        path_to_node(root, path2, data2)

        i = 0
        while i < len(path1) and i < len(path2):
            if path1[i] != path2[i]:
                break
            i += 1
        return len(path1) + len(path2) - 2*i
    else:
        return 0

def in_order_print(root):
    if not root:
        return
    in_order_print(root.left)
    print (root.data)
    in_order_print(root.right)

def pre_order_print(root):
    if not root:
        return
    print (root.data)
    pre_order_print(root.left)
    pre_order_print(root.right)


root=Node(5)

a=[5,6,3,1,2,4]
n=6
for i in range(1,n):
    binary_insert(root, Node(a[i]))
# print(distance(root, 2,4))
def bstDistance(values, n, node1, node2):
    if node1 not in values or node2 not in values:
        return -1
    root = Node(values[0])
    for i in range(1, n):
        binary_insert(root, Node(values[i]))
    return distance(root, node1, node2)

print(bstDistance(a, n , 2, 4))
