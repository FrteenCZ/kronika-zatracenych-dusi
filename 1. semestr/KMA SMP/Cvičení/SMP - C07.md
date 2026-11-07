---
type: exercise
status: todo
katedra: KMA
date: 03-11-2026
---

> **Téma:** Hodnost, inverzní matice
> **Koncepty:**
> **Zdroj**: 4.pdf

# 1
vystupňovat → počet nenulových řádků = hodnost

---

${}\mathbf{A}^{-1}:\mathbf{A}\mathbf{A}^{-1}=\mathbf{A}^{-1}\mathbf{A}=\mathbf{I}{}$

# 1
${}\mathbf{A}\mathbf{X}=\mathbf{B}{}$

${}\mathbf{A}=\begin{bmatrix}2 & 3 \\  4 & -1\end{bmatrix}{}$

${}\mathbf{B}=\begin{bmatrix}2 & 1 \\  3 & 0\end{bmatrix}{}$


pokud je ${}\mathbf{A}{}$ singulární ${}\nexists \mathbf{A}^{-1}{}$


$$
\begin{align}
\mathbf{A}^{-1}\mathbf{AX}=\mathbf{A}^{-1}\mathbf{B} \\
\mathbf{X}=\mathbf{A}^{-1}\mathbf{B}
\end{align}
$$
${}\det \mathbf{A}=-14\implies \mathbf{A} \text{ je regulární }\impliedby \mathrm{h}(\mathbf{A})=2{}$

I)
$$
\begin{align}
\begin{bmatrix*}[cc|cc]
2 & 3 & 1 & 0 \\
4 & -1 & 0 & 1
\end{bmatrix*}\sim\begin{bmatrix*}[cc|cc]
2 & 3 & 1 & 0 \\
0 & -7 & -2 & 1
\end{bmatrix*}\sim\begin{bmatrix*}[cc|cc]
1 & \frac{3}{2} & \frac{1}{2} & 0 \\
0 & 1 & \frac{2}{7} & -\frac{1}{7}
\end{bmatrix*}\sim\begin{bmatrix*}[cc|cc]
1 & 0 & \frac{1}{14} & \frac{3}{14} \\
0 & 1 & \frac{2}{7} & -\frac{1}{7}
\end{bmatrix*} \\
\mathbf{A}^{-1}=\frac{1}{14}\begin{bmatrix}
1 & 3 \\
4 & -2
\end{bmatrix}
\end{align}
$$

II)
$$
\begin{align}
\mathbf{A}^{-1}=\frac{1}{\det \mathbf{A}}\cdot \mathbf{A}^{\mathbf{A}}=-\frac{1}{14}\cdot \begin{bmatrix}
-1 & -4 \\
-3 & 2
\end{bmatrix}^T=-\frac{1}{14}\begin{bmatrix}
-1 & -3 \\
-4 & 2
\end{bmatrix}
\end{align}
$$

$$
\begin{align}
\mathbf{X}=\frac{1}{14}\begin{bmatrix}
1 & 3 \\
4 & -2
\end{bmatrix}\begin{bmatrix}
2 & 1 \\
3 & 0
\end{bmatrix}=\frac{1}{14}\begin{bmatrix}
11 & 1 \\
2 & 4
\end{bmatrix}
\end{align}
$$
# 2
${}\mathbf{A}=\begin{bmatrix}2 & 1 & 2 \\  3 & 1 & 2 \\  -1 & -1 & -2\end{bmatrix}{}$
${}\det \mathbf{A}=0\implies \nexists \mathbf{A}^{-1}{}$

# 3
${}\mathbf{A}=\begin{bmatrix}2 & 9 & -5 \\  0 & 2 & -1 \\  1 & 3 & -2\end{bmatrix}{}$

I)
$$
\begin{align}
\begin{bmatrix*}[ccc|ccc]
2 & 9 & -5 & 1 & 0 & 0\\
0 & 2 & -1 & 0 & 1 & 0 \\
1 & 3 & -2 & 0 & 0 & 1
\end{bmatrix*}\sim\begin{bmatrix*}[ccc|ccc]
1 & 3 & -2 & 0 & 0 & 1\\
0 & 2 & -1 & 0 & 1 & 0 \\
0 & 3 & 1 & 1 & 0 & -2
\end{bmatrix*}\sim\begin{bmatrix*}[ccc|ccc]
1 & 3 & -2 & 0 & 0 & 1\\
0 & 1 & -\frac{1}{2} & 0 & \frac{1}{2} & 0 \\
0 & 0 & \frac{5}{2} & 1 & -\frac{3}{2} & -2
\end{bmatrix*}\sim \\
\sim\begin{bmatrix*}[ccc|ccc]
1 & 3 & -2 & 0 & 0 & 1\\
0 & 1 & -\frac{1}{2} & 0 & \frac{1}{2} & 0 \\
0 & 0 & 1 & \frac{2}{5} & -\frac{3}{5} & -\frac{1}{5}
\end{bmatrix*}\dots
\end{align}
$$

II)
$$
\begin{align}
\mathbf{A}^{-1}=\frac{1}{-1}\begin{bmatrix}
-1 & -1 & -2 \\
3 & 1 & 3 \\
1 & 2 & 4
\end{bmatrix}^T=\begin{bmatrix}
1 & -3 & -1 \\
1 & -1 & -2 \\
2 & -3 & -4
\end{bmatrix}
\end{align}
$$

---

${}\mathbf{A}=\begin{bmatrix}3 & 4 \\  -2 & 5\end{bmatrix}{}$


$$
\begin{align}
\mathbf{A}^{-1}=\frac{1}{\det \mathbf{A}}\mathbf{A}^{\mathbf{A}}=\frac{1}{23}\begin{bmatrix}
5 & -4 \\
2 & 3
\end{bmatrix}
\end{align}
$$