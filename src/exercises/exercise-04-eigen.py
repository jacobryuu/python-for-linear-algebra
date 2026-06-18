"""
モジュール4 演習: 固有値と固有ベクトル
"""

import numpy as np

# ============================================================
# 演習1: 固有値分解の確認
# ============================================================
print("=" * 60)
print("演習1: 固有値分解 A = PDP^(-1)")
print("=" * 60)

A = np.array([[4, -2], [1, 1]], dtype=float)

# (a) NumPyで固有値分解
# vals, vecs = np.linalg.eig(A)
# print("固有値:", vals)
# print("固有ベクトル:\n", vecs)

# (b) 検算: A @ v = λv
# for i in range(2):
#     v = vecs[:, i]
#     λ = vals[i]
#     left = A @ v
#     right = λ * v
#     print(f"λ={λ:.2f}: A@v={left}, λv={right}")
#     print(f"  一致: {np.allclose(left, right)}")

# (c) A = PDP^(-1) の確認
# P = vecs
# D = np.diag(vals)
# P_inv = np.linalg.inv(P)
# A_reconstructed = P @ D @ P_inv
# print("再構成 A:\n", A_reconstructed)
# print("一致:", np.allclose(A, A_reconstructed))


# ============================================================
# 演習2: べき乗法の実装
# ============================================================
print("\n" + "=" * 60)
print("演習2: べき乗法で最大固有値を求める")
print("=" * 60)


def power_iteration(A, n_iter=100, tol=1e-8):
    """
    べき乗法
    戻り値: (最大固有値, 対応する固有ベクトル)
    """
    n = A.shape[0]
    v = np.random.randn(n)
    v = v / np.linalg.norm(v)

    for _i in range(n_iter):
        # v_next = A @ v
        # v_next = v_next / np.linalg.norm(v_next)
        # 収束判定
        # if np.linalg.norm(v_next - v) < tol:
        #     break
        # v = v_next
        pass

    # レイリー商で固有値を推定
    # λ = (v @ A @ v) / (v @ v)
    # return λ, v


# A2 = np.array([[2, 1], [1, 2]], dtype=float)
# λ, v = power_iteration(A2)
# print(f"最大固有値: {λ:.4f}")
# print(f"固有ベクトル: {np.round(v, 4)}")

# 真値と比較
# true_vals, true_vecs = np.linalg.eig(A2)
# print(f"真の最大固有値: {np.max(true_vals):.4f}")


# ============================================================
# 演習3: 逆べき乗法（最小固有値）
# ============================================================
print("\n" + "=" * 60)
print("演習3: 逆べき乗法で最小固有値を求める")
print("=" * 60)


def inverse_power_iteration(A, n_iter=100):
    """
    逆べき乗法: A^(-1) にべき乗法を適用 → 最小固有値
    ヒント: A の代わりに np.linalg.solve(A, v) を使う
    """
    n = A.shape[0]
    v = np.random.randn(n)
    v = v / np.linalg.norm(v)

    for _ in range(n_iter):
        # solve A @ v_next = v （逆行列の代わりに連立方程式を解く）
        # v_next = v_next / np.linalg.norm(v_next)
        pass

    # 最小固有値 = 1/λ_inv
    # λ_inv = v @ A @ v （レイリー商）
    # return λ_inv, v


# A3 = np.array([[3, 1], [1, 3]], dtype=float)
# λ_min, v = inverse_power_iteration(A3)
# print(f"最小固有値: {λ_min:.4f}")


# ============================================================
# 演習4: PCAの実装
# ============================================================
print("\n" + "=" * 60)
print("演習4: スクラッチでPCAを実装")
print("=" * 60)


class PCA:
    """主成分分析"""

    def __init__(self, n_components):
        self.n_components = n_components

    def fit(self, X):
        """X: (n_samples, n_features)"""
        # 1. 中心化
        # 2. 共分散行列
        # 3. 固有値分解 (np.linalg.eigh は対称行列用で数値的に安定)
        # 4. 上位 n_components 個の固有ベクトルを保持
        # ここを実装
        pass

    def transform(self, X):
        """X を主成分空間に射影"""
        pass

    def inverse_transform(self, X_pca):
        """主成分空間から元の空間に復元"""
        pass


# from sklearn.datasets import load_iris
# iris = load_iris()
# X = iris.data

# pca = PCA(n_components=2)
# pca.fit(X)
# X_pca = pca.transform(X)
# X_recon = pca.inverse_transform(X_pca)

# print(f"元の形状: {X.shape}")
# print(f"PCA後: {X_pca.shape}")
# print(f"復元誤差: {np.mean((X - X_recon)**2):.4f}")


# ============================================================
# 演習5: 行列のべき乗と固有値
# ============================================================
print("\n" + "=" * 60)
print("演習5: 対角化で行列のべき乗を計算")
print("=" * 60)


def matrix_power_eig(A, k):
    """固有値分解で A^k を計算"""
    # 1. 固有値分解
    # 2. A^k = P * diag(λ_i^k) * P^(-1)
    pass


# A4 = np.array([[0.8, 0.2], [0.3, 0.7]], dtype=float)
# for k in [1, 2, 5, 10, 20]:
#     Ak = np.linalg.matrix_power(A4, k)
#     Ak_eig = matrix_power_eig(A4, k)
#     print(f"A^{k}:\n{Ak_eig}")
#     print()

# Q: k が大きくなると行列はどうなるか？
# ヒント: 最大固有値とその固有ベクトルの関係
