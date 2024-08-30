import argparse

def checkInput():
    parser = argparse.ArgumentParser(
        prog = "spider",
        description = "Download Images from a Website"
    )
    parser.add_argument(
        'image',
        nargs='+',
        action='append',
        help='Place image path'
    )
    
    args = parser.parse_args()
    return args

def main():
    args = checkInput()
    print(args.image)
main()