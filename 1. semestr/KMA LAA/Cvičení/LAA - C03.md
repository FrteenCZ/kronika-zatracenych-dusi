---
type: exercise
status: todo
date: 06-10-2026
katedra: KMA
---

> **Téma:** 
> **Koncepty:** [[Matice]]

# Nechť ${}\mathbf{A}=\begin{bmatrix}3 & -2 & 1 \\  -1 & 0 & 4\end{bmatrix}{}$, ${}\mathbf{B}=\begin{bmatrix}1 & 2 \\  -2 & 3 \\  0 & 5\end{bmatrix}{}$. Vypočítejte:
- ${}\mathbf{A}\cdot \mathbf{B}{}$

$$
\begin{bmatrix}3 & -2 & 1 \\  -1 & 0 & 4\end{bmatrix}\cdot\begin{bmatrix}1 & 2 \\  -2 & 3 \\  0 & 5\end{bmatrix}{}=\begin{bmatrix}
3+4+0 & 6-6+5 \\
-1+0+0 & -2+0+20
\end{bmatrix}=\begin{bmatrix}
7 & 5 \\
-1 & 18
\end{bmatrix}
$$

- ${}\mathbf{B}\cdot \mathbf{A}{}$

$$
\begin{bmatrix}1 & 2 \\  -2 & 3 \\  0 & 5\end{bmatrix}\cdot\begin{bmatrix}3 & -2 & 1 \\  -1 & 0 & 4\end{bmatrix}=\begin{bmatrix}
3-2 & -2+0 & 1+8 \\
-6-3 & -4+0 & -2+12 \\
0-5 & 0+0 & 0+20
\end{bmatrix}=\begin{bmatrix}
1 & -2 & 9 \\
-9 & -4 & 10 \\
-5 & 0 & 20
\end{bmatrix}
$$
- ${}\mathbf{A}^T\cdot \mathbf{B}^T{}$

$$
\begin{bmatrix}3 & -2 & 1 \\  -1 & 0 & 4\end{bmatrix}^T\cdot\begin{bmatrix}1 & 2 \\  -2 & 3 \\  0 & 5\end{bmatrix}^T=\begin{bmatrix}
3 & -1 \\
-2 & 0 \\
1 & 4
\end{bmatrix}\cdot \begin{bmatrix}
1 & -2 & 0 \\
2 & 3 & 5
\end{bmatrix}=\begin{bmatrix}
1 & -9 & -5 \\
-2 & 4 & 0 \\
9 & 10 & 20
\end{bmatrix}
$$

- ${}\mathbf{B}^T\cdot \mathbf{A}^T{}$

$$
\mathbf{B}^T\cdot \mathbf{A}^T=(\mathbf{A}\cdot \mathbf{B})^T=\begin{bmatrix}
7 & -1 \\
5 & 18
\end{bmatrix}
$$
# Vypočítejte
- 
  $$
  \begin{bmatrix}
  1 & 0 & 0 \\
  0 & 0 & 0 \\
  0 & 0 & 0
  \end{bmatrix}\cdot \begin{bmatrix}
  1 \\
  2 \\
  3
  \end{bmatrix}=\begin{bmatrix}
  1 \\
  0 \\
  0
  \end{bmatrix}
  $$
- 
  $$
  \begin{bmatrix}
  0 & 0 & 0 \\
  0 & 1 & 0
  \end{bmatrix}\cdot \begin{bmatrix}
  1 \\
  2 \\
  3
  \end{bmatrix}=\begin{bmatrix}
  0 \\
  2
  \end{bmatrix}
  $$
- 
  $$
  \begin{bmatrix}
  0 & 0 & 1
  \end{bmatrix}\cdot \begin{bmatrix}
  1 \\
  2 \\
  3
  \end{bmatrix}=\begin{bmatrix}
  3
  \end{bmatrix}
  $$
- 
  $$
  \begin{bmatrix}
  1 & 0 & 0 \\
  0 & -1 & 0 \\
  0 & 0 & 3
  \end{bmatrix}\cdot \begin{bmatrix}
  1 \\
  2 \\
  3
  \end{bmatrix}=\begin{bmatrix}
  1 \\
  -2 \\
  9
  \end{bmatrix}
  $$
- 
  $$
  \begin{bmatrix}
  2 & 0 & 0 \\
  0 & 2 & 0 \\
  0 & 0 & 2
  \end{bmatrix}\cdot \begin{bmatrix}
  1 \\
  2 \\
  3
  \end{bmatrix}=\begin{bmatrix}
  2 \\
  4 \\
  6
  \end{bmatrix}
  $$
