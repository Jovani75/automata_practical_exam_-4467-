def increment_binary(bin_str):
    bin_list = list(bin_str)
    i = len(bin_list) - 1
    while i >= 0:
        if bin_list[i] == '0':
            bin_list[i] = '1'
            break
        else:
            bin_list[i] = '0'
            i -= 1
    if i < 0:
        bin_list.insert(0, '1')
    return ''.join(bin_list)

print(increment_binary("1011"))
print(increment_binary("111"))
