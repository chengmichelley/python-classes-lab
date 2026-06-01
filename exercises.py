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
        self.check_for_winner()
        self.check_for_tie()
        
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
        b = self.board
        while True:
            move = input(f"Enter a valid move (EX. A1): ").lower()
        
            if move in b and b[move] is None:
                b[move] = self.turn
                break
            else:
                print("Invalid input. Choose an empty board space.")
    
    def check_for_winner(self):
        b = self.board
        
        if (
            b['a1'] and (b['a1'] == b['b1'] == b['c1']) or 
            b['a2'] and (b['a2'] == b['b2'] == b['c2']) or 
            b['a3'] and (b['a3'] == b['b3'] == b['c3']) or 
            b['a1'] and (b['a1'] == b['b2'] == b['c3']) or 
            b['a3'] and (b['a3'] == b['b2'] == b['c1']) or 
            b['a1'] and (b['a1'] == b['a2'] == b['a3']) or 
            b['b1'] and (b['b1'] == b['b2'] == b['b3']) or
            b['c1'] and (b['c1'] == b['c2'] == b['c3'])
        ):
            self.winner = self.turn
    
    def check_for_tie(self):
        b = self.board
        if self.winner == None and None not in b.values():
            self.tie = True
            print("Tie! There is no winner.")
      
game_instance = Game()
game_instance.play_game()
