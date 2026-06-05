from ai import SmartAI
from ui import *
from scoreboard import ScoreBoard

class TicTacToe:

    def __init__(
        self,
        mode="single",
        player1="Player",
        player2="Computer"
    ):

        self.mode = mode

        self.player1 = player1
        self.player2 = player2

        self.scoreboard = ScoreBoard()

        self.reset_board()

    # ======================
    # RESET BOARD
    # ======================

    def reset_board(self):

        self.board = [
            "1","2","3",
            "4","5","6",
            "7","8","9"
        ]

        self.current = "X"

    # ======================
    # WIN CHECK
    # ======================

    def check_win(self):

        wins = [

            [0,1,2],
            [3,4,5],
            [6,7,8],

            [0,3,6],
            [1,4,7],
            [2,5,8],

            [0,4,8],
            [2,4,6]
        ]

        for a,b,c in wins:

            if (
                self.board[a] ==
                self.board[b] ==
                self.board[c]
            ):
                return True

        return False

    # ======================
    # DRAW CHECK
    # ======================

    def check_draw(self):

        for cell in self.board:

            if cell not in ["X","O"]:
                return False

        return True

    # ======================
    # PLAYER MOVE
    # ======================

    def make_move(self, pos):

        pos -= 1

        if pos < 0 or pos > 8:
            return False

        if self.board[pos] in ["X","O"]:
            return False

        self.board[pos] = self.current

        return True

    # ======================
    # BOT MOVE
    # ======================

    def bot_move(self):

        move = SmartAI.get_move(self.board)

        self.board[move] = "O"

    # ======================
    # SHOW UI
    # ======================

    def show_ui(self):

        clear()
        banner()

        self.scoreboard.display(
            self.player1,
            self.player2
        )

        draw_board(self.board)

    # ======================
    # SINGLE MATCH
    # ======================

    def play_match(self):

        while True:

            self.show_ui()

            # PLAYER X

            if self.current == "X":

                move = input(
                    f"{self.player1} (X) Choose Position: "
                )

                if not move.isdigit():
                    continue

                if not self.make_move(int(move)):
                    continue

                if self.check_win():

                    self.show_ui()

                    print(
                        f"\n🏆 {self.player1} Wins!"
                    )

                    self.scoreboard.player1_win()

                    return

                self.current = "O"

            # PLAYER O / BOT

            else:

                if self.mode == "single":

                    print(
                        f"\n{self.player2} Thinking..."
                    )

                    self.bot_move()

                else:

                    move = input(
                        f"{self.player2} (O) Choose Position: "
                    )

                    if not move.isdigit():
                        continue

                    if not self.make_move(int(move)):
                        continue

                if self.check_win():

                    self.show_ui()

                    print(
                        f"\n🏆 {self.player2} Wins!"
                    )

                    self.scoreboard.player2_win()

                    return

                self.current = "X"

            if self.check_draw():

                self.show_ui()

                print("\n🤝 Match Draw!")

                return

    # ======================
    # START GAME
    # ======================

    def start(self):

        while True:

            self.reset_board()

            self.play_match()

            print()
            again = input(
                "Play Again? (y/n): "
            ).lower()

            if again != "y":

                clear()

                print(
                    "\nThanks For Playing ❤️"
                )

                print(
                    f"\nAuthor : azod08\n"
                )

                break

