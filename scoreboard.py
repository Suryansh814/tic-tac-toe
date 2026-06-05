class ScoreBoard:

    def __init__(self):

        self.player1_score = 0
        self.player2_score = 0

    def player1_win(self):
        self.player1_score += 1

    def player2_win(self):
        self.player2_score += 1

    def display(self, p1, p2):

        print()
        print("╔════════════════════════════╗")
        print("║         SCOREBOARD         ║")
        print("╠════════════════════════════╣")
        print(f"║ {p1:<12} : {self.player1_score:<8}║")
        print(f"║ {p2:<12} : {self.player2_score:<8}║")
        print("╚════════════════════════════╝")
        print()

