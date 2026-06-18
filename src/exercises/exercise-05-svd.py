"""
モジュール5 演習: SVDと高度な分解
"""

import numpy as np

# ============================================================
# 演習1: SVDの手計算確認
# ============================================================
print("=" * 60)
print("演習1: SVDの検算")
print("=" * 60)

A = np.array([[1, 2], [3, 4], [5, 6]], dtype=float)

U, s, Vt = np.linalg.svd(A, full_matrices=False)

# (a) 直交性の確認
print("Uの形状:", U.shape)
print("s:", s)
print("Vtの形状:", Vt.shape)

# U の直交性: U @ U.T = I か？
# print("U @ U.T:\n", np.round(U @ U.T, 6))

# V の直交性: Vt @ Vt.T = I か？
# print("Vt @ Vt.T:\n", np.round(Vt @ Vt.T, 6))

# (b) 復元
# Σ を構成して A = UΣVt を確認
# m, n = A.shape
# Sigma = np.zeros((m, n))
# Sigma[:n, :n] = np.diag(s)
# A_reconstructed = U @ Sigma @ Vt
# print("復元誤差:", np.linalg.norm(A - A_reconstructed))

# (c) AtA の固有値との関係
# AtA = A.T @ A
# vals, vecs = np.linalg.eigh(AtA)
# print("\nA^TA の固有値:", np.sort(vals)[::-1])
# print("特異値の2乗:", s**2)


# ============================================================
# 演習2: 低ランク近似の実装
# ============================================================
print("\n" + "=" * 60)
print("演習2: SVDによる低ランク近似")
print("=" * 60)


def low_rank_approx(A, k):
    """A のランク k 近似"""
    U, s, Vt = np.linalg.svd(A, full_matrices=False)
    # 最初の k 個の特異値だけを使う
    # ここを実装
    pass


# ランダムな 50x30 行列
# np.random.seed(42)
# A_big = np.random.randn(50, 30)

# for k in [1, 5, 10, 15, 20, 30]:
#     Ak = low_rank_approx(A_big, k)
#     error = np.linalg.norm(A_big - Ak) / np.linalg.norm(A_big)
#     compression = (50 * k + k + k * 30) / (50 * 30)
#     print(f"k={k:2d}: 相対誤差={error:.4f}, 圧縮率={compression:.1%}")


# ============================================================
# 演習3: 画像圧縮のシミュレーション
# ============================================================
print("\n" + "=" * 60)
print("演習3: 画像圧縮シミュレーション")
print("=" * 60)


# 疑似画像: 100x100 のチェッカーボード
def checkerboard(n=100, size=10):
    board = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if (i // size + j // size) % 2 == 0:
                board[i, j] = 1.0
    return board


# img = checkerboard(100, 10)
# U, s, Vt = np.linalg.svd(img, full_matrices=False)

# # k を変えて圧縮
# for k in [1, 3, 5, 10, 20]:
#     compressed = U[:, :k] @ np.diag(s[:k]) @ Vt[:k, :]
#     error = np.linalg.norm(img - compressed) / np.linalg.norm(img)
#     ratio = (100 * k + k + k * 100) / (100 * 100)
#     print(f"k={k:2d}: 誤差={error:.4f}, 圧縮率={ratio:.1%}")


# ============================================================
# 演習4: 推薦システムのシミュレーション
# ============================================================
print("\n" + "=" * 60)
print("演習4: SVDで欠損値補完")
print("=" * 60)

# ユーザー-アイテム評価行列（0は未評価）
R = np.array(
    [
        [5, 3, 0, 1, 4],
        [4, 0, 0, 1, 5],
        [1, 1, 0, 5, 0],
        [1, 0, 0, 4, 0],
        [0, 1, 5, 4, 0],
        [0, 0, 4, 0, 5],
    ],
    dtype=float,
)

# (a) SVD
# U, s, Vt = np.linalg.svd(R, full_matrices=False)
# print("特異値:", np.round(s, 2))

# (b) ランク2近似で欠損値を予測
# k = 2
# R_pred = U[:, :k] @ np.diag(s[:k]) @ Vt[:k, :]
# print("予測評価:\n", np.round(R_pred, 1))

# (c) 元の0の部分だけ表示
# missing = R == 0
# print("欠損値の予測:\n", np.round(R_pred[missing], 2))


# ============================================================
# 演習5: Cholesky分解
# ============================================================
print("\n" + "=" * 60)
print("演習5: Cholesky分解の実装")
print("=" * 60)


def cholesky(A):
    """A = LL^T のCholesky分解（Aは対称正定値）"""
    n = A.shape[0]
    L = np.zeros((n, n))

    for i in range(n):
        for _j in range(i + 1):
            # sum_k L[i,k] * L[j,k]
            # ここを実装
            pass

    return L


# A_pos = np.array([[4, 2, -2],
#                   [2, 5, 0],
#                   [-2, 0, 6]], dtype=float)

# L = cholesky(A_pos)
# print("L:\n", np.round(L, 4))
# print("検算 L @ L.T:\n", np.round(L @ L.T, 4))
# print("一致:", np.allclose(A_pos, L @ L.T))


# ============================================================
# 発展課題: 雑音除去
# ============================================================
print("\n" + "=" * 60)
print("発展課題: SVDによる雑音除去")
print("=" * 60)


def denoise_svd(signal, k):
    """
    SVD低ランク近似で時系列の雑音を除去
    signal: 1次元時系列
    k: 保持する特異値の数
    """
    # 1. ハンケル行列を構築
    # 2. SVD
    # 3. 低ランク近似
    # 4. 対角平均で時系列に戻す
    pass


# t = np.linspace(0, 4*np.pi, 200)
# clean = np.sin(t) + 0.5 * np.sin(3*t)
# noisy = clean + np.random.randn(200) * 0.3
# denoised = denoise_svd(noisy, k=4)

# Q: k を増やすと結果はどう変わるか？
