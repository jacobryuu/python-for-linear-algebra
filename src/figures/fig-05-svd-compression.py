"""
図5: SVD低ランク近似による画像圧縮

使い方:
    python figures/fig-05-svd-compression.py

生成される図:
    fig-05_svd_compression.png  — ランクkを変えたときの復元結果
"""

import matplotlib.pyplot as plt
import numpy as np


def create_test_image(n=128):
    """テスト用の人工画像（チェッカーボード + 円 + テキスト風）"""
    img = np.zeros((n, n))

    # チェッカーボード
    for i in range(n):
        for j in range(n):
            if (i // 16 + j // 16) % 2 == 0:
                img[i, j] = 0.8

    # 円
    cx, cy, r = n / 2, n / 2, n / 3
    for i in range(n):
        for j in range(n):
            d = np.sqrt((i - cx) ** 2 + (j - cy) ** 2)
            if d < r:
                img[i, j] = 0.3
            if d < r * 0.6:
                img[i, j] = 0.6

    return img


def plot_compression():
    """SVD圧縮の可視化"""
    img = create_test_image(128)
    U, s, Vt = np.linalg.svd(img, full_matrices=False)

    ranks = [1, 2, 5, 10, 20, 50]

    fig, axes = plt.subplots(2, 4, figsize=(16, 8))
    axes = axes.ravel()

    # 元画像
    axes[0].imshow(img, cmap="gray", vmin=0, vmax=1)
    axes[0].set_title(f"Original (rank={len(s)})", fontsize=12)
    axes[0].axis("off")

    for idx, k in enumerate(ranks):
        compressed = U[:, :k] @ np.diag(s[:k]) @ Vt[:k, :]
        error = np.linalg.norm(img - compressed) / np.linalg.norm(img)
        ratio = (128 * k + k + k * 128) / (128 * 128)

        axes[idx + 1].imshow(compressed, cmap="gray", vmin=0, vmax=1)
        axes[idx + 1].set_title(f"rank={k}\nerror={error:.2%}, ratio={ratio:.1%}", fontsize=10)
        axes[idx + 1].axis("off")

    # Hide unused subplot
    axes[-1].axis("off")

    plt.tight_layout()
    plt.savefig("figures/fig-05_svd_compression.png", dpi=150)

    plt.tight_layout()
    plt.savefig("figures/fig-05_svd_compression.png", dpi=150)


def plot_singular_values():
    """特異値の分布"""
    img = create_test_image(128)
    U, s, Vt = np.linalg.svd(img, full_matrices=False)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # 特異値の絶対値
    ax1 = axes[0]
    ax1.semilogy(s[:50], "b.-", markersize=6)
    ax1.set_xlabel("i", fontsize=12)
    ax1.set_ylabel("σ_i", fontsize=12)
    ax1.set_title("上位50個の特異値 (対数軸)", fontsize=13)
    ax1.grid(True, alpha=0.3)

    # 累積寄与率
    ax2 = axes[1]
    cumsum = np.cumsum(s) / np.sum(s)
    ax2.plot(cumsum[:50], "r.-", markersize=6)
    ax2.axhline(0.9, color="gray", linestyle="--", alpha=0.7, label="90%")
    ax2.axhline(0.99, color="gray", linestyle=":", alpha=0.7, label="99%")
    ax2.set_xlabel("k", fontsize=12)
    ax2.set_ylabel("累積寄与率", fontsize=12)
    ax2.set_title("特異値の累積寄与率", fontsize=13)
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("figures/fig-05_singular_values.png", dpi=150)


if __name__ == "__main__":
    plot_compression()
    plot_singular_values()
    print("図を生成しました: figures/fig-05*.png")
