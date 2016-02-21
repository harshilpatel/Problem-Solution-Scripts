string_value = input()
next_line = input().split()
index = int(next_line[0])
index_character = next_line[1]

print(string_value[:index] + index_character + string_value[index+1:])