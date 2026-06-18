"""
図4: PCAと固有値分解の可視化

使い方:
    python figures/fig-04-pca.py

生成される図:
    fig-04a_pca_iris.png      — IrisデータセットのPCA
    fig-04b_eigenvalues.png   — 固有値の減衰（スクリープロット）
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris


def plot_pca_iris():
    """IrisデータセットのPCA可視化"""
    iris = load_iris()
    X = iris.data
    y = iris.target

    # PCA
    X_centered = X - X.mean(axis=0)
    U, s, Vt = np.linalg.svd(X_centered, full_matrices=False)
    X_pca = X_centered @ Vt[:2].T

    fig, ax = plt.subplots(figsize=(8, 6))

    colors = ["blue", "red", "green"]
    targets = iris.target_names

    for label, color, name in zip([0, 1, 2], colors, targets, strict=False):
        mask = y == label
        ax.scatter(
            X_pca[mask, 0],
            X_pca[mask, 1],
            c=color,
            label=name,
            alpha=0.7,
            s=50,
            edgecolors="black",
            linewidth=0.5,
        )

    # 主成分の方向を矢印で表示
    for i in range(2):
        ax.arrow(
            0,
            0,
            Vt[i, 0] * 4,
            Vt[i, 1] * 4,
            head_width=0.2,
            head_length=0.2,
            fc="black",
            ec="black",
            alpha=0.5,
        )

    ax.set_xlabel("第1主成分", fontsize=12)
    ax.set_ylabel("第2主成分", fontsize=12)
    ax.set_title("IrisデータセットのPCA", fontsize=14)
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)
    ax.set_aspect("equal")

    plt.tight_layout()
    plt.savefig("figures/fig-04a_pca_iris.png", dpi=150)


def plot_scree():
    """スクリープロット（固有値の減衰）"""
    iris = load_iris()
    X = iris.data
    X_centered = X - X.mean(axis=0)

    U, s, Vt = np.linalg.svd(X_centered, full_matrices=False)
    variance_ratio = s**2 / np.sum(s**2)
    cumulative = np.cumsum(variance_ratio)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # 個別寄与率
    ax1 = axes[0]
    ax1.bar(range(1, len(variance_ratio) + 1), variance_ratio, color="steelblue", alpha=0.7)
    ax1.plot(range(1, len(variance_ratio) + 1), variance_ratio, "ro-", markersize=8)
    ax1.set_xlabel("主成分", fontsize=12)
    ax1.set_ylabel("寄与率", fontsize=12)
    ax1.set_title("各主成分の寄与率", fontsize=13)
    ax1.set_xticks(range(1, len(variance_ratio) + 1))
    ax1.grid(True, alpha=0.3)

    # 累積寄与率
    ax2 = axes[1]
    ax2.bar(range(1, len(cumulative) + 1), cumulative, color="coral", alpha=0.7)
    ax2.plot(range(1, len(cumulative) + 1), cumulative, "bo-", markersize=8)
    ax2.axhline(0.9, color="red", linestyle="--", alpha=0.5, label="90% 基準")
    ax2.set_xlabel("主成分数", fontsize=12)
    ax2.set_ylabel("累積寄与率", fontsize=12)
    ax2.set_title("累積寄与率", fontsize=13)
    ax2.set_xticks(range(1, len(cumulative) + 1))
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("figures/fig-04b_eigenvalues.png", dpi=150)


if __name__ == "__main__":
    plot_pca_iris()
    plot_scree()
    print("図を生成しました: figures/fig-04*.png")
