try:
    from operations.constants.constant_values.Args import constant
    print("Import constant values")
except ImportError as e:
    print(e)

name = constant.account_name.value
key = constant.account_key.value
container = constant.container_name.value
