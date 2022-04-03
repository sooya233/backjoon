# Num1916.py - 최소비용 구하기
# https://www.acmicpc.net/problem/1916
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
MAX = sys.maxsize

n = int(input())
m = int(input())

graph = [[] for i in range(n + 1)]
dp = [MAX for i in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

start, end = map(int, input().split())

def dijkstra(start):
    dp[start] = 0
    heap = []
    heappush(heap, [0, start])
    while heap:
        c, n = heappop(heap)
        if dp[n] < c:
            continue
        for n_n, cost in graph[n]:
            n_w = c + cost
            if dp[n_n] > n_w:
                dp[n_n] = n_w
                heappush(heap, [n_w, n_n])
dijkstra(start)
print(dp[end])