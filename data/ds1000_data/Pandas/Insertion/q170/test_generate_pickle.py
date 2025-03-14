import pandas as pd
import numpy as np


def g(df):
    return df.loc[(df.sum(axis=1) != 0), (df.sum(axis=0) != 0)]


def define_test_input(args):
    if args.test_case == 1:
        df = pd.DataFrame(
            [[-1, -1, 0, 2], [0, 0, 0, 0], [1, 0, 0, 1], [0, 1, 0, 0], [1, 1, 0, 1]],
            columns=["A", "B", "C", "D"],
        )
    if args.test_case == 2:
        df = pd.DataFrame(
            [[1, 1, 0, 1], [0, 0, 0, 0], [1, 0, 0, 1], [0, 1, 0, 0], [1, 1, 0, 1]],
            columns=["A", "B", "C", "D"],
        )
    return df


if __name__ == "__main__":
    import argparse
    import os
    import pickle

    parser = argparse.ArgumentParser()
    parser.add_argument("--test_case", type=int, default=1)
    args = parser.parse_args()

    df = define_test_input(args)

    with open("input/input{}.pkl".format(args.test_case), "wb") as f:
        pickle.dump(df, f)

    result = g(df)
    with open("ans/ans{}.pkl".format(args.test_case), "wb") as f:
        pickle.dump(result, f)
