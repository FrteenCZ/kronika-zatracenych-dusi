---
type: lecture
status: todo
date: 07-10-2026
katedra: KMA
---

> **Téma:** DETERMINANT MATICE
> **Koncepty:** [[Permutace]], [[Matice]], [[Matice#Determinant]]
> **Zdroj**: [[P03a.pdf]]


**Permutace** konečné množiny ${}M = \{1, 2, \dots, n\}{}$ je prosté zobrazení množiny ${}M{}$ na sebe. *(je jich ${}n!{}$)*

> [!example]-
> ${}\pi_{1} = \begin{pmatrix}1 & 2 & 3 & 4 & 5 \\  5 & 3 & 2 & 1 & 4\end{pmatrix}{}$ ${}\pi_{2} = \begin{pmatrix}1 & 2 & 3 & 4 & 5 \\  2 & 4 & 3 & 1 & 5\end{pmatrix}{}$


Jestliže ${}i, j \in M = \{1, 2, \dots, n\}{}$, potom permutace ${}\pi{}$ taková, že ${}\pi(i) = j, \pi(j) = i{}$ a pro každé ${}s \in M \setminus \{i, j\}{}$ je ${}\pi(s) = s{}$, se nazývá **transpozice**.

> ${}\pi=\begin{pmatrix}1 & 2 & 3 & 4 & 5 \\  1 & 3 & 2 & 4 & 5\end{pmatrix}\implies{}$ permutace lze skládat ${}\pi_{1}\circ \pi_{2}\implies{}$ není komutativní!
> #fixme : Příklad jak neplatí komutativita

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

> [!example]-
> $$
> \begin{align}
> \pi_{1}=\begin{pmatrix}
> 1 & 2 & 3 & 4 & 5 \\
> 5 & 3 & 2 & 1 & 4
> \end{pmatrix} && \alpha_{1}=\begin{pmatrix}
> 1 & 2 & 3 & 4 & 5 \\
> 5 & 2 & 3 & 4 & 1
> \end{pmatrix} \\
> 1~~~3~~~2~~~5~~~4 && \alpha_{2}=\begin{pmatrix}
> 1 & 2 & 3 & 4 & 5 \\
> 1 & 2 & 3 & 5 & 4
> \end{pmatrix} \\
> 1~~~3~~~2~~~4~~~5 && \alpha_{2}=\begin{pmatrix}
> 1 & 2 & 3 & 4 & 5 \\
> 1 & 3 & 2 & 4 & 5
> \end{pmatrix} \\
> 1~~~2~~~3~~~4~~~5 \\
>  \\
> \pi_{1}=\alpha_{3}\circ\alpha_{2}\circ\alpha_{1}=\begin{pmatrix}
> 1 & 2 & 3 & 4 & 5 \\
> 5 & 3 & 2 & 1 & 4
> \end{pmatrix} \\
> \implies \pi_{1} \text{ je lichá } \implies \mathrm{zn}(\pi_{1})=-1
> \end{align}
> $$


> [!note] Definice 1. 
> Nechť ${}\mathbf{A} = [a_{ij}]{}$ je **čtvercová** matice řádu ${}n{}$. Potom **determinant matice** ${}\mathbf{A}{}$ je prvek
> 
> $$
> \det \mathbf{A} = \sum_{\pi} \mathrm{zn}(\pi)a_{1\pi(1)} \cdot a_{2\pi(2)} \dots a_{n\pi(n)} = |\mathbf{A}|,
> $$
> kde sčítáme přes všechny permutace ${}\pi{}$ na množině ${}\{1, 2, \dots, n\}{}$.

Pro ${}n = 2{}$ máme: (${}2! =2{}$)
$$\det \mathbf{A} = \begin{vmatrix}a_{11} & a_{12} \\  a_{21}  & a_{22}\end{vmatrix} = a_{11}a_{22} - a_{12} a_{21}$$

$$
\begin{align}
\pi_{1}=\begin{pmatrix}
1 & 2 \\
1 & 2
\end{pmatrix} &  & &\mathrm{zn}(\pi_{1})=1 \\
\pi_{2}=\begin{pmatrix}
1 & 2 \\
2 & 1
\end{pmatrix} &  & &\mathrm{zn}(\pi_{2})=-1
\end{align}
$$

> [!example]-
> $$
\begin{align}
\mathbf{A}=\begin{bmatrix}
3 & 2 \\
4 & 1
\end{bmatrix} &  & \det \mathbf{A}=\begin{vmatrix}
3 & 2 \\
4 & 1
\end{vmatrix}=3\cdot 1-2\cdot 4
\end{align}
$$


Pro ${}n = 3{}$ máme: (${}3! =6{}$)
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
$$
\begin{array}{ll}
\pi_1=\left(\begin{array}{lll}
1 & 2 & 3 \\
1 & 2 & 3
\end{array}\right) \operatorname{zn}\left(\pi_1\right)=1 & \pi_4=\left(\begin{array}{lll}
1 & 2 & 3 \\
1 & 3 & 2
\end{array}\right) \operatorname{zn}\left(\pi_4\right)=-1 \\
\pi_2=\left(\begin{array}{lll}
1 & 2 & 3 \\
2 & 3 & 1
\end{array}\right) \operatorname{zn}\left(\pi_2\right)=1 & \pi_5=\left(\begin{array}{lll}
1 & 2 & 3 \\
3 & 2 & 1
\end{array}\right) \operatorname{zn}\left(\pi_5\right)=-1 \\
\pi_3=\left(\begin{array}{lll}
1 & 2 & 3 \\
3 & 1 & 2
\end{array}\right) \operatorname{zn}\left(\pi_3\right)=1 & \pi_6=\left(\begin{array}{lll}
1 & 2 & 3 \\
2 & 1 & 3
\end{array}\right) \operatorname{zn}\left(\pi_6\right)=-1
\end{array}
$$



Tato metoda výpočtu determinantu matice řádu 3 se nazývá **Sarrusovo pravidlo**. ==!Pouze 3==
![[Rule of Sarrus.png|381]]

> [!example]-
> $$
\begin{vmatrix}
2 & 1 & 3 \\
-1 & 2 & 4 \\
3 & 2 & 1
\end{vmatrix}=2\cdot 2\cdot 1+(-1)\cdot 2\cdot 3+3\cdot 1\cdot 4-3\cdot 2\cdot 3-4\cdot 2\cdot 2-1\cdot 1\cdot(-1)=-23
$$



> [!quote] Věta 1. 
> Pro každou čtvercovou matici ${}\mathbf{A} = [a_{ij}]{}$ platí
> 
> $$
> \mathbf{A}^T = \det \mathbf{A}.
> $$
> 
> > [!done]- Důkaz
> > Analogicky vyberu místo řádku sloupec


> [!note] Definice 2. 
> Nechť ${}\mathbf{A} = [a_{ij}]{}$ je čtvercová matice řádu ${}n{}$, nechť ${}i, j \in \{1, 2, \dots, n\}{}$. Potom ${}\mathbf{A}_{ij}{}$ bude značit matici řádu ${}n - 1{}$, která vznikne z matice ${}\mathbf{A}{}$ tím, že vyškrtneme ${}i{}$-tý řádek a ${}j{}$-tý sloupec. Prvek ${}\mathbf{A}_{ij} = (-1)^{i+j} \det \mathbf{A}_{ij}{}$ nazýváme **algebraický doplněk** matice ${}\mathbf{A}{}$ k místu ${}(i, j){}$.


> [!quote] Věta 2 (o rozvoji determinantu podle řádku) 
> Nechť ${}\mathbf{A} = [a_{ij}]{}$ je čtvercová matice řádu ${}n{}$, nechť ${}i{}$ je číslo zvoleného řádku, ${}i \in \{1, 2, \dots, n\}{}$. Potom 
> 
> $$
> \det \mathbf{A} = a_{i1}\mathbf{A}_{i1} + a_{i2}\mathbf{A}_{i2} + \dots + a_{in}\mathbf{A}_{in} = \sum_{j=1}^n  a_{ij} \mathbf{A}_{ij}
> $$
> 
> > [!done]- Důkaz
> > Dokázána rozepsáním na předchozí straně pro ${}n=3{}$ a ${}i=2{}$ a funguje to analogicky i pro ${}n>2{}$ a libovolné ${}i\in \{ 1,2,\dots,n \}{}$
> > #fixme : přidat odvození na rozvoj podle řádku
> 
> > [!note] Poznámka
> > Díky Větě 1 lze stejně počítat determinant pomocí rozvoje podle libovolného sloupce.


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
> $$
> 
> > [!done]- Důkaz
> > ve všech součinech při výpočtu determinantu matice ${}\mathbf{B}{}$ prvky zůstanou stejné, ale příslušná permutace změní znaménko (bude složena o 1 transpozici navíc) ${}\implies \det \mathbf{B}=-\det \mathbf{A}{}$

**Důsledek 4.** 
Jsou-li ve čtvercové matici ${}\mathbf{A}{}$ řádu ${}n{}$ dva řádky (respektive sloupce) stejné, potom ${}\det \mathbf{A} = 0{}$.

> [!done]- Důkaz
> ${}\mathbf{B}{}$ vznikne prohozením těch 2 stejných řádků ${}\mathbf{B}=\mathbf{A}{}$, z věty 3: 
> 
> $$
> \begin{align}
>  \det \mathbf{B}=-\det \mathbf{A} \\
>  \det \mathbf{A}=-\det \mathbf{A}
> \end{align} \implies \det \mathbf{A}=0
> $$


> [!quote] Věta 5. 
> Nechť matice ${}\mathbf{B}{}$ vznikne z matice ${}\mathbf{A}{}$ řádu ${}n{}$ tím, že řádek (respektive sloupec) ${}i{}$ vynásobíme číslem ${}c{}$. Potom 
> 
> $$
> \det \mathbf{B} = c \cdot \det \mathbf{A}.
> $$
> 
> > [!done]- Důkaz
> > Rozvoj podle ${}i{}$-tého řádku
> > 
> >$$
> \begin{align}
> \det \mathbf{B}&=c\cdot a_{i1} \cdot \mathbf{A}_{i1}+ c\cdot a_{i_{2}} \cdot \mathbf{A}_{i2}+\dots+c\cdot a_{in} \cdot \mathbf{A}_{in}= \\
> &=c(a_{i1} \cdot \mathbf{A}_{i1}+\dots+a_{in} \cdot \mathbf{A}_{in})=c\cdot \det \mathbf{A}
> \end{align}
> >$$


**Důsledek 6.** 
Je-li v matici ${}\mathbf{A} = [a_{ij}]{}$ řádu ${}n{}$ celý řádek (respektive sloupec) nulový, potom ${}\det \mathbf{A} = 0{}$.

> [!done]- Důkaz
> Zřejmý


> [!quote] Věta 7. 
> Nechť matice ${}\mathbf{B}{}$ vznikne z matice ${}\mathbf{A}{}$ řádu ${}n{}$ tím, že k řádku (respektive sloupci) ${}i{}$ přičteme ${}k{}$-násobek řádku (resp. sloupce) ${}j, 1 \leq i, j \leq n, i\neq j{}$. Potom
> 
> $$
> \det \mathbf{B} = \det \mathbf{A}.
> $$
> 
> > [!done]- Důkaz
> > 
> > $$
> \begin{align}
> \mathbf{A}&=[b_{ij}] \\ \\
> \det  \mathbf{B}&=\begin{vmatrix}
> b_{11} & \dots & b_{1n} \\
> \vdots \\
> b_{i1}+k\cdot b_{j1} & \dots & b_{in}+k\cdot b_{jn} \\
> \vdots \\
> b_{j1} & \dots & b_{jn} \\
> \vdots \\
> b_{n1} & \dots & b_{nn}
> \end{vmatrix} = (b_{i1}+k\cdot b_{j1})\mathbf{B}_{i1}+\dots+(b_{in}+k\cdot b_{jn})\mathbf{B}_{in}= \\
> &= (b_{i1} \cdot \mathbf{B}_{i1}+\dots+b_{in} \cdot \mathbf{B}_{in})+k\cdot(b_{j1} \cdot \mathbf{B}_{i1}+\dots+b_{jn} \cdot \mathbf{B}_{in})= \\
> &= \det \mathbf{A}+k\cdot \begin{vmatrix}
> b_{11} & \dots & b_{1n} \\
> \vdots \\
> b_{j1} & \dots & b_{jn} \\
> \vdots \\
> b_{j1} & \dots & b_{jn} \\
> \vdots \\
> b_{n1} & \dots & b_{nn}
> \end{vmatrix} \to \text{ i-tý a j-tý řádek jsou stejné! (Důsledek 4.)} \\
> &= \det \mathbf{A}+k\cdot 0=\det \mathbf{A}
> \end{align}
> > $$


> [!quote] Věta 8. 
> Nechť ${}\mathbf{A}, \mathbf{B}{}$ jsou matice řádu ${}n{}$. Potom
> 
> $$
> \det(\mathbf{A} \cdot \mathbf{B}) = \det \mathbf{A} \cdot \det \mathbf{B}.
> $$
> 
> > [!done]- Důkaz
> > Vyplyne později

