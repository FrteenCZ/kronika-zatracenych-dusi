---
type: lecture
status: todo
date: 07-10-2026
katedra: KMA
---

> **Téma:** Determinant matice
> **Koncepty:** [[Permutace]], [[Matice]], [[Matice#Determinant]]
> **Zdroj**: [[P03a.pdf]]

**Permutace** konečné množiny ${}M=\{ 1,2,3,\dots,n \}{}$ je prosté zobrazení množiny ${}M{}$ na sebe.
> Př.
> ${}\pi_{1} = \begin{pmatrix}1 & 2 & 3 & 4 & 5 \\  5 & 3 & 2 & 1 & 4\end{pmatrix}{}$ ${}\pi_{2} = \begin{pmatrix}1 & 2 & 3 & 4 & 5 \\  2 & 4 & 3 & 1 & 5\end{pmatrix}{}$        je jich ${}n!{}$

Jestliže ${}i,j\in M=\{ 1,2,\dots n \}{}$, potom permutace ${}\pi{}$ taková že ${}\pi(i)=j$, $\pi(j)=i{}$ a pro každé ${}s \in M \setminus \{ i,j \}{}$ je ${}\pi(s)=s{}$, se nazývá **transpozice**.
>

Každá permutace se dá vyjádřit jako složení konečného počtu transpozic.

Permutace se nazývá **sudá**, je-li složením sudého počtu transpozic. Permutace se nazývá **lichá**, je-li  složením lichého počtu transpozic.

> [!error]
> Znaménko permutace je 1, je-li permutace sudá; −1, je-li permutace lichá. Píšeme zn(π) = ( 1, je-li permutace π sud´a; −1, je-li permutace π lich´a.

> [!info] Definice 1.
> Nechť $\mathbf{A} = [a_{ij} ]$ je čtvercová matice ˇr´adu n. Potom determinant matice A je prvek det A = X π zn(π)a1π(1)a2π(2) · · · anπ(n) , kde sˇc´ıt´ame pˇres vˇsechny permutace π na mnoˇzinˇe {1, 2, ..., n}.

Pro ${}n=2{}$ máme: 
$$
\begin{align}
\det \mathbf{A} = \begin{vmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{vmatrix}=1\cdot a_{11}\cdot a_{22}-1\cdot a_{12}\cdot a_{21}
\end{align}
$$

Pro ${}n=3{}$ máme:
$$
\begin{align}
\det \mathbf{A}=\begin{vmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{vmatrix}=a_{11}a_{22}a_{33}+a_{13}a_{21}a_{32}+a_{12}a_{23}a_{31}−a_{13}a_{22}a_{31}−a_{11}a_{23}a_{32}−a_{12}a_{21}a_{33}
\end{align}
$$

Tato metoda výpočtu determinantu matice řádu 3 se nazývá **Sarrusovo pravidlo**. ==!Pouze 3==
![[Rule of Sarrus.png|381]]








Př.:

$$
\begin{align}
\det \mathbf{A}=\begin{vmatrix}
2 & 3 & -2 & 4 \\
-3 & -2 & 4 & -3 \\
4 & 2 & -3 & 5 \\
3 & 5 & -4 & 2
\end{vmatrix}
=\begin{vmatrix}
2 & 3 & -2 & 4 \\
-1 & 1 & 2 & 1 \\
0 & -4 & 1 & -3 \\
1 & 2 & -2 & -2
\end{vmatrix}=\begin{vmatrix}
0 & 5 & 2 & 6 \\
-1 & 1 & 2 & 1 \\
0 & -4 & 1 & -3 \\
0 & 3 & 0 & -1
\end{vmatrix}= \\
=0\cdot A_{11}+(-1)A_{21}+0\cdot A_{31}+0\cdot A_{41}=(-1)\cdot(-1)^{2+1}\cdot \begin{vmatrix}
5 & 2 & 6 \\
-4 & 1 & -3 \\
3 & 0 & -1
\end{vmatrix}= \\
=1\cdot(5\cdot 1\cdot(-1)+2\cdot(-3)\cdot 3+6\cdot(-4)\cdot 0-6\cdot 1\cdot 3-2\cdot(-4)\cdot(-1)-5\cdot(-3)\cdot 0)= \\
=1(-5-18+0-18-8-0)=-49
\end{align}
$$