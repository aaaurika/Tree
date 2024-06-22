class SimpleTreeNode:
    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов


class SimpleTree:
    def __init__(self, root):
        self.Root = root  # корень, может быть None

    def AddChild(self, ParentNode, NewChild):
        # Добавляем новый дочерний узел существующему ParentNode
        ParentNode.Children.append(NewChild)
        NewChild.Parent = ParentNode
        # Проверка: узел добавлен
        assert NewChild in ParentNode.Children, "Узел не добавлен"
        self._print_tree()

    def DeleteNode(self, NodeToDelete):
        # Удаление узла и его потомков
        if NodeToDelete.Parent:
            NodeToDelete.Parent.Children.remove(NodeToDelete)
        NodeToDelete.Parent = None
        # Проверка: узел удален, потомки тоже
        assert NodeToDelete not in self.GetAllNodes(), "Узел не удален"
        self._print_tree()

    def GetAllNodes(self):
        nodes = []
        def _dfs(node):
            nodes.append(node.NodeValue)
            for child in node.Children:
                _dfs(child)
        _dfs(self.Root)
        return nodes if self.Root else []

    def FindNodesByValue(self, val):
        # Поиск узлов по значению
        return [node for node in self.GetAllNodes() if node.NodeValue == val]

    def Count(self):
        # Количество всех узлов в дереве
        return len(self.GetAllNodes())

    def _print_tree(self):
        print(f"Текущее дерево: {self.GetAllNodes()}")

#  корневой узел
root = SimpleTreeNode(1, None)

#  дерево
tree = SimpleTree(root)

# Добавляем дочерние узлы
node2 = SimpleTreeNode(2, root)
node3 = SimpleTreeNode(3, root)
tree.AddChild(root, node2)
tree.AddChild(root, node3)

# внуки
node4 = SimpleTreeNode(4, node2)
node5 = SimpleTreeNode(5, node3)
tree.AddChild(node2, node4)
tree.AddChild(node3, node5)

# Удаляем узел
tree.DeleteNode(node4)

