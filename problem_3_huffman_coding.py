import sys
import heapq


class TreeNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.char < other.char
        return self.freq < other.freq

    def __repr__(self):
        return f"{self.char}:{self.freq}"


def get_frequency(data):
    freq_dict = {}
    for char in data:
        if not char in freq_dict:
            freq_dict[char] = 0
        freq_dict[char] += 1
    return freq_dict


def create_huffman_tree(frequency):
    pq_list = [TreeNode(char, frequency[char]) for char in frequency]
    heapq.heapify(pq_list)
    print(pq_list)

    while len(pq_list) > 1:
        left_subtree = heapq.heappop(pq_list)
        right_subtree = heapq.heappop(pq_list)
        new_node = TreeNode('$', left_subtree.freq + right_subtree.freq)
        new_node.left = left_subtree
        new_node.right = right_subtree
        heapq.heappush(pq_list, new_node)
    return pq_list[0]


def generate_huffman_codes(node, path, huffman_codes):
    if node.left is not None:
        generate_huffman_codes(node.left, path + "0", huffman_codes)

    if node.right is not None:
        generate_huffman_codes(node.right, path + "1", huffman_codes)

    if node.left is None and node.right is None:
        huffman_codes[node.char] = path


def encode(data, huffman_codes):
    encoded_string = ""
    for ch in data:
        code = huffman_codes[ch]
        encoded_string = encoded_string + code
    return encoded_string


def huffman_encoding(data):
    frequency = get_frequency(data)
    tree = create_huffman_tree(frequency)
    huffman_codes = {}
    generate_huffman_codes(tree, "", huffman_codes)
    encoded_string = encode(data, huffman_codes)
    return encoded_string, tree


def huffman_decoding(data, tree):
    decoded_string = ""
    current = tree
    for bit in data:
        if bit == '0':
            current = current.left
        else:
            current = current.right
        if current.left is None and current.right is None:
            decoded_string += current.char
            current = tree
    return decoded_string


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))