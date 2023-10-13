class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.list_of_strings = self.matrix_string.split("\n")
        self.row_list = []
        self.column_list = []
        for string in self.list_of_strings:
            self.row_list.append((string.split(" ")))

        for i, list in enumerate(self.row_list):
            for j, string in enumerate(list):
                self.row_list[i][j] = int(string)

    def row(self, index):
        return self.row_list[index - 1]

    def column(self, index):
        for i, list in enumerate(self.row_list[0]):
            self.column_list.append([])
            for j, string in enumerate(self.row_list):
                self.column_list[i].append(string[i])
        for i, list in enumerate(self.column_list):
            for j, string in enumerate(list):
                self.column_list[i][j] = int(string)

        return self.column_list[index - 1]
