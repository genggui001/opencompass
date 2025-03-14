import pandas as pd
import numpy as np


def g(df, columns):
    ans = df[df.c > 0.5][columns]
    ans["sum"] = ans.sum(axis=1)
    return ans


def define_test_input(args):
    if args.test_case == 1:
        np.random.seed(42)
        df = pd.DataFrame(np.random.rand(4, 5), columns=list("abcde"))
        columns = ["b", "e"]

    return df, columns


if __name__ == "__main__":
    import argparse
    import os
    import pickle

    parser = argparse.ArgumentParser()
    parser.add_argument("--test_case", type=int, default=1)
    args = parser.parse_args()

    df, columns = define_test_input(args)

    with open("input/input{}.pkl".format(args.test_case), "wb") as f:
        pickle.dump((df, columns), f)

    result = g(df, columns)
    with open("ans/ans{}.pkl".format(args.test_case), "wb") as f:
        pickle.dump(result, f)
