class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

def build_tree(freq):
    nodes = [Node(c, f) for c, f in freq.items()]

    while len(nodes) > 1:
        nodes.sort(key=lambda x: x.freq)
        left = nodes.pop(0)
        right = nodes.pop(0)

        new = Node(None, left.freq + right.freq)
        new.left = left
        new.right = right
        nodes.append(new)
    return nodes[0]

def generate_codes(node, code, result):
    if node:
        if node.char:
            result[node.char] = code
        generate_codes(node.left, code + "0", result)
        generate_codes(node.right, code + "1", result)

def huffman_encoding(freq):
    root = build_tree(freq)
    result = {}
    generate_codes(root, "", result)
    return result

# Example
freq = {'a':5, 'b':9, 'c':12, 'd':13, 'e':16, 'f':45}
codes = huffman_encoding(freq)
print("Huffman Codes:")
for c in codes:
    print(c, ":", codes[c])
