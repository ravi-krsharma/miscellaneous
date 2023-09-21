#! /env/python3

import debugpy

debugpy.log_to('logs')
debugpy.listen(('0.0.0.0', 5678))
debugpy.wait_for_client()

print("hello, world")