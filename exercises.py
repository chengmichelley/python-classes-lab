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
        
        print("Welcome! Let's Play Tic Tac Toe.")
        
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
        board = self.board
        print(f"""
            A   B   C
        1)  {board['a1'] or ' '} | {board['b1'] or ' '} | {board['c1'] or ' '}
        ----------
        2)  {board['a2'] or ' '} | {board['b2'] or ' '} | {board['c2'] or ' '}
        ----------
        3)  {board['a3'] or ' '} | {board['b3'] or ' '} | {board['c3'] or ' '}
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
        board = self.board
        while True:
            move = input(f"Enter a valid move (EX. a1): ").lower()
        
            if move in board and board[move] is None:
                board[move] = self.turn
                break
            else:
                print("Invalid input. Choose an empty board space.")
    
    def check_for_winner(self):
        board = self.board
        
        winning_combinations = [
            ['a1', 'b1', 'c1'],
            ['a2', 'b2', 'c2'],
            ['a3', 'b3', 'c3'],
            ['a1', 'a2', 'a3'],
            ['b1', 'b2', 'b3'],
            ['c1', 'c2', 'c3'],
            ['a1', 'b2', 'c3'],
            ['c1', 'b2', 'a3']
        ]
        
        for tile1, tile2, tile3 in winning_combinations:
            if board[tile1] and (board[tile1] == board[tile2] == board[tile3]):
                self.winner = self.turn
                break
    
    def check_for_tie(self):
        board = self.board
        if self.winner is None and None not in board.values():
            self.tie = True
                        
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
