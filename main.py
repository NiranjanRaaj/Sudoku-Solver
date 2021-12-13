import sudoku_logic as sl

if __name__=='__main__':
    sudoku_input = [[0, 0, 4, 0, 5, 0, 0, 0, 0],
                    [9, 0, 0, 7, 3, 4, 6, 0, 0],
                    [0, 0, 3, 0, 2, 1, 0, 4, 9],
                    [0, 3, 5, 0, 9, 0, 4, 8, 0],
                    [0, 9, 0, 0, 0, 0, 0, 3, 0],
                    [0, 7, 6, 0, 1, 0, 9, 2, 0],
                    [3, 1, 0, 9, 7, 0, 2, 0, 0],
                    [0, 0, 9, 1, 8, 2, 0, 0, 3],
                    [0, 0, 0, 0, 6, 0, 1, 0, 0]]

    newobj = sl.sudoku(sudoku_input)
    newobj.print_output()
    print('\n')
    for res in newobj.result:
        print(res)
    print('\n')