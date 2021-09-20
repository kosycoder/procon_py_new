import sys

MOD = 998244353

def main() -> None:
    n = int(input())

    k = 0
    for itr in range(63):
        if pow(2,k)>n:
            print(k-1)
            break
        else:
            k += 1

if __name__ == '__main__':
    main()