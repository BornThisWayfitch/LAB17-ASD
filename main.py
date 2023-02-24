import os

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


    def __str__(self):
        return str(self.data)

class BinarySearchTree:
    def __init__(self, expression):
        self.root = None
        self.add(expression)

    def add(self, expression):
        nums = '0123456789'
        num = ''
        token_list = []
        for n in expression:
            if n in nums:
                num+=n
            elif num:
                token_list.append(int(num))
                num = ''
                token_list.append(n)
            else:
                token_list.append(n)

        self.root = self._addToTree(token_list)

    def _addToTree(self, token_list):
        if token_list:
            brackets = 0
            index_sym = 0
            for inx, sym in enumerate(token_list):
                if sym == '(':
                    brackets += 1
                    if brackets == 1:
                        for i in range(len(token_list)):
                            if token_list[i] == ',' and i>=inx:
                                index_sym = i
                                break
                if sym == ')':
                    brackets -= 1
                    if brackets == 1:
                        for i in range(len(token_list)):
                            if token_list[i] == ',' and i>=inx:
                                index_sym = i
                                break

            return Node(token_list[0], self._addToTree(token_list[2:index_sym]),
                        self._addToTree(token_list[index_sym+1:-1]))

    def PreOrder(self):
        self._PreOrder(self.root)

    def _PreOrder(self, node):
        if (node != None):
            print( str(node.data), end= ' ' )
            self._PreOrder(node.left)
            self._PreOrder(node.right)

    def height(self):
        return self._height(self.root)
    def _height(self, node):
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

    def create(self):
        print("================== BinarySearchTree ===================")
        self._create(self.root)
    def _create(self,node, prefix = '', isroot = True, islast = True):
        print(prefix,end='')
        if isroot:
            print('', end='')
        else:
            if islast:
                print('└─', end='')
            else:
                print('├─', end='')
        if node:
            print(node)
        else:
            print('')


        if(not node or (not node.left and not node.right)): return
        line = [node.left, node.right]
        for i in range(len(line)):
            self._create(line[i], prefix + ("" if isroot else ("  " if islast else '│ ')), False, i+1>=len(line))

    def lookup(self, target):
        self._lookup(self.root, target)
    def _lookup(self, node, target):
        if node == None:
            print('К сожалению, данного узла не существует')
            return False
        else:
            if target == node.data:
                print("Информация об узле:")
                print("-Значение:", node)
                print("-Левый потомок:", node.left)
                print("-Правый потомок:", node.right)
                return True
            else:
                if target < node.data: return self._lookup(node.left, target)
                else: return self._lookup(node.right, target)
    def insert(self,data):
        if self.root:
            self._insert(data,self.root)
        else:
            self.root = Node(data)


    def _insert(self,data,node):
        if data < node.data:
            if node.left:
                self._insert(data,node.left)
            else:
                node.left = Node(data)
        else:
            if node.right:
                self._insert(data,node.right)
            else:
                node.right = Node(data)
    # Вспомогательная функция # для поиска узла минимального значения
    def getMinimumData(self, curr):
        while curr.left:
            curr = curr.left
        return curr

    # Функция удаления узла из BST
    def delete(self, data):
        self._delete(self.root, data)
    def _delete(self, node, data):
        parent = None
        curr = node

        while curr and curr.data != data:
            parent = curr

            if data < curr.data:
                curr = curr.left
            else:
                curr = curr.right

        if curr is None:
            return node

        # Случай 1: удаляемый узел не имеет потомков, т. е. это конечный узел.
        if curr.left is None and curr.right is None:

            if curr != node:
                if parent.left == curr:
                    parent.left = None
                else:
                    parent.right = None

            else:
                node = None

        # Случай 2: удаляемый узел имеет двух дочерних элементов
        elif curr.left and curr.right:

            # находит свой неупорядоченный узел-преемник
            successor = self.getMinimumData(curr.right)

            # сохраняет значение преемника
            val = successor.data

            self._delete(node, successor.data)

            # копирует значение преемника в текущий узел
            curr.data = val

        # Случай 3: удаляемый узел имеет только одного потомка
        else:

            # выбирает дочерний узел
            if curr.left:
                child = curr.left
            else:
                child = curr.right


            if curr != node:
                if curr == parent.left:
                    parent.left = child
                else:
                    parent.right = child


            else:
                node = child

        return node

    def main(self):
        self.create()
        print("Список комманд:")
        print(">>S: Поиск нода")
        print(">>I: Добавление нового нода")
        print(">D: Удаление нода")
        print(">E: Выход из программы")
        value = input("Введите букву: ")
        if value == 'S':
            print("\n==========Search===========")
            x = int(input('Введите значение нода: '))
            self.lookup(x)
            self.main()
        elif value == 'I':
            print("\n==========Insert===========")
            x = int(input('Введите значение нода: '))
            self.insert(x)
            self.main()
        elif value == 'D':
            print("\n==========Delete===========")
            x = int(input('Введите значение нода: '))
            self.delete(x)
            self.main()
        elif value == 'E':
            self.create()
            return
        else:
            print("Такой комманды не существует!")
            self.main()

#main
binTree = BinarySearchTree('8(3(1,6(4,7)),10(,14(13,)))')
binTree.main()