- 
  $$
  \begin{bmatrix}
  1 & 0 & 0 \\
  0 & 0 & 1 \\
  0 & 1 & 0
  \end{bmatrix}\cdot \begin{bmatrix}
  1 \\
  2 \\
  3
  \end{bmatrix}=\begin{bmatrix}
  1 \\
  3 \\
  2
  \end{bmatrix}
  $$
- 
  $$
  \begin{bmatrix}
  0 & 0 & 1 \\
  0 & 1 & 0 \\
  1 & 0 & 0
  \end{bmatrix}\cdot \begin{bmatrix}
  1 \\
  2 \\
  3
  \end{bmatrix}=\begin{bmatrix}
  3 \\
  2 \\
  1
  \end{bmatrix}
  $$
- 
  $$
  \begin{bmatrix}
  0 & 0 & 1 \\
  0 & 1 & 0 \\
  1 & 0 & 0
  \end{bmatrix}\cdot \begin{bmatrix}
  1 & 2 & 3 \\
  4 & 5 & 6 \\
  7 & 8 & 9
  \end{bmatrix}=\begin{bmatrix}
  7 & 8 & 9 \\
  4 & 5 & 6 \\
  1 & 2 & 3
  \end{bmatrix}
  $$
- 
  $$
  \begin{bmatrix}
  1 & 2 & 3 \\
  4 & 5 & 6 \\
  7 & 8 & 9
  \end{bmatrix}\cdot \begin{bmatrix}
  0 & 0 & 1 \\
  0 & 1 & 0 \\
  1 & 0 & 0
  \end{bmatrix}=\begin{bmatrix}
  3 & 2 & 1 \\
  6 & 5 & 4 \\
  9 & 8 & 7
  \end{bmatrix}
  $$
- 
  $$
  \begin{bmatrix}
  0 & 0 & 1 \\
  0 & 1 & 0 \\
  1 & 0 & 0
  \end{bmatrix}\cdot \begin{bmatrix}
  1 & 2 & 3 \\
  4 & 5 & 6 \\
  7 & 8 & 9
  \end{bmatrix}\cdot  \begin{bmatrix}
  0 & 0 & 1 \\
  0 & 1 & 0 \\
  1 & 0 & 0
  \end{bmatrix}=\begin{bmatrix}
  7 & 8 & 9 \\
  4 & 5 & 6 \\
  1 & 2 & 3
  \end{bmatrix}\cdot  \begin{bmatrix}
  0 & 0 & 1 \\
  0 & 1 & 0 \\
  1 & 0 & 0
  \end{bmatrix}=\begin{bmatrix}
  9 & 8 & 7 \\
  6 & 5 & 4 \\
  3 & 2 & 1
  \end{bmatrix}
  $$
- 
  $$
  \begin{bmatrix}
  0 & 0 & 1 \\
  0 & 1 & 0 \\
  1 & 0 & 0
  \end{bmatrix}\cdot\begin{bmatrix}
  0 & 0 & 1 \\
  0 & 1 & 0 \\
  1 & 0 & 0
  \end{bmatrix}\cdot\begin{bmatrix}
  1 & 2 & 3 \\
  4 & 5 & 6 \\
  7 & 8 & 9
  \end{bmatrix}=\begin{bmatrix}
  1 & 2 & 3 \\
  4 & 5 & 6 \\
  7 & 8 & 9
  \end{bmatrix}
  $$
- 
  $$
  \begin{bmatrix}
  3 & 0 & 0 \\
  1 & 1 & 0 \\
  0 & -1 & 1 
  \end{bmatrix}\cdot \begin{bmatrix}
  1 & 2 & 3 \\
  4 & 5 & 6 \\
  7 & 8 & 9
  \end{bmatrix}=\begin{bmatrix}
  3 & 6 & 9 \\
  5 & 7 & 9 \\
  3 & 3 & 3
  \end{bmatrix}
  $$
- 
  $$
  \begin{bmatrix}
  1 & 2 & 3 \\
  4 & 5 & 6 \\
  7 & 8 & 9
  \end{bmatrix}\cdot \begin{bmatrix}
  -1 & 0 \\
  1 & -1 \\
  0 & 1
  \end{bmatrix}=\begin{bmatrix}
  1 & 1 \\
  1 & 1 \\
  1 & 1
  \end{bmatrix}
  $$
