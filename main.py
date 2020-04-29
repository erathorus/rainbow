import argparse
from rainbow import Rainbow


def main():
    # Setup flags
    parser = argparse.ArgumentParser(description='Bridge Contentful and Hugo')
    parser.add_argument('store-id')
    parser.add_argument('access-token')
    parser.add_argument('content-directory')
    args = vars(parser.parse_args())

    rainbow = Rainbow(args['store-id'], args['access-token'], args['content-directory'])
    rainbow.save_posts()


if __name__ == '__main__':
    main()
