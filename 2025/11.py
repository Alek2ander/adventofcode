from functools import cache

@cache
def count_paths(node, target):
    if node == target:
        return 1
    if node not in graph:
        return 0
    return sum(count_paths(src, target) for src in graph[node])

graph = {}
with (open('11.txt', 'r') as in_file):
    for line in in_file.readlines():
        source, connections = line.strip().split(': ')
        for connection in connections.split(' '):
            if connection not in graph:
                graph[connection] = []
            graph[connection].append(source)
print(count_paths('out', 'you'))
print(count_paths('out', 'fft') * count_paths('fft', 'dac') * count_paths('dac', 'svr')
      + count_paths('out', 'dac') * count_paths('dac', 'fft') * count_paths('fft', 'svr'))
