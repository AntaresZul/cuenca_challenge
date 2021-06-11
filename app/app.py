from sqlalchemy import create_engine, insert

class Db:
    def __init__(self):
        db_name = 'database'
        db_user = 'username'
        db_pass = 'secret'
        db_host = 'db'
        db_port = '5432'

        # Connecto to the database
        db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
        self.db = create_engine(db_string)

    def write_row(self, queens, solutions):
        # Insert a new number into the 'numbers' table. 
        self.db.execute("INSERT INTO results (number, timestamp) " + \
            "VALUES (" + \
            str(queens) + "," + \
            str(solutions) + ");")


class Chess:
    def __init__(self, num_queens):
        self.num_queens = num_queens
        self.current_solution = [0 for x in range(num_queens)]
        self.solutions = []

    def is_safe(self, test_row, test_col):
        # no need to check for row 0
        if test_row == 0:
            return True
        for row in range(0, test_row):
            # check vertical
            if test_col == self.current_solution[row]:
                return False
            # diagonal
            elif abs(test_row - row) == abs(test_col - self.current_solution[row]):
                return False
        # no attack found
        return True


    def place_queen(self, row):
        for col in range(self.num_queens):
            if not self.is_safe(row, col):
                continue
            else:
                self.current_solution[row] = col
                if row == (self.num_queens - 1):
                    #  last row
                    self.solutions.append(self.current_solution)
                    # print( "Solution number ", len( solutions ), current_solution)
                else:
                    self.place_queen(row + 1)


if __name__ == '__main__':
    print('Application started')
    
    #num_queens = input('Enter number of queens: ')
    num_queens = 8
    for queens in range(num_queens + 1):
        
        print("Solving for " + str(queens) + " Queens")
        chess = Chess(queens)
        chess.place_queen(0)
        solutions = len(chess.solutions)

        db = Db()
        db.write_row(queens, solutions)

        print("---------------------> " + str(solutions) + " solutions found")
