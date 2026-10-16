---
type: exercise
status: todo
katedra: KMA
date: 13-10-2026
---

> **Téma:** 
> **Koncepty:** [[Matice]] [[Matice#Determinant]]
> **Zdroj**: [[dcv-2-2011.pdf]]


# Maticové rovnice

1) $$
\begin{align}
&\mathbf{A}=\begin{bmatrix}
3 & 2 & -1 & 4 \\
0 & -2 & -3 & 1
\end{bmatrix} &  & \mathbf{B}=\begin{bmatrix}
5 & -4 & 3 & 0 \\
2 & 4 & 1 & -3
\end{bmatrix} \\
2\mathbf{X}&=\mathbf{B}-\mathbf{A} \\
\mathbf{X}&=\frac{1}{2}(\mathbf{B}-\mathbf{A}) \\
\mathbf{X}&=\frac{1}{2}\begin{bmatrix}
2 & -6 & 4 & -4 \\
2 & 6 & 4 & -4
\end{bmatrix} \\
\mathbf{X}&=\begin{bmatrix}
1 & -3 & 2 & -2  \\
1 & 3 & 2 & -2
\end{bmatrix}
\end{align}
$$
2) 
   $$
   \begin{align} 
   \mathbf{C=\begin{bmatrix}
   1 & -1 \\
   2 & 0
   \end{bmatrix}} \\
   \mathbf{X}-\mathbf{A}\cdot \mathbf{B}&=\mathbf{C} \text{........... B krát A nelze}
   \end{align}
   $$
3) 
   $$
   \begin{align}
   \mathbf{X}-\mathbf{A}\cdot \mathbf{B}^T=\mathbf{C} \\
   \mathbf{X}=\mathbf{C}+\mathbf{A}\cdot \mathbf{B}^T \\
   \mathbf{X}=\mathbf{C}+\begin{bmatrix}
   4 & 1 \\
   -1 & -14
   \end{bmatrix} \\
   \mathbf{X}=\begin{bmatrix}
   5 & 0 \\
   1 & -14
   \end{bmatrix}
   \end{align}
   $$
4) 
   $$
   \begin{align}
   \mathbf{A}\cdot \mathbf{X}+\mathbf{C}&=2\mathbf{B} \\
\mathbf{A}\cdot \mathbf{X}&=2\mathbf{B}-\mathbf{X}~~|~~\text{... viz 4.pdf}
   \end{align}
   $$


# Determinant
1) 
   $$
   \det \begin{bmatrix}
   3 & 2 \\
   -2 & 4
   \end{bmatrix}=12-(-4)=16
   $$
2) 
   $$
   \begin{align}
   \det \begin{bmatrix}
   2 & 4 & 1 \\
   -2 & 3 & 5 \\
   1 & 2 & 2
   \end{bmatrix}=12+20-4-20+16-3=21
   \end{align}
   $$
3) 
   $$
   \begin{align}
   \det \begin{bmatrix}
   -1 & 5 & 1 \\
   3 & 1 & -2 \\
   -2 & -2 & 1
   \end{bmatrix}=-1+20-6+4-15+2=4
   \end{align}
   $$
4) 
   $$
   \begin{align}
   \det \begin{bmatrix}
   -1 & 0 & -3 & 1 \\
   2 & 1 & 4 &1  \\
   1 & 0 & 2 & 3 \\
   1 & 0 & 1 & -1 
   \end{bmatrix}
   \end{align}=1\cdot(-1)^{2+2}\cdot \det \begin{bmatrix}
   -1 & -3 & 1 \\
   1 & 2 & 3 \\
   1 & 1 & -1
   \end{bmatrix}=1\cdot(2-9+1+3-3-2)=-8
   $$
5) 
   $$
   \begin{align}
   \det \begin{bmatrix}
   1 & 2 & 3 & -1 \\
   4 & 3 & 1 & 2 \\
   -1 & 2 & 3 & 2 \\
   1 & -2 & 1 & 2
   \end{bmatrix}=\det \begin{bmatrix}
0 & 4 & 2 & -3 \\
0 & 11 & -3 & -6 \\
0 & 0 & 4 & 4 \\
1 & -2 & 1 & 2
   \end{bmatrix}=1\cdot(-1)^{1+4}\cdot \det \begin{bmatrix}
   4 & 2 & -3 \\
   11 & -3 & -6 \\
   0 & 4 & 4
   \end{bmatrix}= \\
   =-1\det \begin{bmatrix}
   4 & 2 & -5 \\
   11 & -3 & -3 \\
   0 & 4 & 0
   \end{bmatrix}=-4\det \begin{bmatrix}
   4 & -5 \\
   11 & -3
   \end{bmatrix}=4(-12+55)=172
   \end{align}
   $$

---

$$
\begin{align}
\det \begin{bmatrix}
1 & 2 & 0 & 1 \\
3 & -2 & 1 & 0 \\
0 & 6 & 3 & -2 \\
2 & 4 & 3 & 1
\end{bmatrix}=\det\begin{bmatrix}
0 & 0 & 0 & 1 \\
3 & -2 & 1 & 0 \\
2 & 10& 3 & -2 \\
1 & 2& 3 & 1
\end{bmatrix}=1(-1)^{5}\det \begin{bmatrix}
3 & -2 & 1 \\
2 & 10 & 3 \\
1 & 2 & 3
\end{bmatrix}= \\
=-1(90-6+4-18+12-10)=-72
\end{align}
$$