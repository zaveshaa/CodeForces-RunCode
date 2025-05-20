def solution(letter):
    rows = [
        "qwertyuiop",
        "asdfghjkl",
        "zxcvbnm"
    ]
    for row in rows:
        if letter in row:
            index = row.index(letter)
            next_index = (index + 1) % len(row)
            return row[next_index]
    return letter