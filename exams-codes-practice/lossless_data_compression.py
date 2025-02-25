import heapq
from collections import defaultdict


# Huffman Coding Algorithm
class HuffmanCoding:
    def __init__(self, text):
        self.text = text
        self.frequency = defaultdict(int)
        self.heap = []
        self.codes = {}
        self.reverse_codes = {}

    # Function to calculate frequency of characters
    def calculate_frequency(self):
        for char in self.text:
            self.frequency[char] += 1

    # Create a heap/priority queue for the characters
    def create_heap(self):
        for key in self.frequency:
            heapq.heappush(self.heap, (self.frequency[key], key))

    # Build the Huffman Tree
    def build_tree(self):
        while len(self.heap) > 1:
            left = heapq.heappop(self.heap)
            right = heapq.heappop(self.heap)
            merged = (left[0] + right[0], left, right)
            heapq.heappush(self.heap, merged)
        return heapq.heappop(self.heap)

    # Generate the codes based on the Huffman Tree
    def generate_codes(self, node, code=""):
        if len(node) == 2:
            char = node[1]
            self.codes[char] = code
            self.reverse_codes[code] = char
        else:
            self.generate_codes(node[1], code + "0")
            self.generate_codes(node[2], code + "1")

    # Function to encode the text
    def encode(self):
        self.calculate_frequency()
        self.create_heap()
        root = self.build_tree()
        self.generate_codes(root)
        encoded_text = "".join(self.codes[char] for char in self.text)
        return encoded_text, self.codes

    # Function to decode the text
    def decode(self, encoded_text):
        decoded_text = []
        temp = ""
        for bit in encoded_text:
            temp += bit
            if temp in self.reverse_codes:
                decoded_text.append(self.reverse_codes[temp])
                temp = ""
        return "".join(decoded_text)


# Run-Length Encoding Algorithm
class RLE:
    def __init__(self, text):
        self.text = text

    def encode(self):
        encoding = ""
        i = 0
        while i < len(self.text):
            count = 1
            while i + 1 < len(self.text) and self.text[i] == self.text[i + 1]:
                i += 1
                count += 1
            encoding += str(count) + self.text[i]
            i += 1
        return encoding

    def decode(self):
        decoded_text = ""
        i = 0
        while i < len(self.text):
            count = ""
            while i < len(self.text) and self.text[i].isdigit():
                count += self.text[i]
                i += 1
            decoded_text += int(count) * self.text[i]
            i += 1
        return decoded_text


# Sample Data (Text)
input_text = "AAAAABBBCCDAA"

# Implement Huffman Coding
huffman = HuffmanCoding(input_text)
encoded_huffman, huffman_codes = huffman.encode()
decoded_huffman = huffman.decode(encoded_huffman)

# Implement Run-Length Encoding
rle = RLE(input_text)
encoded_rle = rle.encode()
decoded_rle = rle.decode()

# Output Results
print("Original Text:", input_text)
print("\nHuffman Coding:")
print("Encoded Text:", encoded_huffman)
print("Decoded Text:", decoded_huffman)
print("Huffman Codes:", huffman_codes)

print("\nRun-Length Encoding:")
print("Encoded Text:", encoded_rle)
print("Decoded Text:", decoded_rle)

# Compression Comparison (Character Count: Original vs Encoded Length)
huffman_compressed_size = len(encoded_huffman) / 8  # in bytes
rle_compressed_size = len(encoded_rle) / 8  # in bytes
original_size = len(input_text)

print("\nCompression Comparison:")
print(f"{'Algorithm':<20}{'Original Size (Bytes)':<25}{'Compressed Size (Bytes)'}")
print(f"{'Huffman Coding':<20}{original_size / 8:<25}{huffman_compressed_size:.2f}")
print(f"{'Run-Length Encoding':<20}{original_size / 8:<25}{rle_compressed_size:.2f}")
