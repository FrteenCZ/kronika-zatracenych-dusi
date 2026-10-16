---
type: lecture
status: todo
date: 01-10-2026
katedra: KMA
---

> **Téma:** Násobení matic a řešení soustavy rovnic
> **Koncepty:** [[Matice]]
> **Source**: [[P01b-vyplneny.pdf|P01b.pdf]]

# Násobení matic
${}A{}$ typu ${}m/n{}$ a ${}B{}$ typu ${}n/p{}$, vznikne ${}C{}$ typu ${}m/p{}$

$$
c_{ik}=a_{i1}b_{1k}+a_{i 2}b_{2k}+\dots+a_{in}b_{nk}=\sum_{j=1}^na_{ij}b_{jk}
$$
> [!tip]
>  "Skalární součin řádků A a sloupců B jako vektorů"

př.: 

$$
\begin{align}
A&=\begin{bmatrix}
2 & 4 \\
1 & 2 \\
-1 & -2
\end{bmatrix} &  & B=\begin{bmatrix}
3 & 4 & 1 \\
0 & 2 & -2 \\
3 & 1 & 4
\end{bmatrix} \\
C&=A\cdot B=nelze &  &D=B\cdot A=\begin{bmatrix}
3\cdot 2+4\cdot 1+1\cdot(-1) & 3\cdot 4+4\cdot 2+1\cdot(-2) \\
0+2+2 & 0+4+4 \\
6+1-4 & 12+2-8
\end{bmatrix} =\begin{bmatrix}
9 & 18 \\
4 & 8 \\
3 & 6
\end{bmatrix}
\end{align}
$$

> [!warning]
> Násobení matic není komutativní

> [!note] Věta 2
> 1. $A(BC) = (AB)C$, - asociativní
> 2. $(A + B)C = AC + BC$, distributivní
> 3. $C(A + B) = CA + CB$, distributivní
> 4. $(AB)^T = B^TA^T$,
> 5. $(\lambda A)B = A(\lambda B) = \lambda(AB)$.


---





$$
\begin{align}
x_{1}+2x_{2}-3x_{3}&=1 \\
2x_{1}-3x_{2}+4x_{3}&=5 \\
x_{1}-x_{2}+x_{3}&=2 \\
 \\
 A=\begin{bmatrix}
 1 & 2 & -3 \\
 2 & -3 & 4 \\
 1 & -1 & 1
 \end{bmatrix} x=\begin{bmatrix}
 x_{1} \\
 x_{2} \\
 x_{3}
 \end{bmatrix}b=\begin{bmatrix}
 1 \\
 5 \\
 2
 \end{bmatrix} \\
 \\
\begin{bmatrix*}[ccc|c]
1 & 2 & -3  & 1 \\
2 & -3 & 4  & 5 \\
1 & -1 & 1  & 2
\end{bmatrix*}\sim\begin{bmatrix*}[ccc|c]
1 & 2 & -3 & 1 \\
0 & -7 & 10  & 3 \\
0 & -3 & 4 & 1
\end{bmatrix*}\sim\begin{bmatrix*}[ccc|c]
1 & 2 & -3  & 1 \\
0 & -1 & 2 & 1 \\
0 & 0 & -2 & -2
\end{bmatrix*}\sim\begin{bmatrix*}[ccc|c]
1 & 2 & -3  & 1 \\
0 & 1 & -2 & -1 \\
0 & 0 & 1 & 1
\end{bmatrix*}
\end{align}
$$