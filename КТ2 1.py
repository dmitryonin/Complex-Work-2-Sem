from collections import Counter


class Node:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right


class MinHeap:
    def __init__(self):
        self.heap = []

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
        size = len(self.heap)
        while True:
            left = self._left_child(i)
            right = self._right_child(i)
            smallest = i
            if left < size and self.heap[left].freq < self.heap[smallest].freq:
                smallest = left
            if right < size and self.heap[right].freq < self.heap[smallest].freq:
                smallest = right
            if smallest != i:
                self._swap(i, smallest)
                i = smallest
            else:
                break

    def push(self, item):
        self.heap.append(item)
        self._bubble_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            raise IndexError("pop from empty heap")
        root = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self._bubble_down(0)
        return root

    def __len__(self):
        return len(self.heap)


def build_huffman_tree(text):
    if not text:
        print("Ошибка: Текст пустой!")
        return None

    freq = Counter(text)
    priority_queue = MinHeap()
    for char in freq:
        priority_queue.push(Node(char, freq[char]))

    while len(priority_queue) > 1:
        left = priority_queue.pop()
        right = priority_queue.pop()
        merged = Node(None, left.freq + right.freq, left, right)
        priority_queue.push(merged)

    return priority_queue.pop() if priority_queue else None


def generate_codes(node, current_code, codes):
    if node is None:
        return
    if node.char is not None:
        codes[node.char] = current_code
        return
    generate_codes(node.left, current_code + "0", codes)
    generate_codes(node.right, current_code + "1", codes)



def calculate_bits(text, codes):
    freq = Counter(text)
    total_bits = sum(len(codes[char]) * freq[char] for char in freq)
    return total_bits

alphabet = 'йцукенгшщзфывапролджэячсмитьбю'

print("\nВведите текст для кодирования:")
text = input("Текст: ").strip()

if not text:
    print("\nОшибка: Текст не может быть пустым!")

filtered_text = ''.join([char for char in text if char in alphabet])


tree = build_huffman_tree(filtered_text)
codes = {}
generate_codes(tree, "", codes)

print("КОДЫ ХАФФМАНА:")
for char in sorted(codes):
    count = filtered_text.count(char)
    print(f"  '{char}': {codes[char]} (встречается {count} раз)")

bits = calculate_bits(filtered_text, codes)
original_bits = len(filtered_text) * 8

print(f"Всего бит для кодирования: {bits}")
print(f"Бит при ASCII-кодировании: {original_bits}")

if original_bits > 0:
    compression_ratio = (1 - bits / original_bits) * 100
    print(f"Степень сжатия: {compression_ratio:.2f}%")

encoded_text = ''.join([codes[char] for char in filtered_text])
print("ЗАКОДИРОВАННЫЙ ТЕКСТ:")

print(encoded_text)
