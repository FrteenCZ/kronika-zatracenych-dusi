---
type: lecture
status: todo
date: 01-10-2026
katedra: KMA
---

> **Téma:** ŘEŠENÍ SOUSTAV ROVNIC MATICOVĚ
> **Koncepty:** [[Matice]]
> **Source**: [[P01b-vyplneny.pdf|P01b.pdf]]


> [!note] Definice
>  Následující úpravy matice ${}\mathbf{A}{}$ typu ${}m/n{}$
>  1. vyměnění dvou řádků (resp. sloupců) matice,
>  2. vynásobení řádku (resp. sloupce) matice nenulovým číslem,
>  3. přičtení ${}k{}$-násobku ${}j{}$-tého řádku (resp. sloupce) k řádku (resp. sloupci) ${}i{}$-tému, ${}i \neq j, 1 \leq i, j \leq m{}$ ( resp. ${}1 \leq i, j \leq n{}$)
>  se nazývají **elementární řádkové (resp. sloupcové) úpravy** matice ${}\mathbf{A}{}$.


> [!note] Definice
> Řekneme, že matice ${}\mathbf{A}{}$ je ve **stupňovitém tvaru**, jestliže platí:
> je-li v některém řádku ${}i{}$-tý prvek první nenulový, potom ve všech dalších řádkách jsou všechny prvky od 1. až do ${}i{}$-tého včetně rovny ${}0{}$.

Matici lze pomocí řádkových elementárních úprav převést na matici ve stupňovitém tvaru.
**Postup se nazývá Gaussova eliminační metoda**.


> [!note] Definice 
> Nechť je dána matice ${}\mathbf{A}{}$ typu ${}m/n{}$, ${}n{}$-členný aritmetický vektor ${}x = [x_{1} , x_{2} , \dots, x_{n}]^T {}$, ${}m{}$-členný aritmetický vektor ${}b = [b_{1} , b_{2} , \dots, b_{m} ]^T{}$.
> 
> Potom ${}\mathbf{A}x = b{}$ je **soustava ${}m{}$ lineárních rovnic o ${}n{}$ neznámých**.
> 
> Jestliže ${}\mathbf{A} = [a_{ij} ]{}$, potom ${}\mathbf{A}x = b{}$ rozepíšeme do tvaru:
> $$
\begin{bmatrix}
a_{11} & a_{12} & \dots & a_{1n} \\
a_{21} & a_{22} & \dots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m 2} & \dots & a_{mn}
\end{bmatrix}\cdot \begin{bmatrix}
x_{1} \\
x_{2} \\
\vdots \\
x_{n}
\end{bmatrix}=\begin{bmatrix}
b_{1} \\
b_{2} \\
\vdots \\
b_{m}
\end{bmatrix}
> $$
> t.j.
> $$
\begin{align}
a_{11}x_{1}+a_{12}x_{2}+\dots +a_{1n}x_{n}&=b_{1}, \\
a_{21}x_{1}+a_{22}x_{2}+\dots +a_{2n}x_{n}&=b_{2}, \\
&\vdots \\
a_{m1}x_{1}+a_{m2}x_{2}+\dots +a_{mn}x_{n}&=b_{m},
\end{align}
> $$
> 
> Matice ${}\mathbf{A} = [a_{ij} ]{}$ se nazývá **matice soustavy**.
> Vektor ${}x = [x_{1} , x_{2} , \dots, x_{n} ]^T{}$ **vektor neznámých**.
> Vektor ${}b = [b_{1} , b_{2} , \dots, b_{m} ]^T{}$ **vektor pravých stran**.
> 
> Matici ${}[\mathbf{A}|b] =\begin{bmatrix*}[cccc|c]a_{11} & a_{12} & \dots & a_{1n}  & b_{1} \\ a_{21} & a_{22} & \dots & a_{2n} & b_{2} \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ a_{m1} & a_{m 2} & \dots & a_{mn}  & b_{m}\end{bmatrix*}{}$ nazýváme **rozšířená matice soustavy**.


> [!note] Definice 
> Nechť ${}\mathbf{A}x = b{}$ je soustava ${}m{}$ lineárních rovnic o ${}n{}$ neznámých. Potom každý ${}n{}$-členný aritmetický vektor ${}x{}$, pro který platí ${}\mathbf{A}x = b{}$, nazýváme **řešení soustavy rovnic**.
> Soustavy lineárních rovnic nazýváme **ekvivalentní**, jestliže mají stejné množiny řešení.


> [!quote] Věta 1 
> Jestliže matice ${}[\mathbf{C}|d]{}$ vznikne z matice ${}[\mathbf{A}|b]{}$ užitím řádkových elementárních úprav, potom soustavy lineárních rovnic ${}\mathbf{A}x = b{}$ a ${}\mathbf{C}x = d{}$ jsou ekvivalentní.

