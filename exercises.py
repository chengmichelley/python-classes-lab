class Game():
    def __init__(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
            "a1": None,
            "b1": None,
            "c1": None,
            "a2": None,
            "b2": None,
            "c2": None,
            "a3": None,
            "b3": None,
            "c3": None,
        }

    def play_game(self):
        print("Welcome Let's Play Tic Tac Toe.")
        self.render()
        self.get_move()
        
    def print_board(self):
        b = self.board
        print(f"""
            A   B   C
        1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
        ----------
        2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
        ----------
        3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    def print_message(self):
        if self.tie: 
            print("Tie game!")
        elif self.winner:
            print(f"{self.winner} wins the game!")
        else: 
            print(f"It's player {self.turn}'s turn!")

    def render(self):
        self.print_board()
        self.print_message()
    
    def get_move(self):
        while True:
            move = input(f"Enter a valid move (EX. A1): ").lower()
        
            if move in self.board and self.board[move] is None:
                self.board[move] = self.turn
                break
            else:
                print("Invalid input. Choose an empty board space.")
    
game_instance = Game()
game_instance.play_game()
