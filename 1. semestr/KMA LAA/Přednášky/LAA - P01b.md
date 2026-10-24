---
type: lecture
status: todo
date: 24-09-2026
katedra: KMA
---

> **Téma:** MATICE
> **Koncepty:** [[Matice]]
> **Source**: [[P01b.pdf]], [[P01b-vyplneny.pdf]]

**Matice typu** ${}m/n{}$ je soubor ${}m\cdot n{}$ prvků uspořádaných do ${}m{}$ řádků a ${}n{}$ sloupců:
$$
\mathbf{A}=\begin{bmatrix}
a_{11} & a_{12} & \dots & a_{1n} \\
a_{21} & a_{22} & \dots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m 2} & \dots & a_{mn}
\end{bmatrix}=[a_{ij}]
$$

Prvky ${}a_{kk}{}$, pro které je řádkový index stejný jako index sloupcový, se nazývají prvky **diagonální**.


Matice ${}\mathbf{A}{}$ typu ${}m/n{}$ se nazývá matice **čtvercová řádu** ${}n{}$, jestliže ${}m = n{}$, t.j. jestliže má stejný počet řádků a sloupců.


Matice ${}\mathbf{A}{}$ typu ${}m/n{}$ se nazývá matice **obdélníková**, jestliže ${}m \neq n{}$.


${}n{}$-**členný aritmetický vektor** je matice typu ${}n/1{}$.
Při zápisu ${}n{}$-členného aritmetického vektoru budeme vynechávat druhý index, budeme psát
$$
a=\begin{bmatrix}
a_{1} \\
a_{2} \\
\vdots \\
a_{n}
\end{bmatrix}=[a_{1},a_{2},\dots,a_{n}]^T.
$$

Matice ${}\mathbf{A} = [a_{ij} ]{}$ typu ${}m/n{}$ se nazývá matice **nulová** a značí se **0**, jestliže ${}a_{ij} = 0{}$ pro každé ${}i = 1, \dots, m{}$ a pro každé ${}j = 1, \dots, n{}$, t.j. jestliže na každém místě matice je prvek ${}0{}$.


Čtvercová matice ${}\mathbf{A} = [a_{ij} ]{}$ řádu ${}n{}$ se nazývá matice **diagonální**, jestliže ${}a_{ij} = 0{}$ pro každé ${}i \neq j{}$. Potom píšeme ${}\mathbf{A} = \mathrm{diag} [a_{11} , a_{22} , \dots, a_{nn} ]{}$.


**Jednotková** matice řádu ${}n{}$ je matice $\mathbf{I}=\operatorname{diag}[\underbrace{1,1, \ldots, 1}_n]$, t.j. ${}\mathbf{I}=\begin{bmatrix}1 & 0 & 0 & \dots & 0 \\  0 & 1 & 0 & \dots & 0 \\  0 & 0 & 1 & \dots  & 0 \\  \vdots & \vdots & \vdots & \ddots & \vdots \\  0 & 0 & 0 & \dots & 1\end{bmatrix}{}$


Řekneme, že matice ${}\mathbf{A}{}$ typu ${}m/n{}$ je **horní (resp. dolní) trojúhelníková** matice, jestliže ${}a_{ij} = 0{}$ pro každé ${}i > j{}$ (resp. ${}i < j{}$).


Řekneme, že čtvercová matice ${}\mathbf{A}{}$ řádu ${}n{}$ je **symetrická**, jestliže ${}a_{ij} = a_{ji}{}$ pro každé ${}i, j =1, \dots, n{}$.

Řekneme, že čtvercová matice ${}\mathbf{A}{}$ řádu ${}n{}$ je **antisymetrická**, jestliže ${}a_{ij} = -a_{ji}{}$ pro každé ${}i, j =1, \dots, n{}$.

Matice ${}\mathbf{A} = [a_{ij} ]{}$, ${}\mathbf{B} = [b_{ij} ]{}$ jsou si **rovny**, jestliže to jsou matice stejného typu **m/n** a jestliže ${}a_{ij} = b_{ij}{}$ pro každé ${}i = 1, \dots, m{}$ a pro každé ${}j = 1, \dots, n{}$. Píšeme ${}\mathbf{A}=\mathbf{B}{}$.


# Operace s maticemi
## Transponování matice

