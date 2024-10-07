import sys, os
from tp_utils import *
from logic import *


def main():
    try:
        path = sys.argv[1]
    except:
        print("Invalid input! try with a valid path name")

    if len(sys.argv) > 2:
        raise Exception("Invalid quantity of arguments")

    arr = read_input(path)

    sofia_sum, mateo_sum, dp = coins_game(arr)
    reconstruct_solution(arr, dp)

    print("\n\nGanancia Sophia:  ", sofia_sum)
    print("Ganancia Mateo:  ", mateo_sum)

main()