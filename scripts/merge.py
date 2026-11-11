from urllib.request import urlopen
from sys import getsizeof

# Get adblock rules
config = urlopen(
    "https://johnshall.github.io/Shadowrocket-ADBlock-Rules-Forever/sr_ad_only.conf"
) .read().decode("utf-8").splitlines()

# Read custom rules
with open('custom-rules.txt', 'r') as file:
    custom_rule = file.read().splitlines()

start_idx = custom_rule.index("# START")
final_idx = custom_rule.index("# FINAL")

# rules to be put before adblock rules
start = custom_rule[start_idx+1:final_idx]

# final
final = custom_rule[final_idx+1:]

# [Rule] line num
n = config.index('[Rule]')

custom_config = config[:n+1] + start + \
    config[n+1:] + final

with open('sr_ad_only_custom.conf', 'w+') as file:
    file.writelines('\n'.join(custom_config))

print('Merge Complete')
