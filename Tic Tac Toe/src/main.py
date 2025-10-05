import random


class TicTacToe:
    """
    A class to represent the Tic Tac Toe game.
    Manages the board, player turns, and checks for a winner or a tie.
    """
    def __init__(self) -> None:
        """
        Initializes the game board and selects the first player randomly.
        The board is represented by a list of 9 elements, each initialized to an empty space.
        """
        self.board = [' '] * 10  # The board consists of 9 empty spaces (index 1-9 are the positions for the players).
        self.player_turn = self.get_random_first_player()

    def get_random_first_player(self) -> str:
        """
        Randomly selects the first player from two inputs and assigns 'X' or 'O'.
        Prompts the user for player names and determines who goes first.
        
        :return: 'X' representing the first player.
        """
        player_1 = input('Please write down the name of first player: ')
        player_2 = input('Please write down the name of second player: ')

        if random.choice([player_1, player_2]) == player_1:
            print(f'{player_1} is X.\n{player_2} is O.\n{player_1} begins.')
            
        else:
            print(f'{player_2} is X.\n{player_1} is O.\n{player_2} begins.')
        
        return 'X'

    def swap_player_turn(self) -> str:
        """
        Swaps the current player's turn between 'X' and 'O'.
        
        :return: The new player's turn ('X' or 'O').
        """
        if self.player_turn == 'X':
            self.player_turn = 'O'
        else:
            self.player_turn = 'X'
        return self.player_turn
    
    def fix_spot(self, cell: str, player: str) -> None:
        """
        Updates the board by placing the player's mark ('X' or 'O') in the selected cell.
        If the selected cell is already occupied, prompts the user to choose a different cell.

        :param cell: The cell number (1-9) where the player wants to place their mark.
        :param player: The current player ('X' or 'O').
        """
        if self.board[int(cell)] != ' ':
            print(f'Square number {cell} is taken.')
            cell = input('Please choose another square: ')
        
        self.board[int(cell)] = player

    def show_board(self) -> None:
        """
        Displays the current state of the game board in a readable format.
        """
        print(f"""

            {self.board[1]} | {self.board[2]} | {self.board[3]}
           -----------
            {self.board[4]} | {self.board[5]} | {self.board[6]}
           -----------
            {self.board[7]} | {self.board[8]} | {self.board[9]}
            
        """)

    def check_board_filled(self) -> bool:
        """
        Checks if the board is completely filled (no empty spaces).

        :return: True if the board is full, False otherwise.
        """
        return ' ' not in self.board[1:]

    def check_winner(self, player: str) -> bool:
        """
        Checks if the current player has won by checking all possible winning combinations.

        :param player: The current player ('X' or 'O').
        :return: True if the player has won, False otherwise.
        """
        win_combinations = [(1, 2, 3), (4, 5, 6), (7, 8, 9),
                            (1, 4, 7), (2, 5, 8), (3, 6, 9),
                            (1, 5, 9), (3, 5, 7)]
        
        for combination in win_combinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] == player:
                return True
        return False

    def play(self) -> None:
        """
        Starts and manages the flow of the Tic Tac Toe game. Players take turns until there is a winner or a draw.
        """
        while True:
            cell = input("""Please choose one of the squares:
                         
            1 | 2 | 3
           -----------
            4 | 5 | 6
           -----------
            7 | 8 | 9
        
        """)
            if int(cell) in range(1, 10):
                self.fix_spot(cell, self.player_turn)
                self.show_board()

                if self.check_winner(self.player_turn):
                    print(f'Player {self.player_turn} Won!')
                    break

                if self.check_board_filled():
                    print("It's a Draw!")
                    break

                self.swap_player_turn()


if __name__ == '__main__':
    game = TicTacToe()
    game.play()
