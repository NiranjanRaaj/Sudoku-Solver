class sudoku:

    def __init__(self, s_input):
        #storing the the matric in call variable
        self.s_input = s_input
        self.result = self.s_input
        #storing the index position of fisrt 0 in the input
        self.x = 0
        self.y = self.result[0].index(0)


    def is_safe(self,new_val,pos_x,pos_y, result_set):

        #checking the element whether it is present/repeated in same row
        if new_val not in result_set[pos_x]:
            parallel_element=[]

            # checking the element whether it is present/repeated in same column
            for i in range(0,9):
                parallel_element.append(result_set[i][pos_y])  #appending the column elements in single list
            if new_val not in parallel_element:
                #return True
                sub_matrix =[]
                #getting the min and max xy position of sub matrix
                min_x_pos = (pos_x//3) * 3 # example: (1//3)*3 -> 0 , (5//3)*3 -> 3 , (7//3)*3 -> 6
                max_x_pos = min_x_pos + 2  # example: 0 + 2 -> 2 , 3 + 2 -> 5 , 6 + 2 -> 8

                min_y_pos = (pos_y // 3) * 3 # example: (2//3)*3 -> 0 , (4//3)*3 -> 3 , (8//3)*3 -> 6
                max_y_pos = min_y_pos + 2 # example: 0 + 2 -> 2 , 3 + 2 -> 5 , 6 + 2 -> 8

                # checking the element whether it is present/repeated in sub matrix
                for p in range (min_x_pos, max_x_pos+1):
                    for q in range(min_y_pos, max_y_pos+1):
                        sub_matrix.append(result_set[p][q])
                if new_val not in sub_matrix:
                    print('inside is_safe',pos_x, pos_y)
                    print(sub_matrix)
                    return True

    def logic(self,pos_x, pos_y, result_set):
        print(pos_x,pos_y)

        #checking the position whether it is a final position and having element
        if pos_x == 8 and pos_y == 8 and result_set[pos_x][pos_y] != 0:
            self.result = result_set
            return True

        #checking the element is 0 and applying new numbers in that position
        elif self.s_input[pos_x][pos_y] == 0:
            print("True")

            #loop to find the correct number in that position
            for val in range(1,10):

                #checking the element whether it satisfies the sudoku condition
                if self.is_safe(val,pos_x,pos_y,result_set) == True:
                    result_set[pos_x][pos_y] = val
                    print(result_set)

                    # checking the position whether it is a final position
                    if pos_y == 8 and pos_x == 8:
                        self.result = result_set
                        return True

                    # checking the position and forwarding it to the next row if the y position is 8
                    elif pos_y == 8:
                        if self.logic(pos_x+1, pos_y-8, result_set) == True:
                            return True

                    # checking the position and forwarding it to the next column
                    else:
                        if self.logic(pos_x,pos_y+1,result_set) == True:
                            return True

                print(self.result)

                result_set[pos_x][pos_y] = 0
                #return False

        else:
            # checking the position and forwarding it to the next row if the y position is 8
            if pos_y == 8:
                if self.logic(pos_x + 1, pos_y - 8, result_set) == True:
                    return True

            # checking the position and forwarding it to the next column
            else:
                if self.logic(pos_x, pos_y + 1, result_set) == True:
                    return True

    def print_output(self):
        self.logic(self.x, self.y, self.result)
        '''print('\n')
        for res in self.result:
            print(res)
        print('\n')'''
        return self.result





