def print_error(message):
    print(f"\x1B[31mERROR: {message}\x1B[0m")

def print_success(message):
    print(f"\x1B[32mNOTE: {message}\x1B[0m")

def print_info(message):
    print(f"\x1B[34mNOTE: {message}\x1B[0m")


def print_dict(D):
    if type(D) is dict:
        for c, v in D.items():
            print("{:<12} {:<12}".format(c, v))
    else:
        print_error("WE CANNOT PRINT YOUR DICTIONARY")
        return False

def print_full_df(pd, df):
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    print(df)
    pd.reset_option('display.max_rows')
    pd.reset_option('display.max_columns')
    return


