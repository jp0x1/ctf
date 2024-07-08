'''
MAP OUT POSSIBLE COMBINATIONS BY COMPARING THE TWO SHUFFLED STRINGS AND SEES WHAT MATCHES BETWEEN THE TWO. COULD I HAVE CODED? YES BUT IM LAZY
aaaabbbbccccdddd -> ccaccdabdbd bbada
abcdabcdabcdabcd -> bcaadbdcdbc dacab
???????????????? -> owuwspdgrtejiiud
'''

scrambled = 'owuwspdgrtejiiud'


list = [9, 10, 0, 8, 11, 13, 3, 6, 15, 5, 14, 7, 4, 2, 12, 1]
print(len(list) )




scrambled = 'owuwspdgrtejiiud'
list = [9, 10, 0, 8, 11, 13, 3, 6, 15, 5, 14, 7, 4, 2, 12, 1]

# Determine reverse permutation
reverse_list = [0] * len(list)
for i, val in enumerate(list):
    reverse_list[val] = i

# Unshuffle the scrambled string
unscrambled = ''.join(scrambled[reverse_list[i]] for i in range(len(scrambled)))

print("Original:", unscrambled)