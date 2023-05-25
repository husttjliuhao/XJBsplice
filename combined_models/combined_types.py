import pandas as pd
from itertools import permutations,combinations


def main():
    df = pd.read_csv(predicted_files_dichotomous_variable)
    columnx = []
    seriex = []
    for i in range(2,max_number_in_splicing_region):
        for p in combinations(df.columns[1:], i):
            name = '+'.join(list(p))
            columnx.append(name)
            seriex.append(df[list(p)].sum(axis=1))

    df1 = pd.concat(seriex, axis=1)
    df1.columns = columnx
    df2 = pd.concat([df, df1], axis=1)

    df2.to_csv(combined_files)

if __name__ == "__main__":
    main()