import argparse

from files.src.files import files_stats, draw_stats


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filepath', type=str)
    argv = parser.parse_args()
    return argv


def main(path: str):
    if path is None:
        path = '.'
    df = files_stats.get_stats(path)
    print(df)
    draw_stats.draw_plot(df)


if __name__ == "__main__":
    args = parse_args()
    main(args.filepath)
