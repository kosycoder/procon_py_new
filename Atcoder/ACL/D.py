import sys
import bisect
import itertools
import collections
import fractions
import heapq
import math
import typing
from operator import mul
from functools import reduce
from functools import lru_cache

from typing import NamedTuple, Optional, List, cast

class MFGraph:
    class Edge(NamedTuple):
        src: int
        dst: int
        cap: int
        flow: int

    class _Edge:
        def __init__(self, dst: int, cap: int) -> None:
            self.dst = dst
            self.cap = cap
            self.rev: Optional[MFGraph._Edge] = None

    def __init__(self, n: int) -> None:
        self._n = n
        self._g: List[List[MFGraph._Edge]] = [[] for _ in range(n)]
        self._edges: List[MFGraph._Edge] = []

    def add_edge(self, src: int, dst: int, cap: int) -> int:
        assert 0 <= src < self._n
        assert 0 <= dst < self._n
        assert 0 <= cap
        m = len(self._edges)
        e = MFGraph._Edge(dst, cap)
        re = MFGraph._Edge(src, 0)
        e.rev = re
        re.rev = e
        self._g[src].append(e)
        self._g[dst].append(re)
        self._edges.append(e)
        return m

    def get_edge(self, i: int) -> Edge:
        assert 0 <= i < len(self._edges)
        e = self._edges[i]
        re = cast(MFGraph._Edge, e.rev)
        return MFGraph.Edge(
            re.dst,
            e.dst,
            e.cap + re.cap,
            re.cap
        )

    def edges(self) -> List[Edge]:
        return [self.get_edge(i) for i in range(len(self._edges))]

    def change_edge(self, i: int, new_cap: int, new_flow: int) -> None:
        assert 0 <= i < len(self._edges)
        assert 0 <= new_flow <= new_cap
        e = self._edges[i]
        e.cap = new_cap - new_flow
        assert e.rev is not None
        e.rev.cap = new_flow

    def flow(self, s: int, t: int, flow_limit: Optional[int] = None) -> int:
        assert 0 <= s < self._n
        assert 0 <= t < self._n
        assert s != t
        if flow_limit is None:
            flow_limit = cast(int, sum(e.cap for e in self._g[s]))

        current_edge = [0] * self._n
        level = [0] * self._n

        def fill(arr: List[int], value: int) -> None:
            for i in range(len(arr)):
                arr[i] = value

        def bfs() -> bool:
            fill(level, self._n)
            queue = []
            q_front = 0
            queue.append(s)
            level[s] = 0
            while q_front < len(queue):
                v = queue[q_front]
                q_front += 1
                next_level = level[v] + 1
                for e in self._g[v]:
                    if e.cap == 0 or level[e.dst] <= next_level:
                        continue
                    level[e.dst] = next_level
                    if e.dst == t:
                        return True
                    queue.append(e.dst)
            return False

        def dfs(lim: int) -> int:
            stack = []
            edge_stack: List[MFGraph._Edge] = []
            stack.append(t)
            while stack:
                v = stack[-1]
                if v == s:
                    flow = min(lim, min(e.cap for e in edge_stack))
                    for e in edge_stack:
                        e.cap -= flow
                        assert e.rev is not None
                        e.rev.cap += flow
                    return flow
                next_level = level[v] - 1
                while current_edge[v] < len(self._g[v]):
                    e = self._g[v][current_edge[v]]
                    re = cast(MFGraph._Edge, e.rev)
                    if level[e.dst] != next_level or re.cap == 0:
                        current_edge[v] += 1
                        continue
                    stack.append(e.dst)
                    edge_stack.append(re)
                    break
                else:
                    stack.pop()
                    if edge_stack:
                        edge_stack.pop()
                    level[v] = self._n
            return 0

        flow = 0
        while flow < flow_limit:
            if not bfs():
                break
            fill(current_edge, 0)
            while flow < flow_limit:
                f = dfs(flow_limit - flow)
                flow += f
                if f == 0:
                    break
        return flow

    def min_cut(self, s: int) -> List[bool]:
        visited = [False] * self._n
        stack = [s]
        visited[s] = True
        while stack:
            v = stack.pop()
            for e in self._g[v]:
                if e.cap > 0 and not visited[e.dst]:
                    visited[e.dst] = True
                    stack.append(e.dst)
        return visited

def solve():
    n, m = map(int, input().split())
    mf_graph = MFGraph(n*m+2)

    s = [list(input()) for itr in range(n)]

    for itrn in range(n):
        for itrm in range(m):
            if(itrn+itrm)%2==0:
                mf_graph.add_edge(n*m, itrn*m+itrm, 1)
            else:
                mf_graph.add_edge(itrn*m+itrm, n*m+1, 1)
            if((itrn+itrm)%2==1 or s[itrn][itrm]=='#'):
                continue
            if(itrn!=0):
                if(s[itrn-1][itrm]=='.'):
                    mf_graph.add_edge(itrn*m+itrm, itrn*m+itrm-m, 1)
            if(itrn!=n-1):
                if(s[itrn+1][itrm]=='.'):
                    mf_graph.add_edge(itrn*m+itrm, itrn*m+itrm+m, 1)
            if(itrm!=0):
                if(s[itrn][itrm-1]=='.'):
                    mf_graph.add_edge(itrn*m+itrm, itrn*m+itrm-1, 1)
            if(itrm!=m-1):
                if(s[itrn][itrm+1]=='.'):
                    mf_graph.add_edge(itrn*m+itrm, itrn*m+itrm+1, 1)
    
    print(mf_graph.flow(n*m, n*m+1))

    for e in mf_graph.edges():
        if e.src == n * m or e.dst == n * m + 1 or e.flow == 0:
            continue
        from_i = e.src // m
        from_j = e.src % m
        to_i = e.dst // m
        to_j = e.dst % m
        if from_i - 1 == to_i:
            s[from_i][from_j] = '^'
            s[to_i][to_j] = 'v'
        elif from_i + 1 == to_i:
            s[from_i][from_j] = 'v'
            s[to_i][to_j] = '^'
        elif from_j - 1 == to_j:
            s[from_i][from_j] = '<'
            s[to_i][to_j] = '>'
        elif from_j + 1 == to_j:
            s[from_i][from_j] = '>'
            s[to_i][to_j] = '<'
    for i in range(n):
        print(''.join(s[i]))

if __name__ == '__main__':
    solve()
