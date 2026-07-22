from urllib.request import urlopen
from sys import getsizeof

# Get adblock rules
config = urlopen(
    "https://johnshall.github.io/Shadowrocket-ADBlock-Rules-Forever/sr_ad_only.conf"
) .read().decode("utf-8").splitlines()

# Read custom rules
with open('custom-rules.txt', 'r') as file:
    custom_rule = file.read().splitlines()

# FINAL
final = ['FINAL,DIRECT']

# [Rule] line num
n = config.index('[Rule]')

custom_config = config[:n+1] + custom_rule + config[n+1:] + final

with open('sr_ad_only_custom.conf', 'w+') as file:
    file.writelines('\n'.join(custom_config))

print('Merge Complete')
