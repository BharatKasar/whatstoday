import copy

def exist(board, word: str) -> bool:
    exists = False
    def find(row, col, fs, path):
            print (row, col, fs)
            if row < 0 or row >= len(board):
                return
            if col < 0 or col >= len(board[0]):
                return
            if (row, col) in path:
                return
            if word[len(fs)] != board[row][col]:
                return
            fs += board[row][col]
            path.append((row, col))
            if fs == word:
                print ("in....")
                exists = True
                return
            find(row+1, col, fs, copy.copy(path))
            find(row-1, col, fs, copy.copy(path))
            find(row, col+1, fs, copy.copy(path))
            find(row, col-1, fs, copy.copy(path))
    for i in range(1):
        for j in range(1):
            find(i, j, "", [])
    print ("done.......", exists)
    return exists


board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
word = "ABCESEEEFS"
print(exist(board, word))