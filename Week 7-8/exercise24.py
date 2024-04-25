import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--physics", help="Physics Mark")
    parser.add_argument("--chemistry", help="Chemistry Mark")
    parser.add_argument("--maths", help="Maths Mark")

    args = parser.parse_args()

    avg_mark = (int(args.physics) + int(args.chemistry) + int(args.maths)) / 3

    print(f"Average mark is: {avg_mark}")