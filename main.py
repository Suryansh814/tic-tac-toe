from game import TicTacToe

def main():

    print("=" * 40)
    print("      TIC TAC TOE - AZOD08")
    print("=" * 40)

    print("\n1. Single Player")
    print("2. Two Player")

    mode = input("\nSelect Mode (1/2): ").strip()

    if mode == "1":
        player_name = input("Enter Your Name: ").strip()
        game = TicTacToe(mode="single", player1=player_name)
        game.start()

    elif mode == "2":
        player1 = input("Player 1 Name: ").strip()
        player2 = input("Player 2 Name: ").strip()

        game = TicTacToe(
            mode="multi",
            player1=player1,
            player2=player2
        )

        game.start()

    else:
        print("Invalid Choice")

if __name__ == "__main__":
    main()
