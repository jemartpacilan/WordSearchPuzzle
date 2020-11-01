import sys


class WordSearch:

    def __init__(self, input_file):
        file_data = self.process_file(input_file)
        self.grid = file_data['grid']
        self.words_to_find = file_data['words_to_find']
        self.row = len(self.grid)
        self.column = len(self.grid[0])
        self.direction = [(-1,0), (0,-1), (0,1), (1,0)]
        self.output_file = open(input_file.split('.')[0]+'.out','w')

    def process_file(self, input_file):
        # Open input file
        with open(input_file, 'r') as file:
            grid_of_letters, list_of_words = file.read().split('\n\n')

        # Convert the grid of letters to list
        grid_of_letters = grid_of_letters.split()

        # Check if the grid of letters in the input file has the same number of rows and columns (X*X)
        # If the grid is not (X*X) print an error message and exit
        self.check_if_grid_is_valid(grid_of_letters)

        return {
            'grid': [list(letter.strip()) for letter in grid_of_letters], 
            'words_to_find': list_of_words.split()
        }

    def check_if_grid_is_valid(self, grid):
        for i in range(len(grid)):
            if not (len(grid[i]) == len(grid)):
                print('The grid doesn\'t have the same number of rows and columns (X*X).\nPlease input another file.')
                sys.exit()

    def start_search(self):
        # Remove duplicates from the array of words to search
        words_to_find = sorted(set(self.words_to_find), key=self.words_to_find.index)
        for word in words_to_find:
            self.search_word(word)

    def search_word(self, word):
        # Checks every column and row
        for row in range(self.row):
            for column in range(self.column):
                result = self.search_word_from_grid(word, column, row)
                if (result != None):
                    return result
        # If the word doesn't exist in the grid
        return self.output_file.write(word + ' not found\n')

    def search_word_from_grid(self, word, column_start, row_start):
        # Checks if the word is in the grid at a given starting column and row position
        # Search the word based on the specified directions  
        for direction in range(len(self.direction)):
            result = self.search_word_from_grid_in_direction(word, column_start, row_start, direction)
            if (result != None):
                return result

        return None

    def search_word_from_grid_in_direction(self, word, column_start, row_start, direction):
        # Checks if the word matches in the grid at the specified starting location going to the specified direction
        direction_names = ['up', 'left',
                            'right', 'down']
        
        (dir_row, dir_col) = self.direction[direction]
        for i in range(len(word)):
            row = row_start + i * dir_row
            col = column_start + i * dir_col
            if ((row < 0) or (row >= self.row) or (col < 0) or (col >= self.column) or
                (self.grid[row][col].upper() != word[i].upper())):
                return None

        if (direction_names[direction] =='right'):
                (colEnd, rowEnd) = (column_start + len(word), row_start + 1)
        elif (direction_names[direction] =='down'):
                (colEnd, rowEnd) = (column_start + 1, len(word) + row_start)
        elif (direction_names[direction] =='left'):
                (colEnd, rowEnd) = ((column_start + 1) - len(word) + 1 ,row_start + 1)
        elif (direction_names[direction] =='up'):
                (colEnd, rowEnd) = (column_start + 1, (row_start + 1) - len(word) + 1)

        self.output_file.write (word + ' (' + str(column_start+1) + ',' + str(row_start+1) +') (' + str(colEnd) + ',' + str(rowEnd)+ ')\n' )
        return word


# Driver Code 
if __name__== '__main__':
    # Exits the program if no input file specified
    if (len(sys.argv) < 2):
        print('No input file specified')
        print('Please specifiy an input file')
        print('Sample command: WordSearch.py search.pzl')
        sys.exit()

    search = WordSearch(sys.argv[1])
    search.start_search()