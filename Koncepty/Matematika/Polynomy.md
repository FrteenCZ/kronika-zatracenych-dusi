---
type: concept
aliases:
  - Mnohočlen
status: done
katedra: KMA
---
**source**: [[LAA - P01a]]

> [!info] **Definice**:
> Nechť ${}a_{0},a_{1},\dots a_{n}\in \mathbb{C},a_{n}\neq 0{}$. Funkce ${}p : \mathbb{C} \to \mathbb{C}{}$ definovaná předpisem
> $$
> p(x) = a_n x^n + a_{n−1}x^{n−1} + \dots + a_{1} x + a_{0}
> $$
> se nazývá **polynom (mnohočlen) stupně** $n$ - píšeme $st(p(x))=n$.
>
> Čísla $a_{0} , a_{1} , \dots , a_{n}$ se nazývají **koeficienty polynomu**.

> -  ${}p(x)=a_{0},a_{0}\neq 0\to{}$polynom nultého stupně ${}\to{}$ číslo
> -  ${}p_{1}(x)=a_{1}x+a_{0},a_{1}\neq 0\to{}$                1. stupně ${}\to{}$ lineární
> -  ${}p_{2}(x)=a_{2}x^{2}+a_{1}x+a_{0},a_{2}\neq 0\to{}$    2. stupně ${}\to{}$ kvadratický
> -                                                                 3. stupně ${}\to{}$ kubický

Jestliže všechny koeficienty polynomu = 0, potom ${}p=0{}$ se nazývá **nulový polynom**. ${}st(0)=-\infty{}$

Jestliže všechny koeficienty polynomu $\in \mathbb{R}$, potom mluvíme o **polynomu s reálnými koeficienty**.


číslo $c \in \mathbb{C}$ se nazývá **kořen** polynomu $p(x)$, když $p(c)=0$

> Algebraické rovnice: ${}p_{n}(x)=0{}$    ${}c=?{}$
>
> ${}p_{1}(x)=3x+9\to?c~~~~~~3c+9=0\to c=-3{}$
> ${}p_{2}(x)=x^{2}+6x+9\to?c~~~~~~c_{1,2}=-3{}$
> ${}p_{3}(x)=2x^{3}+6x+1\to?c{}$


---

> [!quote] Věta 1 (Základní věta algebry)
> Každý polynom stupně $\geq$ 1 má v $\mathbb{C}$ alespoň 1 kořen



# Základní operace
$$
\begin{gathered}
p_{1}(x)=3x^{2}-9x+2 && p_{2}(x)=2x^{3}+5x 
\end{gathered}
$$
## sčítání
sčítáme koeficienty u stejných mocnin
$$
p_{1}(x)+p_{2}(x)=2x^{3}+3x^{2}-4x+2
$$
 obecně ${}st(p_{1}(x)+p_{2}(x))\leq \mathrm{max}\{ st(p_{1}(x)),st(p_{2}(x)) \}{}$

## násobení
$$	 p_{1}(x)\cdot p_{2}(x)=(3x^{2}-9x+2)\cdot(2x^{3}+5x)=6x^5-18x^4+4x^{3}+15x^{3}-45x^{2}+10x 	  $$
obecně ${}st(p_{1}(x)\cdot p_{2}(x))=st(p_{1}(x))+st(p_{2}(x)){}$ → umíme víc než budeme potřebovat
  
## odčítání
násobení -1 a sčítání
$$ p_{1}(x)-p_{2}(x)=p_{1}(x)+(-1)\cdot p_{2}(x)=-2x^{3}+3x^{2}-14x+2 $$
## dělení
${}\dfrac{a(x)}{b(x)}=q(x)+\dfrac{r(x)}{b(x)}{}$

Algoritmus pro dělení: [wiki](https://cs.wikipedia.org/wiki/D%C4%9Blen%C3%AD_polynomu_polynomem)
$$
\begin{align}
p_{1}(x):p_{2}(x)&= \text{hotovo} ~~~~ st(p_{1}(x))\text{ není}\geq st(p_{2}(x))\\ \\
& ~~~~~~~~~~~a(x) ~~~~~~~~~~~~~~~~~~b(x) ~~~~~~~~~~~~~~~~~ q(x) ~~~~~~~~~~~~~~~\frac{r(x)}{b(x)}\\
p_{2}(x):p_{1}(x)&= (2x^{3}+5x):(3x^{2}-9x+2)=\frac{2}{3}x+2+\frac{\frac{65}{3}x-4}{3x^{2}-9x+2} \\
&-(2x^{3})-6x^{2}+\frac{4}{3}x) \\
& ---------- \\
& + 6x^{2}-\frac{11}{3}x \\
& -(6x^{2}-18x+4) \\
& ---------- \\
& \frac{65}{3}x-4  \to \text{zbytek po dělení }r(x)
\end{align}
$$
---

