"""
モジュール6 演習: 機械学習応用総合
"""

import numpy as np
from sklearn.datasets import load_digits, load_iris

# ============================================================
# 演習1: PCAによる次元削減と可視化
# ============================================================
print("=" * 60)
print("演習1: IrisデータセットのPCA")
print("=" * 60)

iris = load_iris()
X, y = iris.data, iris.target


def pca_manual(X, n_components=2):
    """スクラッチでPCA"""
    # 1. 中心化
    # 2. 共分散行列 or SVD
    # 3. 上位 n_components 個の主成分に射影
    # ここを実装
    pass


# X_pca = pca_manual(X, 2)
# print(f"PCA後の形状: {X_pca.shape}")
# print("最初の5サンプル:\n", X_pca[:5])


# ============================================================
# 演習2: 単語埋め込みのベクトル演算
# ============================================================
print("\n" + "=" * 60)
print("演習2: 単語埋め込みのアナロジー")
print("=" * 60)

# 擬似的な単語ベクトル（実際は300次元など）
words = {
    "tokyo": np.array([0.9, 0.1, 0.8, 0.2, 0.3]),
    "japan": np.array([0.8, 0.9, 0.7, 0.1, 0.2]),
    "paris": np.array([0.9, 0.2, 0.1, 0.8, 0.3]),
    "france": np.array([0.8, 0.9, 0.2, 0.7, 0.2]),
    "london": np.array([0.8, 0.1, 0.2, 0.1, 0.9]),
    "uk": np.array([0.7, 0.9, 0.1, 0.2, 0.8]),
}


def cosine_similarity(v, w):
    return np.dot(v, w) / (np.linalg.norm(v) * np.linalg.norm(w))


# "日本 : 東京 = フランス : ?" のアナロジー
# query = words["tokyo"] - words["japan"] + words["france"]
# print("tokyo - japan + france に最も近い単語:")
# for name, vec in words.items():
#     sim = cosine_similarity(query, vec)
#     print(f"  {name}: {sim:.3f}")
# Q: 何が最も近いか？期待通りか？


# ============================================================
# 演習3: 行列因子分解による推薦
# ============================================================
print("\n" + "=" * 60)
print("演習3: 行列因子分解")
print("=" * 60)


class MatrixFactorization:
    """SGDによる行列因子分解"""

    def __init__(self, n_factors=3, lr=0.01, reg=0.02, n_epochs=100):
        self.n_factors = n_factors
        self.lr = lr
        self.reg = reg
        self.n_epochs = n_epochs

    def fit(self, ratings):
        """ratings: (m, n) 行列, 0は欠損値"""
        self.m, self.n = ratings.shape
        self.P = np.random.randn(self.m, self.n_factors) * 0.1
        self.Q = np.random.randn(self.n, self.n_factors) * 0.1

        for epoch in range(self.n_epochs):
            loss = 0
            for i in range(self.m):
                for j in range(self.n):
                    if ratings[i, j] > 0:  # 観測値のみ
                        # 予測誤差
                        # err = ratings[i,j] - P[i] @ Q[j]
                        # SGD更新
                        # P[i] += lr * (err * Q[j] - reg * P[i])
                        # Q[j] += lr * (err * P[i] - reg * Q[j])
                        # loss += err**2
                        pass
            if epoch % 20 == 0:
                print(f"  epoch {epoch}: loss = {loss:.4f}")

        return self

    def predict(self):
        return self.P @ self.Q.T


# 小さな評価行列
# R = np.array([
#     [5, 3, 0, 1],
#     [4, 0, 0, 1],
#     [1, 1, 0, 5],
#     [1, 0, 0, 4],
#     [0, 1, 5, 4],
# ], dtype=float)

# mf = MatrixFactorization(n_factors=2, n_epochs=100)
# mf.fit(R)
# pred = mf.predict()
# print("予測評価:\n", np.round(pred, 1))


# ============================================================
# 演習4: Attention機構
# ============================================================
print("\n" + "=" * 60)
print("演習4: Scaled Dot-Product Attention")
print("=" * 60)


def attention(Q, K, V):
    """
    Attention(Q, K, V) = softmax(Q @ K.T / sqrt(d_k)) @ V
    Q: (seq_len, d_k)
    K: (seq_len, d_k)
    V: (seq_len, d_v)
    """
    # ここを実装
    pass


# d_k = 4
# d_v = 4
# seq_len = 3

# Q = np.random.randn(seq_len, d_k)
# K = np.random.randn(seq_len, d_k)
# V = np.random.randn(seq_len, d_v)

# output, weights = attention(Q, K, V)
# print("注意重み:\n", np.round(weights, 3))
# print("各行の和:", weights.sum(axis=-1))  # すべて1になるはず


# ============================================================
# 演習5: 総合問題 — 手書き数字の分類
# ============================================================
print("\n" + "=" * 60)
print("演習5: 手書き数字の分類パイプライン")
print("=" * 60)

digits = load_digits()
X, y = digits.data, digits.target

# ステップ1: 訓練/テスト分割
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ステップ2: PCAで次元削減（16次元に）
# ここを実装


# ステップ3: ソフトマックス回帰で分類
class SoftmaxRegression:
    def __init__(self, n_features, n_classes, lr=0.1):
        self.W = np.random.randn(n_features, n_classes) * 0.01
        self.b = np.zeros(n_classes)
        self.lr = lr

    def softmax(self, Z):
        expZ = np.exp(Z - Z.max(axis=1, keepdims=True))
        return expZ / expZ.sum(axis=1, keepdims=True)

    def forward(self, X):
        return self.softmax(X @ self.W + self.b)

    def train_step(self, X, y_onehot):
        self.forward(X)
        # 勾配: dL/dW = X^T @ (probs - y_onehot) / N
        # ここを実装
        pass

    def accuracy(self, X, y):
        preds = np.argmax(self.forward(X), axis=1)
        return (preds == y).mean()


# ステップ4: 訓練と評価
# model = SoftmaxRegression(n_features=16, n_classes=10, lr=0.1)
# for epoch in range(500):
#     model.train_step(X_train_pca, y_train_onehot)
# print(f"訓練精度: {model.accuracy(X_train_pca, y_train):.1%}")
# print(f"テスト精度: {model.accuracy(X_test_pca, y_test):.1%}")


# ============================================================
# 発展課題: 簡単なTransformerブロック
# ============================================================
print("\n" + "=" * 60)
print("発展課題: SimpleTransformerBlock")
print("=" * 60)


class SimpleTransformerBlock:
    """1ヘッドのTransformerブロック（注意 + FFN）"""

    def __init__(self, d_model, d_ff):
        # 注意機構の重み
        self.W_q = np.random.randn(d_model, d_model) * 0.01
        self.W_k = np.random.randn(d_model, d_model) * 0.01
        self.W_v = np.random.randn(d_model, d_model) * 0.01
        self.W_o = np.random.randn(d_model, d_model) * 0.01

        # FFNの重み
        self.W_1 = np.random.randn(d_model, d_ff) * 0.01
        self.W_2 = np.random.randn(d_ff, d_model) * 0.01

    def forward(self, X):
        # 1. 自己注意
        # Q = X @ W_q, K = X @ W_k, V = X @ W_v
        # attn_out = attention(Q, K, V)
        # X = X + attn_out

        # 2. Feed Forward
        # ff_out = relu(X @ W_1) @ W_2
        # X = X + ff_out
        pass
