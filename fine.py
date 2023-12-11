# Реалізуйте базу даних зі штрафами податкової
# інспекції. Ідентифікувати кожну конкретну людину буде
# персональний ідентифікаційний код. В однієї людини може
# бути багато штрафів.
# Реалізуйте:
# 1. Повний друк бази даних;
# 2. Друк даних за конкретним кодом;
# 3. Друк даних за конкретним типом штрафу;
# 4. Друк даних за конкретним містом;
# 5. Додавання нової людини з інформацією про неї;
# 6. Додавання нових штрафів для вже існуючого запису;
# 7. Видалення штрафу;
# 8. Заміна інформації про людину та її штрафи.
# Використайте дерево для реалізації цього завдання.

class TreeNode:
    id = 1
    def __init__(self, id, city, fines: list) -> None:
        self.id = id
        self.city = city
        self.fines = fines
        self.right = None
        self.left = None


class FinesTree:
    def __init__(self) -> None:
        self.root = None
    
    def add_person(self, city, fines: list):
        id = TreeNode.id
        TreeNode.id += 1
        if not self.root:
            self.root = TreeNode(id, city, fines)
        else:
            self._add_person(self.root, id, city, fines)

    def _add_person(self, node, id, city, fines):
        if id < node.id:
            if node.left is None:
                node.left = TreeNode(id, city, fines)
            else: 
                self._add_person(node.left, id, city, fines)
        elif id > node.id:
            if node.right is None:
                node.right = TreeNode(id, city, fines)
            else:
                self._add_person(node.right, id, city, fines)
    
    def change_info(self, id, city, fines:list):
        node = self._print_fines_by_id(self.root, id ,prnt_info=False)
        if node:
            node.city = city
            node.fines = fines
        else:
            print("person not found")
        

    def add_fine(self, id, fine):
        node = self._print_fines_by_id(self.root, id, prnt_info=False)
        if node:
            node.fines.append(fine)
            print(f"ID: {node.id}, City: {node.city}, Fines: {node.fines}")
        else:
            print("person not found")
    
    def remove_fine(self, id, fine):
        if not self.root:
            print("Database is empty.")
        else:
            node = self._print_fines_by_id(self.root, id, prnt_info=False)
            if node:
                node.fines.remove(fine)
                print(f"ID: {node.id}, City: {node.city}, Fines: {node.fines}")
            else:
                print("person not found")
    
    def print_database(self):
        if not self.root:
            print("Database is empty.")
        else:
            self._print_database(self.root)

    def _print_database(self, node):
        if node:
            self._print_database(node.left)
            print(f"ID: {node.id}, City: {node.city}, Fines: {node.fines}")
            self._print_database(node.right)
    
    def print_fines_by_id(self, id):
        if not self.root:
            print("Database is empty.")
        else:
            self._print_fines_by_id(self.root, id)


    def _print_fines_by_id(self, node, id, prnt_info=True):
        if not node or node.id == id:
            if prnt_info:
                print(f"ID: {node.id}, City: {node.city}, Fines: {node.fines}")
            else:
                return node
        elif id < node.id:
            return self._print_fines_by_id(node.left, id, prnt_info)
        else:
            return self._print_fines_by_id(node.right, id, prnt_info)

    def print_by_fine_type(self, fine_type):
        if not self.root:
            print("Database is empty.")
        else:
            self._print_by_fine_type(self.root, fine_type)

    def _print_by_fine_type(self, node, fine_type):
        if node:
            self._print_by_fine_type(node.left, fine_type)
            if fine_type in node.fines:
                print(f"ID: {node.id}, City: {node.city}, Fines: {node.fines}")
            self._print_by_fine_type(node.right, fine_type)

    def print_by_city(self, city):
        if not self.root:
            print("Databse is empty")
        else:
            self._print_by_city(self.root, city)
    
    def _print_by_city(self, node, city):
        if node:
            self._print_by_city(node.left, city)
            if node.city == city:
                print(f"ID: {node.id}, City: {node.city}, Fines: {node.fines}")
            self._print_by_city(node.right, city)

fines_db = FinesTree()

fines_db.add_person("Paris", ["Speeding", "Parking"])
fines_db.add_person("Madrid", ["Jaywalking"])
fines_db.add_person("Paris", ["Parking", "Noise violation"])
fines_db.add_person("Madrid", ["Parking", "Jaywalking"])
fines_db.add_person("Krakow", ["Smoking", "Jaywalking"])
print()
fines_db.print_fines_by_id(1)
print()
fines_db.print_database()
print()
fines_db.print_by_fine_type("Jaywalking")
print()
fines_db.print_by_city("Paris")
print()
fines_db.add_fine(2, "Noise violation")
fines_db.remove_fine(2, "Noise violation")
fines_db.change_info(2, "Amsterdam", ["Smoking"])
fines_db.print_fines_by_id(2)

