---
type: exercise
status: done
katedra: KMA
date: 27-10-2026
---

> **Téma:** Lineární nezávislo, báze prosotoru
> **Koncepty:**
> **Zdroj**: 3.pdf

# 1
${}\mathbb{R}_{4}{}$   ${}\begin{aligned}&u_{1}=[1,1,2,3]^T \\ &u_{2}=[2,0,-1,3]^T \\  &u_{3}=[4,2,1,-3]^T \\  &u_{4}=[5,2,1,2]^T \end{aligned}{}$ : může být ${}\{ u_{1},u_{2},u_{3},u_{4} \}{}$ báze ${}\mathbb{R}_{4}{}$? ANO, pokud jsou LN

${}\alpha_{1}u_{1}+\alpha_{2}u_{2}+\alpha_{3}u_{3}+\alpha_{4}u_{4}=\mathbb{0}{}$
$$
\begin{align}
\begin{bmatrix}
1 & 2 & 4 & 5 \\
1 & 0 & 2 & 2 \\
2 & -1 & 1 & 1 \\
3 & 3 & -3 & 2
\end{bmatrix}\sim\begin{bmatrix}
1 & 2 & 4 & 5 \\
0 & -2 & -2 & -3 \\
0 & -5 & -7 & -9 \\
0 & -3 & -15 & -13
\end{bmatrix}\sim\begin{bmatrix}
1 & 2 & 4 & 5 \\
0 & 1 & 3 & 3 \\
0 & 0 & 4 & 3 \\
0 & 0 & 6 & 4
\end{bmatrix}\sim\begin{bmatrix}
1 & 2 & 4 & 5 \\
0 & 1 & 3 & 3 \\
0 & 0 & 4 & 3 \\
0 & 0 & 0 & 1
\end{bmatrix}
\end{align}
$$

$$
\begin{align}
\alpha_{1}=0 \\
\alpha_{2}=0 \\
\alpha_{3}=0 \\
\alpha_{4}=0
\end{align}\implies \text{LN}
$$

---
# 2
${}P_{3}{}$: ${}\begin{aligned}&p_{1}(x)=3x^{3}+x^{2}+2 \\  &p_{2}(x)=x^{2}+2x-3 \\  &p_{3}(x)=x^{3}+2x+2\end{aligned}{}$ : generují podprostor v ${}P_{3}{}$

Určit bázi a dimenzi ${}P{}$
${}p(x)=x^{3}+x^{2}+x+1\in P{}$?

${}\alpha_{1}p_{1}(x)+\alpha_{2}p_{2}(x)+\alpha_{3}p_{3}(x)=0{}$

$$
\begin{align}
\begin{bmatrix}
3 & 0 & 1 & 1\\
1 & 1 & 2 & 1 \\
0 & 2 & 2  & 1\\
2 & -3 & 2 & 1
\end{bmatrix}\sim\begin{bmatrix}
1 & 1 & 2 & 1 \\
0 & 2 & 2  & 1\\
0 & -3 & -5 & -2\\
0 & -5 & -2 & -1
\end{bmatrix}\sim\begin{bmatrix}
1 & 1 & 2 & 1 \\
0 & 1 & 3 & 1\\
0 & 0 & -4  & -1\\
0 & 0 & 13 & 4
\end{bmatrix}\sim\begin{bmatrix}
1 & 1 & 2 & 1 \\
0 & 1 & 3 & 1 \\
0 & 0 & 1 & 1 \\
0 & 0 & -4  & -1
\end{bmatrix}\sim \\
\sim\begin{bmatrix}
1 & 1 & 2 & 1 \\
0 & 1 & 3 & 1 \\
0 & 0 & 1 & 1 \\
0 & 0 & 0  & 3
\end{bmatrix}
\end{align}
$$

---

# 3
${}M_{2,2}{}$: ${}\begin{aligned}&\mathbf{A_{1}}=\begin{bmatrix}1 & 0 \\  -1 & 3\end{bmatrix} \\  &\mathbf{A}_{2}=\begin{bmatrix}3 & 2 \\  1 & -2\end{bmatrix} \\  &\mathbf{A}_{3}=\begin{bmatrix}-1 & -2 \\  3 & 4\end{bmatrix} \\  &\mathbf{A}_{4}=\begin{bmatrix}3 & 0 \\  3 & 5\end{bmatrix}\end{aligned}{}$ generují podprostor ${}M{}$ v ${}M_{2,2}{}$ 

? ${}\mathbf{Y}=\begin{bmatrix}1 & 1 \\  1 & 1\end{bmatrix}\in M{}$
? ${}\mathbf{X}=\begin{bmatrix}2 & -4 \\  8 & 16\end{bmatrix}\in M{}$


$$
\begin{align}
\begin{bmatrix*}[cccc|ccc]
1 & 3 & -1 & 3 & 0 & 1 & 2 \\
0 & 2 & -2 & 0 & 0 & 1 & -4 \\
-1 & 1 & 3 & 3 & 0 & 1 & 8 \\
3 & -2 & 4 & 5 & 0 & 1 & 16
\end{bmatrix*}\sim\dots \sim\begin{bmatrix*}[cccc|ccc]
1 & 3 & -1 & 3 & 0 & 1 & 2 \\
0 & 1 & -1 & 0 & 0 & \frac{1}{2} & -2 \\
0 & 0 & 1 & 1 & 0 &  &  \\
0 & 0 & 0 & 0 & 0 &  & 
\end{bmatrix*}
\end{align}
$$
${}\mathbf{X}\not\in M{}$
${}\mathbf{Y}=2\mathbf{A}_{1}+\mathbf{A}_{2}+3\mathbf{A}_{3}{}$ → ${}\hat{\mathbf{Y}}=[2,1,3]^T{}$ - souřadnice prvku ${}\mathbf{Y}{}$ v bázi ${}\mathbf{A}_{1},\mathbf{A}_{2},\mathbf{A}_{3}{}$ v podprostoru ${}M{}$

---

# 4
${}\mathbb{R}_{3}{}$   ${}\begin{aligned}&a_{1}=[1,0,2]^T \\ &a_{2}=[0,1,1]^T \\  &a_{3}=[-1,2,1]^T \end{aligned}{}$ :  generují podprostor ${}V{}$ v ${}\mathbb{R}_{3}{}$
${}v=[1,-1,2]^T{}$
${}v\in V?{}$


${}\alpha_{1}a_{1}+\alpha_{2}a_{2}+\alpha_{3}a_{3}=\mathbb{0}{}$

$$
\begin{align}
\begin{bmatrix*}[ccc|cc]
1 & 0 & -1 & 0 & 1 \\
0 & 1 & 2 & 0 & -1 \\
2 & 1 & 1 & 0 & 2
\end{bmatrix*}\sim\begin{bmatrix*}[ccc|cc]
1 & 0 & -1 & 0 & 1 \\
0 & 1 & 2 & 0 & -1 \\
0 & 1 & 3 & 0 & 0
\end{bmatrix*}\sim\begin{bmatrix*}[ccc|cc]
1 & 0 & -1 & 0 & 1 \\
0 & 1 & 2 & 0 & -1 \\
0 & 0 & 1 & 0 & 1
\end{bmatrix*}
\end{align}
$$
${}0a_{1}+0a_{2}+0a_{3}=\mathbb{0}{}$ ${}\implies{}$ LN ${}\implies{}$ báze je ${}\{ a_{1},a_{2},a_{3} \}{}$
${}V{}$ je generující v ${}\mathbb{R}_{3}{}$ ${}\implies{}$ ${}v\in V{}$
