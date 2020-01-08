import argparse
import sys


def fib(n):

    a,b = 0,1

    for i in range(n):
        a,b = b, a+b

    return a

def main():

    parser = argparse.ArgumentParser(description = "exemplo arg")


    part = 1

    if part == 1:
        part1(parser)
    elif part == 2:
        part2(parser)
    else:
        part1(parser)


def part1(parser):
    parser.add_argument("num", help="numero da sequencia", type=int)
    args = parser.parse_args()

    resultado = fib(args.num)

    print("O", args_num, "da sequencia é: ", resultado)

        
