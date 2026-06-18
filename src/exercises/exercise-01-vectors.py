"""
モジュール1 演習: ベクトルとベクトル空間
"""

import numpy as np

# ============================================================
# 演習1: ベクトル演算の実装
# ============================================================
print("=" * 60)
print("演習1: ベクトル演算をゼロから実装")
print("=" * 60)


def vector_add(v, w):
    """2つのベクトルの加算"""
    return [v[i] + w[i] for i in range(len(v))]


def vector_sub(v, w):
    """2つのベクトルの減算"""
    # ここを実装
    pass


def scalar_mul(c, v):
    """ベクトルのスカラー倍"""
    # ここを実装
    pass


def dot_product(v, w):
    """ドット積"""
    # ここを実装
    pass


def norm(v):
    """L2ノルム"""
    # ここを実装
    pass


# テスト
v = [1, 2, 3]
w = [4, 5, 6]
print(f"v + w = {vector_add(v, w)} (期待値: [5, 7, 9])")
# print(f"v - w = {vector_sub(v, w)}")
# print(f"3 * v = {scalar_mul(3, v)}")
# print(f"v・w = {dot_product(v, w)} (期待値: 32)")
# print(f"||v|| = {norm(v):.2f} (期待値: 3.74)")


# ============================================================
# 演習2: コサイン類似度による類似ユーザー検索
# ============================================================
print("\n" + "=" * 60)
print("演習2: コサイン類似度による類似ユーザー検索")
print("=" * 60)


def cosine_similarity(v, w):
    """コサイン類似度"""
    # ここを実装（np.dot と np.linalg.norm を使ってよい）
    pass


# 5ユーザーの4ジャンル評価ベクトル
users = {
    "A": np.array([5, 1, 4, 2]),
    "B": np.array([1, 5, 2, 4]),
    "C": np.array([4, 2, 5, 1]),
    "D": np.array([5, 1, 3, 3]),
    "E": np.array([2, 5, 1, 5]),
}

target = "A"
print(f"ユーザー{target}との類似度:")
# for name, vec in users.items():
#     if name != target:
#         sim = cosine_similarity(users[target], vec)
#         print(f"  {name}: {sim:.3f}")

# Q: 誰が最も似ている？最も似ていないのは？


# ============================================================
# 演習3: 線形独立の判定
# ============================================================
print("\n" + "=" * 60)
print("演習3: ベクトル集合の線形独立判定")
print("=" * 60)


def is_independent(vectors):
    """
    ベクトル集合が線形独立か判定する
    vectors: list of np.array
    """
    # ヒント: np.linalg.matrix_rank と列数（ベクトル数）を比較
    # ここを実装
    pass


# テスト
v1 = np.array([1, 0, 0])
v2 = np.array([0, 1, 0])
v3 = np.array([0, 0, 1])
v4 = np.array([1, 1, 1])

# print(f"{{v1, v2, v3}}: 独立={is_independent([v1, v2, v3])} (期待値: True)")
# print(f"{{v1, v2, v4}}: 独立={is_independent([v1, v2, v4])} (期待値: True)")
# print(f"{{v1, v2, v3, v4}}: 独立={is_independent([v1, v2, v3, v4])} (期待値: False)")


# ============================================================
# 演習4: 画像のベクトル表現と平均画像
# ============================================================
print("\n" + "=" * 60)
print("演習4: 画像のベクトル表現")
print("=" * 60)

# 10枚の 8×8 画像をシミュレート
np.random.seed(42)
images = np.random.rand(10, 8, 8)  # 10枚の8×8画像

# (a) 各画像をベクトルにフラット化
# ここを実装

# (b) 全画像の平均ベクトルを計算
# ここを実装

# (c) 各画像から平均を引く（中心化）
# ここを実装

# print(f"元の形状: {images.shape}")
# print(f"フラット化後の形状: {flattened.shape}")
# print(f"平均ベクトルの形状: {mean_vector.shape}")


# ============================================================
# 演習5: ノルム比較
# ============================================================
print("\n" + "=" * 60)
print("演習5: 様々なノルムの比較")
print("=" * 60)


def l1_norm(v):
    return np.sum(np.abs(v))


def l2_norm(v):
    return np.sqrt(np.sum(v**2))


def linf_norm(v):
    return np.max(np.abs(v))


v = np.array([3, -4, 5])
# print(f"L1: {l1_norm(v)} (期待値: 12)")
# print(f"L2: {l2_norm(v):.2f} (期待値: 7.07)")
# print(f"Linf: {linf_norm(v)} (期待値: 5)")

# スパースなベクトルと密なベクトルでノルムを比較
sparse = np.array([1, 0, 0, 0, 0, 0, 0, 0])
dense = np.ones(8) / np.sqrt(8)  # L2ノルムが1になるよう正規化

# Q: L1ノルムで比較するとどちらが大きいか？L2ノルムでは？
# print(f"sparse L1: {l1_norm(sparse):.2f}, L2: {l2_norm(sparse):.2f}")
# print(f"dense  L1: {l1_norm(dense):.2f}, L2: {l2_norm(dense):.2f}")


# ============================================================
# 発展課題
# ============================================================
print("\n" + "=" * 60)
print("発展課題: グラム・シュミットの直交化")
print("=" * 60)


def gram_schmidt(vectors):
    """
    グラム・シュミットの直交化
    vectors: list of np.array（線形独立と仮定）
    戻り値: 正規直交基底（list of np.array）
    """
    # 直交化 → 正規化 の順で実装
    pass


# 3次元空間の3つのベクトル
a1 = np.array([1, 1, 0])
a2 = np.array([1, 0, 1])
a3 = np.array([0, 1, 1])

# orthonormal = gram_schmidt([a1, a2, a3])
# for i, q in enumerate(orthonormal):
#     print(f"q{i+1}: {q}")
#     print(f"  ||q|| = {np.linalg.norm(q):.2f}")

# 直交性の確認
# for i in range(3):
#     for j in range(i+1, 3):
#         dp = np.dot(orthonormal[i], orthonormal[j])
#         print(f"  q{i+1}・q{j+1} = {dp:.2f} (期待値: 0)")
