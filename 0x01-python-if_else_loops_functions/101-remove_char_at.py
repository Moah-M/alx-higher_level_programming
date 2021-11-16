
#!/usr/bin/python3
def remove_char_at(str, x):
    s = ""
    for y in range(len(str)):
        if y != x:
            s = s + str[y]
    return s