> [!quote] Věta 2
Jsou-li ${}a(x),{}$ ${}b(x){}$ dva polynomy (${}st(a(x))\geq st(b(x)){}$), polynom ${}b(x){}$ není nulový, potom existují a jsou jednoznačně určeny polynomy $q(x)$, $r(x)$ takové, že $st(r(x)) < st(b(x))$ a platí $a(x) =b(x)q(x) + r(x)$.
>
Speciálně, je-li $b(x) = x−c$, potom existuje polynom
$q(x)$ tak, že $a(x) = (x − c)q(x) + r$, kde navíc $r = a(c)$.

> [!quote] Věta 3
> Je-li $c$ kořen polynomu $a(x)$, potom existuje polynom $q(x)$ takový, že $a(x) = (x − c)q(x)$ a platí $st(q(x)) = st(a(x)) − 1$.

> ${}a(x){}$ je stupně ${}n{}$
> ${}(x-c){}$ je stupně ${}1{}$
> ${}q(x){}$ je stupně ${}n-1{}$

> ${}(x-c){}$ se nazývá kořenový činitel

> Odvodíme, že polynom stupně ${}n{}$ má v ${}\mathbb{C}{}$ ${}n{}$ kořenů:
> ${}a(x)=(x-c_{1})\cdot q_{1}(x){}$ ... kořen ${}c_{1}{}$
> ${}a(x)=(x-c_{1})(x-c_{2})\cdot q_{2}(x){}$ ... kořen ${}c_{2}{}$
> ${}\vdots{}$   opakuj n-krat
> ${}a(x)=(x-c_{1})(x-c_{2})(x-c_{3})\dots(x-c_{n})\cdot q_{n}(x){}$ ... kořen ${}c_{n}{}$ → ${}st(q_{n}(x))=0{}$, ${}q_{n}(x)=a_{n}{}$

> [!quote] Věta 4
> Každý polynom ${}a(x){}$ stupně $\geq 1$ lze v ${}\mathbb{C}{}$ vyjádřit ve tvaru
> $$
> a(x) = a_{n} (x − c_{1} )(x − c_{2} ) \dots (x − c_{n} ),
> $$
> kde $c_{1}, c_{2} , \dots, c_{n} \in \mathbb{C}$ jsou kořeny polynomu $a(x)$.
>
> Tento zápis polynomu se nazývá **rozklad polynomu na kořenové činitele**.

> Pozn.: 
> ${}c_{i},i=1,2,\dots,n{}$ mohou být některé stejné

> [!tip]
> ${}c{}$ je kořen, potom ${}c{}$ dělí ${}a_{0}{}$ ${}\implies c|a_{0}{}$ ${}\implies{}$ umíme najít všechny celočíselné kořeny



> [!quote] Věta 5
>  Je-li číslo $c \in \mathbb{C}$ kořenem polynomu $a(x)$ s reálnými koeficienty, potom také číslo komplexně sdružené $\overline{c} \in \mathbb{C}$ je kořenem polynomu $a(x)$. 

> [!tip] **Důsledek**
Každý polynom s reálnými koeficienty lichého stupně má alespoň jeden reálný kořen. 

# Reálný rozklad polynomu
Jestliže v rozkladu polynomu (s reálnými koeficienty) na kořenové činitele roznásobíme každé dva kořenové činitele, které odpovídají dvojici komplexně sdružených kořenů, získáme **reálný rozklad polynomu**.

> Př.:
> ${}a(x)=a_{n}(x-c_{1})(x-c_{2})\dots(x^{2}+b'_{1}x+c'_{1})(x^{2}+b'_{2}x+c'_{2})\dots{}$
>        pro reálné kořeny      pro komplexní kořeny (${}D<0{}$)

# Hornerovo schéma
Dělení polynomu $a(x)$ polynomem $x − c$ lze jednoduše zapsat do tabulky. Tento způsob dělení polynomu polynomem $x − c$ se nazývá **Hornerovo schéma**.

Označme $a(x) = (x − c)q(x) + r$, kde
$$
\begin{align}
a(x) = a_{n} x^{n} + a_{n−1}x^{n−1} + \dots + a_{1} x + a_{0}, \\
q(x) = q_{n−1} x^{n−1} + q_{n−2} x^{n−2} + \dots + q_{1} x + q_{0} .
\end{align}
$$

Dělení zapíšeme do tabulky takto:

$$
\begin{array}{c|ccccccc}
 & a_n & a_{n-1} & a_{n-2} & a_{n-3} & \ldots & a_1 & a_0 \\
 & &  + & + & + & \ldots & + & +\\
 c&  & q_{n-1} c & q_{n-2} c & q_{n-3} c & \ldots & q_1 c & q_{0}c \\
\hline   & q_{n-1} & q_{n-2} & q_{n-3} & q_{n-4} & \ldots & q_0 & r\\
\end{array}
$$
