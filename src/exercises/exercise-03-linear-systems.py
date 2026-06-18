"""
モジュール3 演習: 線形システムとLU分解
"""

import numpy as np

# ============================================================
# 演習1: ガウス消去法の実装
# ============================================================
print("=" * 60)
print("演習1: ガウス消去法（部分ピボッティング付き）")
print("=" * 60)


def gauss_elimination(A, b):
    """
    ガウス消去法で Ax = b を解く
    A: n x n 行列
    b: n 次元ベクトル
    戻り値: x (n 次元ベクトル)
    """
    n = len(b)
    np.column_stack([A.astype(float), b.astype(float)])

    for i in range(n):
        # 部分ピボッティング
        # |Ab[j,i]| が最大となる行を見つけて入れ替え
        # ここを実装

        for _j in range(i + 1, n):
            # 前進消去
            # factor = Ab[j,i] / Ab[i,i]
            # Ab[j,i:] -= factor * Ab[i,i:]
            pass

    # 後退代入
    x = np.zeros(n)
    for _ in range(n - 1, -1, -1):
        # x[i] = (Ab[i,-1] - Ab[i,i+1:n] @ x[i+1:n]) / Ab[i,i]
        pass

    return x


# テスト
A = np.array([[2, 1, -1], [-3, -1, 2], [-2, 1, 2]], dtype=float)
b = np.array([8, -11, -3], dtype=float)

# x = gauss_elimination(A, b)
# print(f"解: {x}")
# print(f"検算: A @ x = {A @ x}")


# ============================================================
# 演習2: LU分解の実装
# ============================================================
print("\n" + "=" * 60)
print("演習2: LU分解（Doolittle法）")
print("=" * 60)


def lu_decomposition(A):
    """
    A = LU に分解（Doolittle法: Lの対角=1）
    戻り値: (L, U)
    """
    n = A.shape[0]
    L = np.eye(n)
    U = np.zeros((n, n))

    for i in range(n):
        # U の i行を計算
        for _j in range(i, n):
            # U[i,j] = A[i,j] - sum_{k=0}^{i-1} L[i,k] * U[k,j]
            pass

        # L の i列を計算
        for _j in range(i + 1, n):
            # L[j,i] = (A[j,i] - sum_{k=0}^{i-1} L[j,k] * U[k,i]) / U[i,i]
            pass

    return L, U


# テスト
A = np.array([[2, 1, 1], [4, 3, 3], [8, 7, 9]], dtype=float)

# L, U = lu_decomposition(A)
# print("L:\n", np.round(L, 4))
# print("U:\n", np.round(U, 4))
# print("検算 L@U:\n", np.round(L @ U, 4))
# print("元のA:\n", A)


# ============================================================
# 演習3: LU分解で連立方程式を解く
# ============================================================
print("\n" + "=" * 60)
print("演習3: LU分解で Ax = b を解く")
print("=" * 60)


def solve_lu(A, b):
    """LU分解で Ax = b を解く"""
    # 1. A = LU と分解（lu_decompositionを使う）
    # 2. Ly = b を前進代入で解く
    # 3. Ux = y を後退代入で解く
    pass


# A2 = np.array([[4, 3], [6, 3]], dtype=float)
# b2 = np.array([10, 12], dtype=float)
# x2 = solve_lu(A2, b2)
# print(f"解: {x2}")
# print(f"検算: A @ x = {A2 @ x2}")

# 複数の右辺ベクトルでの効率を確認
# b_multi = np.column_stack([b2, np.array([5, 6], dtype=float)])
# ここを実装


# ============================================================
# 演習4: 線形回帰（最小二乗法）
# ============================================================
print("\n" + "=" * 60)
print("演習4: 最小二乗法による線形回帰")
print("=" * 60)

# データ: y = 2x + 1 + ノイズ
np.random.seed(42)
x_data = np.linspace(0, 5, 20)
y_true = 2 * x_data + 1
y_noisy = y_true + np.random.randn(20) * 0.5

# (a) デザイン行列: [x, 1]
# A = np.column_stack([x_data, np.ones(20)])

# (b) 正規方程式を解く
# theta = np.linalg.inv(A.T @ A) @ A.T @ y_noisy

# (c) np.linalg.lstsq で検算
# theta2 = np.linalg.lstsq(A, y_noisy, rcond=None)[0]

# print(f"正規方程式: y = {theta[0]:.3f}x + {theta[1]:.3f}")
# print(f"lstsq:      y = {theta2[0]:.3f}x + {theta2[1]:.3f}")
# print(f"真値:       y = 2.000x + 1.000")

# (d) 多項式回帰（2次）に拡張
# A_poly = np.column_stack([x_data**2, x_data, np.ones(20)])
# theta_poly = np.linalg.lstsq(A_poly, y_noisy, rcond=None)[0]
# print(f"2次回帰: y = {theta_poly[0]:.3f}x^2 + {theta_poly[1]:.3f}x + {theta_poly[2]:.3f}")


# ============================================================
# 演習5: 条件数の確認
# ============================================================
print("\n" + "=" * 60)
print("演習5: 行列の条件数")
print("=" * 60)


# ヒルベルト行列（有名な悪条件行列）
def hilbert(n):
    H = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            H[i, j] = 1.0 / (i + j + 1)
    return H


# for n in [4, 6, 8, 10]:
#     H = hilbert(n)
#     cond = np.linalg.cond(H)
#     print(f"n={n}: 条件数 = {cond:.2e}")

# Q: n が大きくなると条件数はどうなるか？
# Q: 条件数が大きいと連立方程式を解くときに何が問題か？
