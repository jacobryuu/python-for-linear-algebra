"""
図1: ベクトル演算の可視化

使い方:
    python figures/fig-01-vector-ops.py

生成される図:
    fig-01a_vector_add.png  — ベクトル加法（平行四边形）
    fig-01b_dot_product.png — ドット積と角度の関係
"""

import matplotlib.pyplot as plt
import numpy as np


def plot_vector_add():
    """ベクトル加法の可視化"""
    fig, ax = plt.subplots(figsize=(6, 6))

    v = np.array([2, 3])
    w = np.array([4, 1])

    # 原点からのベクトル
    ax.quiver(
        0,
        0,
        v[0],
        v[1],
        angles="xy",
        scale_units="xy",
        scale=1,
        color="blue",
        label="v",
        width=0.05,
    )
    ax.quiver(
        0, 0, w[0], w[1], angles="xy", scale_units="xy", scale=1, color="red", label="w", width=0.05
    )

    # 平行移動したベクトル（平行四边形）
    ax.quiver(
        v[0],
        v[1],
        w[0],
        w[1],
        angles="xy",
        scale_units="xy",
        scale=1,
        color="red",
        alpha=0.3,
        width=0.03,
    )
    ax.quiver(
        w[0],
        w[1],
        v[0],
        v[1],
        angles="xy",
        scale_units="xy",
        scale=1,
        color="blue",
        alpha=0.3,
        width=0.03,
    )

    # 和ベクトル
    v_plus_w = v + w
    ax.quiver(
        0,
        0,
        v_plus_w[0],
        v_plus_w[1],
        angles="xy",
        scale_units="xy",
        scale=1,
        color="green",
        label="v + w",
        width=0.05,
        linestyle="dashed",
    )

    ax.set_xlim(-1, 7)
    ax.set_ylim(-1, 5)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=12)
    ax.set_title("ベクトル加法 (平行四边形則)", fontsize=14)
    plt.tight_layout()
    plt.savefig("figures/fig-01a_vector_add.png", dpi=150)


def plot_dot_product():
    """ドット積と角度の関係"""
    fig, ax = plt.subplots(figsize=(6, 6))

    angles = [30, 60, 90, 120]
    colors = ["blue", "green", "red", "purple"]

    v = np.array([3, 0])

    for i, theta_deg in enumerate(angles):
        theta = np.radians(theta_deg)
        w = np.array([3 * np.cos(theta), 3 * np.sin(theta)])
        dot = np.dot(v, w)

        ax.quiver(
            0,
            0,
            w[0],
            w[1],
            angles="xy",
            scale_units="xy",
            scale=1,
            color=colors[i],
            label=f"θ={theta_deg}°, v·w={dot:.1f}",
            width=0.04,
            alpha=0.7,
        )

    ax.quiver(
        0,
        0,
        v[0],
        v[1],
        angles="xy",
        scale_units="xy",
        scale=1,
        color="black",
        label="v",
        width=0.05,
    )

    ax.set_xlim(-1, 4)
    ax.set_ylim(-1, 4)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=10)
    ax.set_title("ドット積 v·w = ||v|| ||w|| cosθ", fontsize=14)
    plt.tight_layout()
    plt.savefig("figures/fig-01b_dot_product.png", dpi=150)


if __name__ == "__main__":
    plot_vector_add()
    plot_dot_product()
    print("図を生成しました: figures/fig-01a_vector_add.png, fig-01b_dot_product.png")
