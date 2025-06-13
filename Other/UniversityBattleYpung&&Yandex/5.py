def solution(square):
    for i in range(4):
        column_word = ''.join([row[i] for row in square])
        if square[i] != column_word:
            return False
    return True