# Nechť ${}\mathbf{C}=\begin{bmatrix}3 & 3 \\  -3 & 0\end{bmatrix}{}$, ${}\mathbf{D}=\begin{bmatrix}1 & 2 \\  -1 & 1\end{bmatrix}{}$. Najděte
- matici ${}\mathbf{X}{}$ splňující ${}\mathbf{C}=\mathbf{D}\cdot \mathbf{X}{}$

$$
\mathbf{D}^{-1}\mathbf{C}=\mathbf{X}
$$

$$
\mathbf{D}^{-1}=\frac{1}{3}\begin{bmatrix}
1 & -2 \\
1 & 1
\end{bmatrix}
$$

$$
\mathbf{X}=\frac{1}{3}\begin{bmatrix}
1 & -2 \\
1 & 1
\end{bmatrix}\begin{bmatrix}
3 & 3 \\
-3 & 0
\end{bmatrix}=\begin{bmatrix}
1 & -2 \\
1 & 1
\end{bmatrix}\begin{bmatrix}
1 & 1 \\
-1 & 0
\end{bmatrix}=\begin{bmatrix}
3 & 1 \\
0 & 1
\end{bmatrix}
$$
- matici ${}\mathbf{Y}{}$ splňující ${}\mathbf{C}=\mathbf{Y}\cdot \mathbf{D}{}$

$$
\begin{align}
\mathbf{Y}=\mathbf{C}\cdot \mathbf{D}^{-1} \\
\mathbf{Y}=\begin{bmatrix}
1 & 1 \\
-1 & 0
\end{bmatrix}\begin{bmatrix}
1 & -2 \\
1 & 1
\end{bmatrix}=\begin{bmatrix}
2 & -1 \\
-1 & 2
\end{bmatrix}
\end{align}
$$

# Převeďte následující matice na odstupňovaný tvar
- 
  $$
  \begin{bmatrix}
  1 & 4 & 2 & 5 \\
  2 & 11 & 5 & 8 \\
  1 & 7 & 5 & 4
  \end{bmatrix}\sim \begin{bmatrix}
  1 & 4 & 2 & 5 \\
  0 & 3 & 1 & -2 \\
  0 & 3 & 3 & -1
  \end{bmatrix}\sim \begin{bmatrix}
  1 & 4 & 2 & 5 \\
  0 & 3 & 1 & -2 \\
  0 & 0 & 2 & 1
  \end{bmatrix}
  $$
- 
  $$
  \begin{bmatrix}
  1 & 1 & 1 & 1 \\
  1 & 2 & 3 & 4 \\
  3 & 2 & 1 & 0 \\
  -1 & 4 & 9 & 14
  \end{bmatrix}\sim  \begin{bmatrix}
  1 & 1 & 1 & 1 \\
  0 & 1 & 2 & 3 \\
  0 & -1 & -2 & -3 \\
  0 & 5 & 10 & 15
  \end{bmatrix}\sim  \begin{bmatrix}
  1 & 1 & 1 & 1 \\
  0 & 1 & 2 & 3 \\
  0 & 0 & 0 & 0\\
  0 & 0 & 0 & 0
  \end{bmatrix}
  $$
- 
  $$
  \begin{align}
  \begin{bmatrix}
  0 & 2 & \sqrt[5]{ 3 } & -5 & i \\
  \pi^{2} & -e & 0 & \frac{3}{4}i & 13 \\
  0 & 0 & 0 & 0 & 2^{-10} \\
  0 & 0 & 0 & 0 & -\sqrt{ 7 } \\
  0 & 0 & e^\pi & \pi^e & 0
  \end{bmatrix}\sim \begin{bmatrix}
  \pi^{2} & -e & 0 & \frac{3}{4}i & 13 \\
  0 & 2 & \sqrt[5]{ 3 } & -5 & i \\
   0 & 0 & e^\pi & \pi^e & 0 \\
   0 & 0 & 0 & 0 & 2^{-10} \\
    0 & 0 & 0 & 0 & -\sqrt{ 7 }
  \end{bmatrix}\sim \\ \sim \begin{bmatrix}
  \pi^{2} & -e & 0 & \frac{3}{4}i & 13 \\
  0 & 2 & \sqrt[5]{ 3 } & -5 & i \\
   0 & 0 & e^\pi & \pi^e & 0 \\
   0 & 0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0 & 1
  \end{bmatrix}\sim \begin{bmatrix}
  \pi^{2} & -e & 0 & \frac{3}{4}i & 13 \\
  0 & 2 & \sqrt[5]{ 3 } & -5 & i \\
   0 & 0 & e^\pi & \pi^e & 0 \\
   0 & 0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0 & 0
  \end{bmatrix}
  \end{align}
  $$
