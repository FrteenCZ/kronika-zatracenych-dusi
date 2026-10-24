---
type: exercise
status: todo
katedra: KMA
date: 20-10-2026
---

> **Téma:** 
> **Koncepty:** [[Lineární prostory]]

LP - lineární prostor
- ${}\mathbb{R}_{n}{}$ → grupa ale není těleso → operace násobení pouze číslem
- ${}\mathbf{M}_{m,n}{}$
- ${}P_{n}{}$ polynom stupně ${}\leq n{}$



---
$$
\mathbb{R}_{3}:\begin{aligned}
&u_{1}=[2,3,1]^T\\
&u_{2}=[-1,2,-2]^T\\
&u_{3}=[1,5,-1]^T
\end{aligned}
$$

$$
\begin{aligned}
k_{1}u_{1}+k_{2}u_{2}+k_{3}u_{3}=\mathbb{0}\\
k_{1}\begin{bmatrix}
2 \\
3 \\
1
\end{bmatrix}+k_{2}\begin{bmatrix}
-1 \\
2 \\
-2
\end{bmatrix}+k_{3}\begin{bmatrix}
1 \\
5 \\
-1
\end{bmatrix}=\begin{bmatrix}
0 \\
0 \\
0
\end{bmatrix}
\end{aligned}
$$


$$
\begin{bmatrix*}[ccc|c]
2 & -1 & 1 & 0 \\
3 & 2 & 5 & 0 \\
1 & -2 & -1 & 0
\end{bmatrix*}\sim \begin{bmatrix*}[ccc|c]
1 & -2 & -1 & 0\\
0 & 1 &1 & 0 \\
0 & 0 & 0 & 0
\end{bmatrix*}
$$
---

Př.:

$$
P_{2}: 
\begin{aligned}
&p_{1}(x)=x^{2}+2x-3 \\
&p_{2}(x)=2x^{2}+3x-1 \\
& p_{3}(x)=x^{2}+x-2
\end{aligned}
$$

$$
\begin{align}
k_{1}p_{1}+k_{2}p_{2}+k_{3}p_{3}=\mathbb{0} \\
k_{1}(x^{2}+2x-3)+k_{2}(2x^{2}+3x-1)+k_{3}(x^{2}+x-2)=0 \\
x^{2}(k_{1}+2k_{2}+k_{3})+x(2k_{1}+3k_{2}+k_{3})+(-3k_{1}-k_{2}-2k_{3})=0 \\
 \\
k_{1}+2k_{2}+k_{3}=0 \\
2k_{1}+3k_{2}+k_{3}=0 \\
-3k_{1}-k_{2}-2k_{3}=0 \\
 \\
\begin{bmatrix*}[ccc|c]
1 & 2 & 1 & 0 \\
2 & 3 & 1 & 0 \\
-3 & -1 & -2 & 0
\end{bmatrix*}\sim \begin{bmatrix*}[ccc|c]
1 & 3 & 1 & 0 \\
0 & -1 & -1 & 0 \\
0 & 5 & 1 & 0
\end{bmatrix*}\sim \begin{bmatrix*}[ccc|c]
1 & 3 & 1 & 0 \\
0 & 1 & 1 & 0 \\
0 & 0 & 4 & 0
\end{bmatrix*}\implies \text{LN}
\end{align}
$$
---
