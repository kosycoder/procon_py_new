import types

import sys

import heapq

def main() -> None:
    q = int(sys.stdin.readline())
    a = []
    S = [0]
    hq = []
    heapq.heapify(hq)

    for itrq in range(q):
        query = list(map(int, sys.stdin.readline().split()))
        
        if query[0] == 1:
            a.append(0)
            S.append(S[itrq])
            heapq.heappush(hq, query[1]-S[itrq])

        if query[0] == 2:
            a.append(query[1])
            S.append(S[itrq]+query[1])
        
        if query[0] == 3:
            a.append(0)
            S.append(S[itrq])
            print(heapq.heappop(hq)+S[itrq+1])

if __name__ == '__main__':
    main()
