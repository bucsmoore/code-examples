import pygame

pygame.init()
"""
PART A
"""


def threePlusOne(n):
    """
    This is a function that calculates the Collatz Conjecture for any given n value and prints a list of every step along the way.
    """
    print(n)
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            print(n)
        else:
            n = (3 * n) + 1
            print(n)


"""
PART B
"""


def threePlusOne_count(n):
    """
    This is a function that calculates the Collatz Conjecture for any given n value and prints a list of every step along the way.
    """
    count = 0
    print(n)
    while n != 1:
        count += 1
        if n % 2 == 0:
            n = n / 2
            print(n)
        else:
            n = (3 * n) + 1
            print(n)
    print(f"There are {count} items in the sequence when n is {n}.")


def threePlusOne_range(upperLimit):
    """
    This is a version of the 3n+1 calculation that checks across an entire range of numbers and returns them in a dictionary.
    """
    threePlusOne_dict = {}
    for i in range(2, upperLimit + 1):
        count = 0
        n = i
        while n != 1:
            count += 1
            if n % 2 == 0:
                n = n / 2
            else:
                n = (3 * n) + 1
        threePlusOne_dict[i] = count
    print(threePlusOne_dict)


"""
PART C
"""


def threePlusOne_graph(results):
    """
    This is a continuation of the previous function that also tracks the current maximum count and graphs the number of iterations for each integer.
    """

    graph = pygame.display.set_mode()

    maxItersSoFar = max([v for v in results.values()])
    maxKeySoFar = [k for k in results.keys() if results[k] == maxItersSoFar][0]
    coordinates = []
    font = pygame.font.Font(None, 75)
    if len(coordinates) > 2:
        msg = font.render(f"{maxKeySoFar}:{maxItersSoFar}", True, "snow")
        for dictItem in results.items():
            coordinates.append((dictItem[0] * 7, dictItem[1] * 7))
        graph.fill("black")
        pygame.draw.lines(graph, "snow", False, (coordinates))
        newGraph = pygame.transform.flip(graph, False, True)
        pygame.display.flip()
        graph.blit(newGraph, (0, 0))
        graph.blit(msg, (30, 100))
        pygame.display.flip()


def main():
    result = threePlusOne_range(60)
    threePlusOne_graph(result)


main()
