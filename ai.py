class SmartAI:

    @staticmethod
    def get_move(board):

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

        # Win if possible
        for combo in wins:

            temp = board[:]

            count_o = 0
            empty = -1

            for pos in combo:

                if temp[pos] == "O":
                    count_o += 1

                elif temp[pos] not in ["X", "O"]:
                    empty = pos

            if count_o == 2 and empty != -1:
                return empty

        # Block player
        for combo in wins:

            temp = board[:]

            count_x = 0
            empty = -1

            for pos in combo:

                if temp[pos] == "X":
                    count_x += 1

                elif temp[pos] not in ["X", "O"]:
                    empty = pos

            if count_x == 2 and empty != -1:
                return empty

        # Take center
        if board[4] not in ["X","O"]:
            return 4

        # Corners
        for pos in [0,2,6,8]:
            if board[pos] not in ["X","O"]:
                return pos

        # Remaining
        for i in range(9):
            if board[i] not in ["X","O"]:
                return i