Je-li ${}\mathbf{A} = [a_{ij} ]{}$ matice typu ${}m/n{}$, potom matice typu ${}n/m{}$ tvaru ${}\mathbf{A}^T = [a_{ji} ]{}$ se nazývá matice **transponovaná**.

 > [!quote] Věta 1
 > 1. Matice ${}\mathbf{A}{}$ je symetrická ${}\Leftrightarrow \mathbf{A}^T=\mathbf{A}{}$.
 > 2. Pro každou matici ${}\mathbf{A}{}$ platí: ${}(\mathbf{A}^T )^T = \mathbf{A}{}$.
 
 
## Sčítání matic

Jsou-li matice ${}\mathbf{A} = [a_{ij} ]{}$, ${}\mathbf{B} = [b_{ij} ]{}$ matice stejného typu ${}m/n{}$, potom jejich **součet** je matice typu ${}m/n{}$ tvaru ${}\mathbf{A} + \mathbf{B} = [a_{ij} + b_{ij} ]{}$.


## Násobení matice číslem

Je-li ${}\lambda{}$ číslo, ${}\mathbf{A} = [a_{ij} ]{}$ matice typu ${}m/n{}$, potom matice typu ${}m/n{}$ tvaru ${}\lambda \mathbf{A} = [\lambda a_{ij} ]{}$ se nazývá **násobek** matice ${}\mathbf{A}{}$ číslem ${}\lambda{}$.


Matice **opačná** k matici ${}\mathbf{A}{}$ je násobek matice ${}\mathbf{A}{}$ číslem ${}−1{}$, tedy ${}\mathbf{A} = (-1)\mathbf{A}{}$.

**Odečítání matic** je součet matice a matice opačné, t.j. ${}\mathbf{A} - \mathbf{B} = \mathbf{A} + (-\mathbf{B}){}$.


## Násobení matic
Jsou-li ${}\mathbf{A} = [a_{ij} ]{}$ matice typu ${}m/n{}$, ${}\mathbf{B} = [b_{jk} ]{}$ matice typu ${}n/p{}$, potom matice ${}\mathbf{C} = [c_{ik} ]{}$ typu ${}m/p{}$ se nazývá **součin** matic ${}\mathbf{C} = \mathbf{AB}{}$, jestliže pro každé ${}i = 1, \dots, m, k = 1, \dots, p{}$ platí:

$$
c_{ik}=a_{i1}b_{1k}+a_{i 2}b_{2k}+\dots+a_{in}b_{nk}=\sum_{j=1}^na_{ij}b_{jk}.
$$
> [!tip]
>  "Skalární součin řádků ${}\mathbf{A}{}$ a sloupců ${}\mathbf{B}{}$ jako vektorů"

> [!example]-
> $$
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

> [!quote] Věta 2.
> Pro každé tři matice ${}\mathbf{A}, \mathbf{B}, \mathbf{C}{}$ a pro libovolné čı́slo ${}\lambda{}$ platıí, kdykoliv alespoň jedna strana rovnosti je definována:
> 1. ${}\mathbf{A}(\mathbf{BC}) = (\mathbf{AB})\mathbf{C}{}$,
> 2. ${}(\mathbf{A} + \mathbf{B})\mathbf{C} = \mathbf{AC} + \mathbf{BC}{}$,
> 3. ${}\mathbf{C}(\mathbf{A} + \mathbf{B}) = \mathbf{CA} + \mathbf{CB}{}$,
> 4. ${}(\mathbf{AB})^T = \mathbf{B}^T \mathbf{A}^T{}$,
> 5. ${}(\lambda \mathbf{A})\mathbf{B} = \mathbf{A}(\lambda \mathbf{B}) = \lambda(\mathbf{AB}){}$.
> Pro jednotkovou matici ${}\mathbf{I}{}$ a nulovou matici ${}\mathbf{0}{}$ a pro každou matici ${}\mathbf{A}{}$ platí, kdykoliv levá strana rovnosti je definována:
> 6. ${}\mathbf{AI} = \mathbf{A}, \mathbf{IA} = \mathbf{A}{}$,
> 7. ${}\mathbf{A0} = \mathbf{0}, \mathbf{0A} = \mathbf{0}{}$.

Jestliže ${}\mathbf{A}{}$ je čtvercová matice řádu ${}n{}$, potom čtvercová matice ${}\mathbf{A}^{-1}{}$ řádu ${}n{}$ se nazývá **inverzní matice** k matici ${}\mathbf{A}{}$, jestliže ${}\mathbf{A}\mathbf{A}^{-1} = \mathbf{A}^{-1}\mathbf{A} = \mathbf{I}{}$.

> [!quote] Věta 3
> Ke čtvercové matici existuje nejvýše jedna inverzní matice.
