try:
    from HttpTrigger1_tokyoOlympics.operations.constants.constant_values.Args import constant
    import argparse
    import sys

    print("Import constant values")
except ImportError as e:
    print(e)

args = None

def parse_args():
    global args

    parser = argparse.ArgumentParser()

    parser.add_argument('--{}'.format(constant.account_name.value),'-accnt_name',help="Account name for Microsoft Azure")
    parser.add_argument('--{}'.format(constant.account_key.value),'-accnt_key',help="Access keys for Storage account in Microsoft Azure")
    parser.add_argument('--{}'.format(constant.container_name.value),'-cont_name',help="Container Name in Microsoft Azure Storage account")
    args = vars(parser.parse_args())

    return args

def get_run_args(key):
    parse_args()
    return args[key]

name = get_run_args(constant.account_name.value)
key = get_run_args(constant.account_key.value)
container = get_run_args(constant.container_name.value)
