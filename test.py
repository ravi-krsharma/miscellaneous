#! /env/python3

import debugpy

debugpy.log_to('logs')
# debugpy.listen(('0.0.0.0', 5678))
debugpy.wait_for_client()

# debugpy.listen(5678)
print("Waiting for debugger attach")
# debugpy.wait_for_client()
debugpy.breakpoint()
print('break on this line')

print("hello, world")