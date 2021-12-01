n = int(input()) # 点の総数
path = list() # path[p] : 点pから行ける点のリスト
for _ in range(n):
   tmp = list(map(int, input().split())) # tmp[0]から行ける点はtmp[1]個あり、それはtmp[2:]
   path.append(tmp[2:])

entry = [None]*(n) # 最初に発見した時刻→Noneにする？
exit = [None]*(n) # 隣接リストを調べ終えた時刻→Noneにする？

TIME = 0

def dfs(p, d, f):
   global TIME

   # ここに来訪時の処理を書く
   entry[p] = TIME # 時刻の記録
   TIME += 1
   
    
   for nxt in path[p]: #繋がってる点の内 
       if entry[nxt] == None: # 未探索の(発見時刻が初期値のままの場合)
           dfs(nxt, d, f) # 先に進む
   
   # ここに帰る時の処理を書く
   exit[p] = TIME # 繋がってる全ての点を探索し終えたらその点でやることは終わり
   TIME += 1
   
   return     
   
for start in range(0, n):
   if entry[start] == None: # 未探索の点があれば
       dfs(start, entry, exit) # dfs開始

for i in range(0, n):
   print(i, entry[i], exit[i])

# 11
# 0 2 1 2
# 1 2 3 4
# 2 2 5 6
# 3 1 7
# 4 0
# 5 1 8
# 6 0
# 7 0
# 8 1 9
# 9 0
# 10 0

