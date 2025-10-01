import struct


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return data

    def is_empty(self):
        return self.head is None

    def peek(self):
        if self.head is None:
            return None
        return self.head.data

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements


class QueueIterator:
    def __init__(self, queue, reverse=False):
        self.reverse = reverse
        self.queue = queue

        if reverse:
            self.elements = []
            current = queue.head
            while current:
                self.elements.append(current.data)
                current = current.next
            self.elements.reverse()
            self.index = 0
            self.length = len(self.elements)
        else:
            self.current = queue.head

    def __iter__(self):
        return self

    def __next__(self):
        if self.reverse:
            if self.index >= self.length:
                raise StopIteration
            data = self.elements[self.index]
            self.index += 1
            return data
        else:
            if self.current is None:
                raise StopIteration
            data = self.current.data
            self.current = self.current.next
            return data


def get_integer_input(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Значение должно быть не меньше {min_value}")
                continue
            if max_value is not None and value > max_value:
                print(f"Значение должно быть не больше {max_value}")
                continue
            return value
        except ValueError:
            print("Пожалуйста, введите целое число")


queue = Queue()

print("=== Ввод данных для очереди ===")
n = get_integer_input("Введите количество элементов в очереди: ", min_value=1)

for i in range(n):
    value = get_integer_input(f"Введите элемент {i + 1}: ")
    queue.enqueue(value)

K = get_integer_input("Введите число K (сколько элементов удалить): ", min_value=1, max_value=n)

P1 = queue.head

print("\nИсходная очередь:")
print(" -> ".join(map(str, queue.display())))

removed_elements = []
total_sum = 0

for _ in range(K):
    if not queue.is_empty():
        data = queue.dequeue()
        removed_elements.append(data)
        total_sum += data

print(f"\nУдаленные элементы: {removed_elements}")
print(f"Сумма удаленных элементов: {total_sum}")

new_first = queue.head
if new_first:
    print(f"Новый первый элемент: значение = {new_first.data}")
    print(f"Указатель на новый первый элемент: {id(new_first)}")
    new_first_value = new_first.data
    new_first_pointer = id(new_first)
else:
    print("Очередь пуста после удаления")
    new_first_value = -1
    new_first_pointer = 0

with open('rez.dat', 'wb') as f:
    f.write(struct.pack('i', total_sum))
    f.write(struct.pack('i', new_first_value))
    f.write(struct.pack('q', new_first_pointer))

print(f"\nДанные сохранены в файл 'rez.dat'")

if not queue.is_empty():
    print("\nОчередь после удаления:")
    print(" -> ".join(map(str, queue.display())))

    print("\nПрямой порядок обхода:")
    for item in QueueIterator(queue):
        print(item, end=" ")
    print()

    print("Обратный порядок обхода:")
    for item in QueueIterator(queue, reverse=True):
        print(item, end=" ")
    print()
else:
    print("\nОчередь пуста")