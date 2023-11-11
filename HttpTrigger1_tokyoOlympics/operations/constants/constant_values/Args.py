from enum import Enum,unique
import sys

sys.path.append('..')

@unique
class constant(Enum):
    account_name = 'account_name'
    account_key = 'account_key'
    container_name = 'container_name'