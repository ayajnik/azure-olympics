from enum import Enum,unique
import sys

sys.path.append('..')

@unique
class constant(Enum):
    account_name = ''
    account_key = ''
    container_name = 'containerrawdata1'