import sys
import itertools

MOD = 998244353

def main() -> None:
    s, k = input().split()
    s = sorted(list(s))
    k = int(k)
    
    s = set(list(itertools.permutations(s)))
    lis = sorted(list(s))
    
    print("".join(lis[k-1]))

if __name__ == '__main__':
    main()
