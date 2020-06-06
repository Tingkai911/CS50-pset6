def main():

    while True:
        try:
            height = int(input("Height: "))
            if height in range(1,9):
                break
        except ValueError:
            continue

    pyramid(height, height)

def pyramid(height, space):

    if height == 0:
        return;

    pyramid(height - 1, space)

    for _ in range(space - height):
        print(" ", end = "")

    for _ in range(height):
        print("#", end = "")

    print("  ", end = "")

    for _ in range(height):
        print("#", end = "")

    print()

main()