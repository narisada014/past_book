# 重さのオーダーが大きい時の指定重さ以下の価値最大化問題
# O(N**2 * Vmax)が計算量となる。dp1と場合によって分けて使用する
N,W = list(map(int, input().split()))
MAX_V = 100100
MAX_N = 110
ws = [0]
vs = [0]
# Nはアイテム数
# アイテム数分重さと価値を配列に追加していく
for i in range(N):
    w, v = list(map(int, input().split()))
    ws.append(w)
    vs.append(v)

# 重さの表の初期化を行う
# アイテム * 価値のマトリクスになる
weight = []
for i in range(N+1): # 0埋めしているのでN+1
    weight.append([10**18]*(MAX_V+1))

# 全ての次元が1000000000...となっているので[0][0]の初期位置を0で初期化する
weight[0][0] = 0
# 1行ずつ
for i in range(1,N+1):
    # 1列ずつ
    for v in range(MAX_V+1):
        # アイテムを選択しない場合
        weight[i][v] = min(weight[i][v], weight[i-1][v])
        # iを使用する場合
        if v - vs[i] >= 0:
            # minの前者は初期値。後者は選んだパターン
            weight[i][v] = min(weight[i][v], weight[i-1][v-vs[i]] + ws[i])
# アイテムの最終次元の中(全て選ぶ可能性を計算した結果)の最大値が答えとなる
ans = 0
for i in range(MAX_V+1):
    if weight[N][i] <= W:
        ans = i # インデックスiが価値になっている

print(ans)