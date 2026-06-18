"""
図2: 線形変換の可視化

使い方:
    python figures/fig-02-linear-transform.py

生成される図:
    fig-02a_rotation.png   — 回転変換
    fig-02b_shear.png      — せん断変換
    fig-02c_eigen.png      — 固有ベクトルの方向（変換後も向き不変）
"""

import matplotlib.pyplot as plt
import numpy as np


def plot_rotation():
    """回転変換の可視化"""
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    # 元のグリッド
    x = np.arange(-5, 6)
    y = np.arange(-5, 6)
    X, Y = np.meshgrid(x, y)

    for idx, (theta_deg, title) in enumerate(
        [(0, "元のグリッド"), (45, "45°回転"), (90, "90°回転")]
    ):
        ax = axes[idx]
        theta = np.radians(theta_deg)
        R = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])

        # グリッド点を変換
        XY = np.stack([X.ravel(), Y.ravel()])
        XY_t = R @ XY
        X_t = XY_t[0].reshape(X.shape)
        Y_t = XY_t[1].reshape(Y.shape)

        # グリッド線を描画
        for i in range(len(x)):
            ax.plot(X_t[i, :], Y_t[i, :], "b-", alpha=0.3, lw=0.5)
            ax.plot(X_t[:, i], Y_t[:, i], "b-", alpha=0.3, lw=0.5)

        ax.set_xlim(-6, 6)
        ax.set_ylim(-6, 6)
        ax.set_aspect("equal")
        ax.grid(True, alpha=0.2)
        ax.set_title(title, fontsize=13)
        ax.axhline(0, color="black", lw=0.5)
        ax.axvline(0, color="black", lw=0.5)

    plt.tight_layout()
    plt.savefig("figures/fig-02a_rotation.png", dpi=150)


def plot_shear():
    """せん断変換の可視化"""
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    # 単位正方形
    square = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]]).T

    for idx, (k, title) in enumerate([(0, "元の正方形 (k=0)"), (1.5, "せん断変換 (k=1.5)")]):
        ax = axes[idx]
        S = np.array([[1, k], [0, 1]])
        transformed = S @ square

        ax.fill(transformed[0], transformed[1], alpha=0.3, color="blue")
        ax.plot(transformed[0], transformed[1], "b-", lw=2)

        ax.set_xlim(-0.5, 3)
        ax.set_ylim(-0.5, 2)
        ax.set_aspect("equal")
        ax.grid(True, alpha=0.3)
        ax.set_title(title, fontsize=13)
        ax.axhline(0, color="black", lw=0.5)
        ax.axvline(0, color="black", lw=0.5)

    plt.tight_layout()
    plt.savefig("figures/fig-02b_shear.png", dpi=150)


def plot_eigen_direction():
    """固有ベクトル（変換後も方向不変）の可視化"""
    fig, ax = plt.subplots(figsize=(6, 6))

    A = np.array([[2, 1], [1, 2]])
    vals, vecs = np.linalg.eig(A)

    # 単位円上の点
    theta = np.linspace(0, 2 * np.pi, 100)
    circle = np.array([np.cos(theta), np.sin(theta)])

    # 変換後の図形
    ellipse = A @ circle

    ax.plot(circle[0], circle[1], "b-", alpha=0.5, label="単位円")
    ax.plot(ellipse[0], ellipse[1], "r-", alpha=0.5, label="変換後")

    # 固有ベクトルの方向
    for i in range(2):
        v = vecs[:, i]
        λ = vals[i]
        ax.quiver(
            0,
            0,
            v[0],
            v[1],
            angles="xy",
            scale_units="xy",
            scale=1,
            color="green",
            width=0.05,
            label=f"固有ベクトル v{i + 1}",
        )
        ax.quiver(
            0,
            0,
            λ * v[0],
            λ * v[1],
            angles="xy",
            scale_units="xy",
            scale=1,
            color="purple",
            width=0.05,
            label=f"変換後 λv{i + 1}",
            alpha=0.7,
        )

    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=10)
    ax.set_title("固有ベクトル: 変換後も方向が変わらない", fontsize=13)
    ax.axhline(0, color="black", lw=0.5)
    ax.axvline(0, color="black", lw=0.5)

    plt.tight_layout()
    plt.savefig("figures/fig-02c_eigen.png", dpi=150)


if __name__ == "__main__":
    plot_rotation()
    plot_shear()
    plot_eigen_direction()
    print("図を生成しました: figures/fig-02*.png")
