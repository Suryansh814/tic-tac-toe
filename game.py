import random

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

        self.board = [
            "1","2","3",
            "4","5","6",
            "7","8","9"
        ]

        self.current = "X"

    # =====================
    # BOARD
    # =====================

    def show_board(self):

        print()

        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("---+---+---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("---+---+---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")

        print()

    # =====================
    # WIN CHECK
    # =====================

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

    # =====================
    # DRAW
    # =====================

    def check_draw(self):

        for cell in self.board:

            if cell not in ["X", "O"]:
                return False

        return True

    # =====================
    # MOVE
    # =====================

    def make_move(self, pos):

        pos -= 1

        if pos < 0 or pos > 8:
            return False

        if self.board[pos] in ["X", "O"]:
            return False

        self.board[pos] = self.current
        return True

    # =====================
    # BOT MOVE
    # =====================

    def bot_move(self):

        free = []

        for i in range(9):

            if self.board[i] not in ["X", "O"]:
                free.append(i)

        move = random.choice(free)

        self.board[move] = "O"

    # =====================
    # START
    # =====================

    def start(self):

        while True:

            self.show_board()

            if self.current == "X":

                move = input(
                    f"{self.player1} (X) Choose Position: "
                )

                if not move.isdigit():
                    print("Invalid Input")
                    continue

                if not self.make_move(int(move)):
                    print("Invalid Move")
                    continue

                if self.check_win():

                    self.show_board()

                    print(
                        f"{self.player1} Wins!"
                    )
                    break

                self.current = "O"

            else:

                if self.mode == "single":

                    print(
                        f"{self.player2} is thinking..."
                    )

                    self.bot_move()

                else:

                    move = input(
                        f"{self.player2} (O) Choose Position: "
                    )

                    if not move.isdigit():
                        print("Invalid Input")
                        continue

                    if not self.make_move(int(move)):
                        print("Invalid Move")
                        continue

                if self.check_win():

                    self.show_board()

                    print(
                        f"{self.player2} Wins!"
                    )
                    break

                self.current = "X"

            if self.check_draw():

                self.show_board()

                print("Match Draw!")

                break

