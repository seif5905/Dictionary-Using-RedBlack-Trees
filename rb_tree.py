from node import Node

def insert(root: Node | None, data) -> Node:
    new_node = Node(data)

    if root == None: # if tree empty, new node is root
        new_node.color = "black"
        return new_node
    
    current = root
    parent = None
    while current != None:
        parent = current
        if data < current.data:
            current = current.l_child
        elif data > current.data:
            current = current.r_child
        else:
            return root # if number is a duplicate
        
    new_node.parent = parent
    if data < parent.data:
        parent.l_child = new_node
    elif data > parent.data:
        parent.r_child = new_node

    return fix_insert(root, new_node)

def fix_insert(root: Node, node: Node) -> Node:

    while node != root and node.parent != None and node.parent.color == "red":

        p = node.parent
        gp = p.parent

        if gp and gp.l_child == p: # if parent is left child of grandparent
            uncle = gp.r_child
            
            if uncle and uncle.color == "red":
                uncle.color = "black"
                p.color = "black"
                gp.color = "red"
                node = gp

            else:
                if p.l_child == node:
                    root = rotate_r(root, gp)
                elif p.r_child == node:
                    root = rotate_l(root, p)
                    root = rotate_r(root, gp)

                root.color = "black"
                gp.color = "red"
                break

        else: # if parent is right child of grandparent
            uncle = gp.l_child
            
            if uncle and uncle.color == "red":
                uncle.color = "black"
                p.color = "black"
                gp.color = "red"
                node = gp

            else:
                if p.l_child == node:
                    root = rotate_r(root, p)
                    root = rotate_l(root, gp)
                elif p.r_child == node:
                    root = rotate_l(root, gp)
                
                root.color = "black"
                gp.color = "red"
                break

    root.color = "black"
    return root

def rotate_l(root: Node, x: Node) -> Node:
    
    y = x.r_child
    y.l_child = x.r_child
    x.r_child.parent = y.l_child
    y.parent = x.parent
    gp = x.parent
    if gp.l_child == x.parent:
        gp.l_child = y
    else:
        gp.r_child = y
    y.l_child = x
    x.parent = y
    
    return y
    

def rotate_r(root: Node, x: Node) -> Node:
    pass

def search(root: Node, data) -> Node | None:
    current = root
    while current != None:
        if data < current.data:
            current = current.l_child
        elif data > current.data:
            current = current.r_child
        else:
            return current
    return None

def get_height(root: Node):
    if root != None:
        x = get_height(root.r_child)
        y = get_height(root.l_child)
        if x > y:
            return x + 1
        else:
            return y + 1
    return 0

def get_size(root: Node):
    if root != None:
        x = get_size(root.r_child)
        y = get_size(root.l_child)
        return x + y + 1
    return 0

def get_black_height(root: Node):
    current = root
    black_height = 0
    while current != None:
        if current.color == "black":
            black_height += 1
        current = current.l_child
    return black_height
    