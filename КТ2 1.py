class Node:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right


class MinHeap:
    def __init__(self):
        self.heap = []
        self._size = 0
        self._capacity = 0

    def _parent(self, i):
        return (i - 1) // 2

    def _left_child(self, i):
        return 2 * i + 1

    def _right_child(self, i):
        return 2 * i + 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _bubble_up(self, i):
        while i > 0:
            parent = self._parent(i)
            if self.heap[i].freq < self.heap[parent].freq:
                self._swap(i, parent)
                i = parent
            else:
                break

    def _bubble_down(self, i):
        while True:
            left = self._left_child(i)
            right = self._right_child(i)
            smallest = i
            if left < self._size and self.heap[left].freq < self.heap[smallest].freq:
                smallest = left
            if right < self._size and self.heap[right].freq < self.heap[smallest].freq:
                smallest = right
            if smallest != i:
                self._swap(i, smallest)
                i = smallest
            else:
                break

    def push(self, item):
        if self._size < self._capacity:
            self.heap[self._size] = item
        else:
            self.heap.append(item)
            self._capacity += 1
        self._size += 1
        self._bubble_up(self._size - 1)

    def pop(self):
        if self._size == 0:
            raise IndexError("pop from empty heap")

        root = self.heap[0]
        self._size -= 1

        if self._size > 0:
            self.heap[0] = self.heap[self._size]
            self._bubble_down(0)

        return root

    def __len__(self):
        return self._size


def build_huffman_tree(text):
    if string_length(text) == 0:
        print("Ошибка: Текст пустой!")
        return None

    freq = {}
    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    priority_queue = MinHeap()
    for char in freq:
        priority_queue.push(Node(char, freq[char]))

    while priority_queue.__len__() > 1:
        left = priority_queue.pop()
        right = priority_queue.pop()
        merged = Node(None, left.freq + right.freq, left, right)
        priority_queue.push(merged)

    return priority_queue.pop() if priority_queue.__len__() > 0 else None


def generate_codes(node, current_code, codes):
    if node is None:
        return
    if node.char is not None:
        codes[node.char] = current_code
        return
    generate_codes(node.left, current_code + "0", codes)
    generate_codes(node.right, current_code + "1", codes)


def calculate_bits(text, codes):
    freq = {}
    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    total_bits = 0
    for char in freq:
        code_length = 0
        for _ in codes[char]:
            code_length += 1
        total_bits += code_length * freq[char]
    return total_bits


def string_length(s):
    count = 0
    for _ in s:
        count += 1
    return count


def is_text_empty(text):
    for _ in text:
        return False
    return True


alphabet = 'йцукенгшщзфывапролджэячсмитьбю'

print("\nВведите текст для кодирования:")
text = input("Текст: ").strip()

if is_text_empty(text):
    print("\nОшибка: Текст не может быть пустым!")
    exit()

filtered_text = ''
for char in text:
    if char in alphabet:
        filtered_text += char

if is_text_empty(filtered_text):
    print("\nОшибка: После фильтрации текст пустой!")
    exit()

tree = build_huffman_tree(filtered_text)
if tree is None:
    print("Не удалось построить дерево Хаффмана")
    exit()

codes = {}
generate_codes(tree, "", codes)

print("КОДЫ ХАФФМАНА:")
for char in sorted(codes):
    count = 0
    for c in filtered_text:
        if c == char:
            count += 1
    print(f"  '{char}': {codes[char]} (встречается {count} раз)")

bits = calculate_bits(filtered_text, codes)
original_bits = string_length(filtered_text) * 8

print(f"Всего бит для кодирования: {bits}")
print(f"Бит при ASCII-кодировании: {original_bits}")

if original_bits > 0:
    compression_ratio = (1 - bits / original_bits) * 100
    print(f"Степень сжатия: {compression_ratio:.2f}%")

encoded_text = ''
for char in filtered_text:
    encoded_text += codes[char]

print("ЗАКОДИРОВАННЫЙ ТЕКСТ:")
print(encoded_text)
