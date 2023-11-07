from enum import Enum,unique
import sys

sys.path.append('..')

@unique
class constant(Enum):
    account_name = 'tokyoolympicsanalysis'
    account_key = 'Q/2Up2Id9usdnnic3RaiUQw/p98nR+DTqoDXKaa6JD950Ba4UNWGb30+iNVPczhsULhSa9kUTkx6+AStKmiPCw=='
    container_name = 'containerrawdata'