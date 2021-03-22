"""
Так как условие задачи не обговорено и обходов деревьев существует много и для различных целей,
я решил написать типа BFS для поиска пути от одной вершины дерева к другой в дереве заданном списками смежности
"""


def tree_search(tree, node1, node2):
    """
    Determine path from node to node in tree, if it exists

    Keyword arguments:
    tree - tree given by adjacency list
    node1 - source node
    node2 - destination node

    Prints:
    path from node1 to node2, or 'Пути нет' if path doesn't exist
    """
    mark = set()
    root = node1
    path = {}
    queue = [root]
    while len(queue) > 0:
        parent = queue.pop(0)
        mark.add(parent)
        for node in tree.get(parent):
            if node not in mark:
                path[node] = parent
                queue.append(node)
            if node == node2:
                item = node
                print(item)
                while item != node1:
                    print(path.get(item))
                    item = path.get(item)
                return
    print('Пути нет')
    return


tree = {
    1: [2, 5, 7],
    2: [1, 3, 6],
    3: [2, 4, 5],
    4: [3, 7],
    5: [1, 3, 6],
    6: [2, 5],
    7: [1, 4],
    8: [9],
    9: [8]
}


tree_search(tree, 8, 9)
