import heapq

def huffman_encoding(characters, frequencies):
    heap = [[freq, [char, ""]] for char, freq in zip(characters, frequencies)]
    heapq.heapify(heap)

    while len(heap) > 1:
        low = heapq.heappop(heap)
        high = heapq.heappop(heap)

        for pair in low[1:]:
            pair[1] = '0' + pair[1]
        for pair in high[1:]:
            pair[1] = '1' + pair[1]

        heapq.heappush(heap, [low[0] + high[0]] + low[1:] + high[1:])

    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

# Example usage
chars = ['A', 'B', 'C', 'D', 'E', 'F']
freq = [5, 9, 12, 13, 16, 45]

huff = huffman_encoding(chars, freq)

print("Character\tHuffman Code")
for char, code in huff:
    print(f"{char}\t\t{code}")
