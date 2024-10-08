class Stack:
    def __init__(self, name):
        self.items = []
        self.name = name

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def __str__(self):
        return str(self.items)


def move_disk(from_pole, to_pole, stacks):
    disk = from_pole.pop()
    to_pole.push(disk)
    print(f"Перемістити диск {disk} з {from_pole.name} на {to_pole.name}")
    print("Проміжний стан:", {stack.name: stack.items.copy() for stack in stacks})


def hanoi_recursive(n, source, target, auxiliary):
    if n == 1:
        move_disk(source, target, [source, auxiliary, target])
        return
    hanoi_recursive(n - 1, source, auxiliary, target)
    move_disk(source, target, [source, target, auxiliary])
    hanoi_recursive(n - 1, auxiliary, target, source)


if __name__ == "__main__":
    n = int(input("Введіть кількість дисків: "))
    source = Stack("A")
    target = Stack("C")
    auxiliary = Stack("B")

    for i in range(n, 0, -1):
        source.push(i)
    print(f"Початковий стан: A: {source} B: {target}, C :{auxiliary}")
    hanoi_recursive(n, source, target, auxiliary)
