"""
Tree in Python
Adapted from Youtube codebasics 
Title: "Tree (General Tree) - Data Structures & Algorithms Tutorials In Python #9"
URL: https://youtu.be/4r_XR9fUPhQ
"""

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = [] # Each element in list in an instance of TreeNode class
        self.parent = None

    def __str__(self):
        return self.data + " | Parent: " + self.parent.data + " | Children: [" + ", ".join([child.data for child in self.children]) + "]"

    def add_child(self, child):
        child.parent = self # Parent of new node is the current node
        self.children.append(child)

    def get_level(self):
        level = 0
        parent = self.parent
        while parent:
            level += 1
            parent = parent.parent
        return level

    def print_tree(self):
        prefix = ' ' * self.get_level() * 3 + "|--" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()




def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)
    
    return root




if __name__ == "__main__":
    root = build_product_tree()
    root.print_tree()
    print(str(root.children[0]))
    

