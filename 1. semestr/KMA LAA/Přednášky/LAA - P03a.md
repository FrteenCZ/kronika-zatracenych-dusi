---
type: lecture
status: todo
date: 07-10-2026
katedra: KMA
---

> **Téma:** DETERMINANT MATICE
> **Koncepty:** [[Permutace]], [[Matice]], [[Matice#Determinant]]
> **Zdroj**: [[P03a.pdf]]


**Permutace** konečné množiny ${}M = \{1, 2, \dots, n\}{}$ je prosté zobrazení množiny ${}M{}$ na sebe.

Jestliže ${}i, j \in M = \{1, 2, \dots, n\}{}$, potom permutace ${}\pi{}$ taková, že ${}\pi(i) = j, \pi(j) = i{}$ a pro každé ${}s \in M \setminus \{i, j\}{}$ je ${}\pi(s) = s{}$, se nazývá **transpozice**.

Každá permutace se dá vyjádřit jako složení konečného počtu transpozic.

Permutace se nazývá **sudá**, je-li složením sudého počtu transpozic. 
Permutace se nazývá **lichá**, je-li složením lichého počtu transpozic.

**Znaménko** permutace je ${}1{}$, je-li permutace sudá; ${}−1{}$, je-li permutace lichá. Píšeme
$$
\mathrm{zn}(\pi)\begin{cases}
1, & \text{je-li permutace } \pi \text{ sudá}; \\
-1, & \text{je-li permutace } \pi \text{ lichá}.
\end{cases}
$$


> [!note] Definice 1. 
> Nechť ${}\mathbf{A} = [a_{ij}]{}$ je čtvercová matice řádu ${}n{}$. Potom **determinant matice** ${}\mathbf{A}{}$ je prvek
> 
> $$
> \det \mathbf{A} = \sum_{\pi} \mathrm{zn}(\pi)a_{1\pi(1)} \cdot a_{2\pi(2)} \dots a_{n\pi(n)},
> $$
> kde sčítáme přes všechny permutace ${}\pi{}$ na množině ${}\{1, 2, \dots, n\}{}$.

Pro ${}n = 2{}$ máme: ${}\det \mathbf{A} = \begin{vmatrix}a_{11} & a_{12} \\  a_{21}  & a_{22}\end{vmatrix} = a_{11}a_{22} - a_{12} a_{21}{}$.

Pro ${}n = 3{}$ máme: 
$$
\begin{align}
\det \mathbf{A}&=\begin{vmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{vmatrix}= \\
&= a_{11} a_{22} a_{33} +a_{13} a_{21} a_{32} +a_{12} a_{23} a_{31} - a_{13}a_{22}a_{31} - a_{11} a_{23} a_{32} - a_{12} a_{21} a_{33}.
\end{align}
$$
Tato metoda výpočtu determinantu matice řádu 3 se nazývá **Sarrusovo pravidlo**.


> [!quote] Věta 1. 
> Pro každou čtvercovou matici ${}\mathbf{A} = [a_{ij}]{}$ platí
> 
> $$
> \mathbf{A}^T = \det \mathbf{A}.
> $$


> [!note] Definice 2. 
> Nechť ${}\mathbf{A} = [a_{ij}]{}$ je čtvercová matice řádu ${}n{}$, nechť ${}i, j \in \{1, 2, \dots, n\}{}$. Potom ${}\mathbf{A}_{ij}{}$ bude značit matici řádu ${}n - 1{}$, která vznikne z matice ${}\mathbf{A}{}$ tím, že vyškrtneme ${}i{}$-tý řádek a ${}j{}$-tý sloupec. Prvek ${}\mathbf{A}_{ij} = (-1)^{i+j} \det \mathbf{A}_{ij}{}$ nazýváme **algebraický doplněk** matice ${}\mathbf{A}{}$ k místu ${}(i, j){}$.


> [!quote] Věta 2 (o rozvoji determinantu podle řádku) 
> Nechť ${}\mathbf{A} = [a_{ij}]{}$ je čtvercová matice řádu ${}n{}$, nechť ${}i{}$ je číslo zvoleného řádku, ${}i \in \{1, 2, \dots, n\}{}$. Potom 
> 
> $$
> \det \mathbf{A} = a_{i1}\mathbf{A}_{i1} + a_{i2}\mathbf{A}_{i2} + \dots + a_{in}\mathbf{A}_{in} = \sum_{j=1}^n  a_{ij} \mathbf{A}_{ij}
> $$


> [!note] Definice 3. 
> Následující úpravy matice ${}\mathbf{A}{}$ typu ${}m/n{}$
> 1. vyměnění dvou řádků (respektive sloupců) matice,
> 2. vynásobení řádku (respektive sloupce) matice nenulovým číslem,
> 3. přičtení ${}k{}$-násobku ${}j{}$-tého řádku (respektive sloupce) k řádku (respektive sloupci) ${}i{}$-tému, ${}i\neq j, 1  \leq i, j \leq m{}$ ( resp. ${}1 \leq i, j \leq n{}$)
>  
> se nazývají **elementární řádkové (respektive sloupcové) úpravy** matice ${}\mathbf{A}{}$.


> [!quote] Věta 3. 
> Jestliže čtvercová matice ${}\mathbf{B}{}$ řádu ${}n{}$ vznikne ze čtvercové matice ${}\mathbf{A}{}$ řádu ${}n{}$ tím, že vyměníme ${}i{}$-tý a ${}j{}$-tý řádek (respektive sloupec) (${}i\neq j{}$), potom
> $$
\det \mathbf{B} = - \det \mathbf{A}.
$$

**Důsledek 4.** 
Jsou-li ve čtvercové matici ${}\mathbf{A}{}$ řádu ${}n{}$ dva řádky (respektive sloupce) stejné, potom ${}\det \mathbf{A} = 0{}$.

> [!quote] Věta 5. 
> Nechť matice ${}\mathbf{B}{}$ vznikne z matice ${}\mathbf{A}{}$ řádu ${}n{}$ tím, že řádek (respektive sloupec) ${}i{}$ vynásobíme číslem ${}c{}$. Potom 
> 
> $$
> \det \mathbf{B} = c \cdot \det \mathbf{A}.
> $$


**Důsledek 6.** 
Je-li v matici ${}\mathbf{A} = [a_{ij}]{}$ řádu ${}n{}$ celý řádek (respektive sloupec) nulový, potom ${}\det \mathbf{A} = 0{}$.

> [!quote] Věta 7. 
> Nechť matice ${}\mathbf{B}{}$ vznikne z matice ${}\mathbf{A}{}$ řádu ${}n{}$ tím, že k řádku (respektive sloupci) ${}i{}$ přičteme ${}k{}$-násobek řádku (resp. sloupce) ${}j, 1 \leq i, j \leq n, i\neq j{}$. Potom
> 
> $$
> \det \mathbf{B} = \det \mathbf{A}.
> $$


> [!quote] Věta 8. 
> Nechť ${}\mathbf{A}, \mathbf{B}{}$ jsou matice řádu ${}n{}$. Potom
> 
> $$
> \det(\mathbf{A} \cdot \mathbf{B}) = \det \mathbf{A} \cdot \det \mathbf{B}.
> $$



---
**Permutace** konečné množiny ${}M=\{ 1,2,3,\dots,n \}{}$ je prosté zobrazení množiny ${}M{}$ na sebe.
> Př.
> ${}\pi_{1} = \begin{pmatrix}1 & 2 & 3 & 4 & 5 \\  5 & 3 & 2 & 1 & 4\end{pmatrix}{}$ ${}\pi_{2} = \begin{pmatrix}1 & 2 & 3 & 4 & 5 \\  2 & 4 & 3 & 1 & 5\end{pmatrix}{}$        je jich ${}n!{}$

Jestliže ${}i,j\in M=\{ 1,2,\dots n \}{}$, potom permutace ${}\pi{}$ taková že ${}\pi(i)=j$, $\pi(j)=i{}$ a pro každé ${}s \in M \setminus \{ i,j \}{}$ je ${}\pi(s)=s{}$, se nazývá **transpozice**.
>

Každá permutace se dá vyjádřit jako složení konečného počtu transpozic.

Permutace se nazývá **sudá**, je-li složením sudého počtu transpozic. Permutace se nazývá **lichá**, je-li  složením lichého počtu transpozic.

> [!error]
> Znaménko permutace je 1, je-li permutace sudá; −1, je-li permutace lichá. Píšeme zn(\pi) = ( 1, je-li permutace \pi sud´a; −1, je-li permutace \pi lich´a.

> [!info] Definice 1.
> Nechť $\mathbf{A} = [a_{ij} ]$ je čtvercová matice ˇr´adu n. Potom determinant matice A je prvek det A = X \pi zn(\pi)a1\pi(1)a2\pi(2) · · · an\pi(n) , kde sˇc´ıt´ame pˇres vˇsechny permutace \pi na mnoˇzinˇe {1, 2, \dots, n}.

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
