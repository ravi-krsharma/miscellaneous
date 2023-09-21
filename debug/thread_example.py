import debugpy
import threading

def foo(x):
    debugpy.debug_this_thread()
    print('set breakpoint here')
    return 0

from ctypes import CFUNCTYPE, c_void_p, c_size_t, c_uint32, windll

event = threading.Event()

thread_func_p = CFUNCTYPE(c_uint32, c_void_p)
thread_func = thread_func_p(foo)
assert windll.kernel32.CreateThread(c_void_p(0), c_size_t(0), thread_func, c_void_p(0), c_uint32(0), c_void_p(0))

event.wait()