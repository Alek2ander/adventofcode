import os
import time

os.chdir('./2023')
start_perf_counter = time.perf_counter_ns()
exec(open("./01.py").read())
end_perf_counter = time.perf_counter_ns()
print(f'Perf counter: {(end_perf_counter - start_perf_counter)/1000000}ms')
