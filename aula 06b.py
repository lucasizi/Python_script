num_test_case = int(input())

for i in range(num_test_case):
    test_string = input()
    even_indexed_characters = ''
    odd_indexed_characters = ''

    for j in range(len(test_string)):
        if j % 2 == 0:
            even_indexed_characters += test_string[j]
        else:
            odd_indexed_characters += test_string[j]
    print('{} {}'.format(even_indexed_characters, odd_indexed_characters))

