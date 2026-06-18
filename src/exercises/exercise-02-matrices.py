"""
モジュール2 演習: 行列と線形変換
"""

import numpy as np

# ============================================================
# 演習1: 行列積の手実装
# ============================================================
print("=" * 60)
print("演習1: 行列積をゼロから実装")
print("=" * 60)


def matmul(A, B):
    """行列積 A @ B を for ループで実装"""
    m, n = A.shape
    n2, p = B.shape
    assert n == n2, f"形状不一致: Aの列{n} ≠ Bの行{n2}"
    C = np.zeros((m, p))
    for _i in range(m):
        for _j in range(p):
            # ここを実装: C[i,j] = sum_k A[i,k] * B[k,j]
            pass
    return C


A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# print("自作 matmul:")
# print(matmul(A, B))
# print("NumPy @:")
# print(A @ B)


# ============================================================
# 演習2: 線形変換の可視化準備
# ============================================================
print("\n" + "=" * 60)
print("演習2: 様々な線形変換")
print("=" * 60)


def rotation_matrix(theta):
    """回転行列 (theta: radian)"""
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s], [s, c]])


def shear_matrix(k):
    """x方向のせん断行列"""
    return np.array([[1, k], [0, 1]])


def reflection_matrix():
    """y=xに関する対称変換"""
    return np.array([[0, 1], [1, 0]])


# 単位正方形の頂点
square = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]]).T  # 2x5

# 各変換を適用
theta = np.pi / 4  # 45度
R = rotation_matrix(theta)
# transformed = R @ square
# print("45°回転後の頂点:\n", transformed.T)


# ============================================================
# 演習3: 逆行列と連立方程式
# ============================================================
print("\n" + "=" * 60)
print("演習3: 逆行列で連立方程式を解く")
print("=" * 60)

# 2x2 の連立方程式
# 3x + 2y = 7
#  x -  y = -1

A = np.array([[3, 2], [1, -1]])
b = np.array([7, -1])

# (a) 逆行列を使って解く
# A_inv = np.linalg.inv(A)
# x = A_inv @ b
# print(f"逆行列による解: x={x[0]}, y={x[1]}")

# (b) np.linalg.solve で検算
# x_solve = np.linalg.solve(A, b)
# print(f"linalg.solve: x={x_solve[0]}, y={x_solve[1]}")

# (c) 逆行列が存在しない場合を試す
A_singular = np.array([[1, 2], [2, 4]])
# try:
#     np.linalg.inv(A_singular)
# except np.linalg.LinAlgError as e:
#     print(f"特異行列: {e}")
# print(f"A_singularのランク: {np.linalg.matrix_rank(A_singular)}")


# ============================================================
# 演習4: 線形変換の合成
# ============================================================
print("\n" + "=" * 60)
print("演習4: 変換の合成")
print("=" * 60)

# ベクトル v = (1, 0) に以下の操作を順に適用:
# 1. 45°回転
# 2. x方向に2倍拡大
# 3. y=xで反転

v = np.array([1.0, 0.0])

R = rotation_matrix(np.pi / 4)
S = np.array([[2, 0], [0, 1]])
M = reflection_matrix()

# 合成変換 T = M @ S @ R（右から順に適用）
# T = M @ S @ R
# result = T @ v
# print(f"合成変換の結果: {result}")

# 注意: 行列積は結合的だが非可換
# R @ S と S @ R が異なることを確認
# print("\n非可換性の確認:")
# print("RS:\n", R @ S)
# print("SR:\n", S @ R)


# ============================================================
# 演習5: 画像のアフィン変換（応用）
# ============================================================
print("\n" + "=" * 60)
print("演習5: 画像座標のアフィン変換")
print("=" * 60)


def affine_transform(points, angle_deg=30, scale=1.0, tx=0, ty=0):
    """
    点群にアフィン変換を適用（同次座標系）
    points: (N, 2) の点群
    """
    theta = np.radians(angle_deg)
    c, s = np.cos(theta), np.sin(theta)

    # 3x3 アフィン変換行列（回転 + 拡大 + 平行移動）
    T = np.array([[scale * c, -scale * s, tx], [scale * s, scale * c, ty], [0, 0, 1]])

    # 同次座標に変換
    ones = np.ones((points.shape[0], 1))
    homogeneous = np.hstack([points, ones])  # (N, 3)

    # 変換を適用
    transformed = (T @ homogeneous.T).T  # (N, 3)
    return transformed[:, :2]  # 2次元座標に戻す


# 三角形の頂点
triangle = np.array([[0, 0], [1, 0], [0.5, 1]])

# result = affine_transform(triangle, angle_deg=45, scale=1.5, tx=2, ty=1)
# print("変換前:\n", triangle)
# print("変換後 (45°回転, 1.5倍, (2,1)移動):\n", result)


# ============================================================
# 発展課題: PageRankの1反復
# ============================================================
print("\n" + "=" * 60)
print("発展課題: PageRankの1反復")
print("=" * 60)


def pagerank_once(L, r):
    """
    L: 隣接行列 (n x n)
    r: 現在のランクベクトル (n,)
    """
    L.shape[0]
    # 遷移確率行列 M を計算
    # M[:, j] = L[:, j] / sum(L[:, j])
    # ここを実装
    pass


# 4ページのリンク構造
L = np.array(
    [
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0],
    ]
)

r = np.ones(4) / 4
# for i in range(5):
#     r = pagerank_once(L, r)
#     print(f"反復{i+1}: {np.round(r, 4)}")
