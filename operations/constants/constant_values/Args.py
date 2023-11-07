from enum import Enum,unique
import sys

sys.path.append('..')

@unique
class constant(Enum):
    account_name = 'tokyoolympicsanalysis'
    account_key = ''
    container_name = ''