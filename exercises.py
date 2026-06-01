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
        
        self.scores = {"X": 0, "O": 0, "ties": 0}

    def play_game(self):
        
        print("Welcome Let's Play Tic Tac Toe.")
        
        while True:
            while not self.winner and not self.tie:
                self.render()
                self.get_move()
                self.check_for_winner()
                self.check_for_tie()
                if not self.winner and not self.tie:
                    self.switch_turn()
        
            self.update_scores()
            self.render()
        
            if not self.prompt_play_again():
                print("Thanks for playing! Final Records:")
                print(f"Play X: {self.scores['X']} wins | Play O: {self.scores['O']} wins | Ties: {self.scores['ties']}")
                break
        
            self.reset_game()
        
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
            
        print(f"[Record -> X: {self.scores['X']} | O: {self.scores['O']} | Ties: {self.scores['ties']}]")

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
            
    def switch_turn(self):
        if self.turn == "X" :
            self.turn = "O"
        else:
            self.turn = "X"
            
    def update_scores(self):
        if self.winner:
            self.scores[self.winner] += 1
        elif self.tie:
            self.scores["ties"] += 1
            
    def prompt_play_again(self):
        while True:
            choice = input("Would you like to play again? (yes/no): ").lower()
            if choice in ["y", "yes"]:
                return True
            if choice in ["n", "no"]:
                return False
            print("Invalid response. Please select 'yes' or 'no' .")
    
    def reset_game(self):
        self.turn = "X"
        self.tie = False
        self.winner = None
        self.board = {key: None for key in self.board}
      
game_instance = Game()
game_instance.play_game()
