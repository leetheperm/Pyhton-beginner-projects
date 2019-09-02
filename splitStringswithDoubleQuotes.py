import re

listr = ('')
# should be tuple 

split_data = listr.splitlines()
strip_data = str(split_data)
strip_data.strip('\t')
print(json.dumps(split_data))
