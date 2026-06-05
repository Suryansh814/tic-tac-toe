from colorama import Fore, Style, init
import os

init(autoreset=True)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner():

    print(Fore.RED + r"""
╔══════════════════════════════════════╗
║         TIC TAC TOE - AZOD08        ║
╚══════════════════════════════════════╝
""")

def draw_board(board):

    print()

    print(
        Fore.CYAN +
        f" {board[0]} │ {board[1]} │ {board[2]}"
    )

    print(Fore.YELLOW + "───┼───┼───")

    print(
        Fore.CYAN +
        f" {board[3]} │ {board[4]} │ {board[5]}"
    )

    print(Fore.YELLOW + "───┼───┼───")

    print(
        Fore.CYAN +
        f" {board[6]} │ {board[7]} │ {board[8]}"
    )

    print()

