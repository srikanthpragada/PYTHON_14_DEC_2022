import str_funs as sf
from str_funs import has_digit

import sys

# Add a folder to module search path
sys.path.insert(0, r'd:\classroom\nov14p\demo\stlib')
print(sys.path)  # module search path

import num_funs as nf

print(nf.iseven(10))

print(sf.count_upper('AbC'))
print(has_digit('AbC12'))