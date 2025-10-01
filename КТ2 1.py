import heapq
from collections import Counter


class Node:
    """Класс для узла дерева Хаффмана"""

    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


class HuffmanTree:
    """Класс для построения дерева Хаффмана"""

    def __init__(self, text):
        self.text = text
        self.codes = {}
        self.reverse_codes = {}
        self.root = self._build_tree()
        if self.root:
            self._generate_codes(self.root, "")

    def _build_tree(self):
        """Построение дерева Хаффмана"""
        if not self.text:
            return None

        # Подсчет частот символов
        frequency = Counter(self.text)

        # Создание начальной кучи
        heap = []
        for char, freq in frequency.items():
            heapq.heappush(heap, Node(char, freq))

        # Построение дерева
        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)

            merged = Node(None, left.freq + right.freq)
            merged.left = left
            merged.right = right

            heapq.heappush(heap, merged)

        return heapq.heappop(heap) if heap else None

    def _generate_codes(self, node, current_code):
        """Генерация кодов Хаффмана для символов"""
        if node is None:
            return

        if node.char is not None:
            self.codes[node.char] = current_code
            self.reverse_codes[current_code] = node.char
            return

        self._generate_codes(node.left, current_code + "0")
        self._generate_codes(node.right, current_code + "1")

    def encode(self):
        """Кодирование текста"""
        if not self.root:
            return ""
        return ''.join(self.codes[char] for char in self.text)

    def print_tree(self, node=None, level=0, prefix="Root: "):
        """Вывод дерева в читаемом формате"""
        if node is None:
            node = self.root
            if node is None:
                print("Дерево пустое")
                return

        if node.char is not None:
            print(" " * (level * 4) + prefix + f"'{node.char}': {node.freq}")
        else:
            print(" " * (level * 4) + prefix + f"({node.freq})")

            if node.left:
                self.print_tree(node.left, level + 1, "L--- ")
            if node.right:
                self.print_tree(node.right, level + 1, "R--- ")

    def print_codes(self):
        """Вывод кодов для всех символов"""
        print("\nКоды Хаффмана:")
        for char, code in sorted(self.codes.items()):
            print(f"  '{char}': {code}")


# Код, который был в функции main
print("Программа построения дерева Хаффмана для русского текста")
print("=" * 50)

text = input("Введите текст на русском языке: ").strip()

if not text:
    print("Ошибка: введен пустой текст!")
    exit()

# Проверка, что текст содержит только русские буквы и пробелы
russian_letters = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя ')
if not all(char.lower() in russian_letters for char in text):
    print("Ошибка: текст должен содержать только русские буквы и пробелы!")
    exit()

# Построение дерева Хаффмана
huffman = HuffmanTree(text)

# Вывод результатов
print("\n" + "=" * 50)
print("РЕЗУЛЬТАТЫ:")
print("=" * 50)

# Вывод дерева
print("\nДерево Хаффмана:")
huffman.print_tree()

# Вывод кодов
huffman.print_codes()

# Кодирование текста
encoded_text = huffman.encode()
print(f"\nЗакодированный текст:")
print(f"  {encoded_text}")

# Вывод статистики
original_size = len(text) * 8  # в битах (предполагаем 8 бит на символ)
encoded_size = len(encoded_text)
compression_ratio = (1 - encoded_size / original_size) * 100

print(f"\nСтатистика:")
print(f"  Исходный размер: {original_size} бит")
print(f"  Закодированный размер: {encoded_size} бит")
print(f"  Степень сжатия: {compression_ratio:.2f}%")