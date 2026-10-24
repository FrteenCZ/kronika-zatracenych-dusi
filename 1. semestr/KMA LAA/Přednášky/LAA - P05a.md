---
type: lecture
status: todo
katedra: KMA
date: 21-10-2026
---

> **Téma:** HODNOST MATICE
> **Koncepty:** [[Matice]]
> **Zdroj**: [[P05a.pdf]]


> [!note] Definice 1.
>  Nechť ${}\mathbf{A} = [a_{ij} ]{}$ je matice typu ${}m/n{}$. Množina všech lineárních kombinací řádků (resp. sloupců) matice ${}\mathbf{A}{}$ je lineární vektorový prostor, který nazýváme **řádkový (resp. sloupcový) prostor matice** ${}\mathbf{A}{}$.

> $$
\mathbf{A}=\left .\begin{bmatrix}
[~~~~~~~~~] \\
[~~~~~~~~~] \\
\vdots \\
[~~~~~~~~~]
\end{bmatrix} \right\} n \text{ řádků v } \mathbb{R}_{n}\to \text{ lineární obal řádků } \mathbf{A} 
$$



Dimenze řádkového (resp. sloupcového) prostoru matice ${}\mathbf{A}{}$ se nazývá **řádková (resp. sloupcová) hodnost matice** ${}\mathbf{A}{}$ a značí ${}\mathrm{h}^r (\mathbf{A}){}$ (resp. ${}\mathrm{h}^s (\mathbf{A}){}$). =Maximální počet LN řádků/sloupečků ${}\mathbf{A}{}$


> [!quote] Věta 1.
>  Pro každou matici ${}\mathbf{A}{}$ platí ${}\mathrm{h}^r(\mathbf{A})=\mathrm{h}^s(\mathbf{A}){}$.


> [!note] Definice 2.
>  Hodnost matice ${}\mathbf{A}{}$ se rovná řádkové nebo sloupcové hodnosti matice ${}\mathbf{A}{}$. Píšeme ${}\mathrm{h}(\mathbf{A}) = \mathrm{h}^r (\mathbf{A}) = \mathrm{h}^s(\mathbf{A}){}$.

> [!note] Definice 3.
> Řekneme, že matice ${}\mathbf{A}{}$ je ve **stupňovitém tvaru**, jestliže platí:
> - je-li v některém řádku ${}i{}$-tý prvek první nenulový, potom ve všech dalších řádkách jsou všechny prvky od 1. až do ${}i{}$-tého včetně rovny ${}0{}$.
> - Matici lze pomocí řádkových elementárních úprav převést na matici ve stupňovitém tvaru.

> [!quote] Věta 2.
>  Hodnost matice ve stupňovitém tvaru je rovna počtu nenulových řádků matice.

> [!example] 
> $$
> \mathbf{A}=\begin{bmatrix}
> 1 & 2 & -1 & 4 & 6 \\
> 0 & 0 & 1 & 2 & 3 \\
> 0 & 0 & 0 & 1 & -1 \\
> 0 & 0 & 0 & 0 & 0
> \end{bmatrix} \implies 3 \text{ řádky jsou LN} \implies \mathrm{h}(\mathbf{A})=3
> $$


> [!quote] Věta 3.
>  Elementární řádkové úpravy matice nemění hodnost matice.

>[!done]- Důkaz
> - výměna 2 řádků, jenom prohazuji prvky
> - vynásobím řádek číslem - dostanu další prvek LP
> - přičtení násobku řádku k druhému ${}\implies{}$ množina všech LK řádků zůstává stejná ${}\implies{}$ zůstane stejný řádkový prostor ${}\implies{}$ zůstane stejná jako dimenze a tedy i hodnost


> [!note] Definice 4.
> Nechť ${}\mathbf{A}{}$ je matice typu ${}m/n{}$. Pro libovolné ${}r \leq \min \{ m, n \}{}$, pro libovolnou volbu ${}1 \leq k_{1} < k_{2} < \dots < k_{r} \leq m{}$ *(vyberu r řádků)* a ${}1 \leq l_{1} < l_{2} < \dots < l_{r} \leq n{}$ *(vyberu r sloupečků)* budeme determinant matice ${}\mathbf{A}(k_{1} , k_{2}, \dots, k_{r} /l_{1} , l_{2}, \dots, l_{r} ){}$ nazývat **minor řádu** ${}r{}$.

> [!example]-
> 
> $$
> \mathbf{A}=\begin{bmatrix}
> 3 & 2 & -1 & 2 \\
> 8 & -2 & 1 & 3 \\
> 0 & 2 & 4 & 1
> \end{bmatrix}
> $$
> - minor řádu 2 : ${}\begin{vmatrix}3 & 2 \\  8 & -2\end{vmatrix}=-22{}$
> - minor řádu 3 : ${}\begin{vmatrix}2 & -1 & 2 \\  -2 & 1 & 3 \\  2 & 4 & 1\end{vmatrix}={}$ 
> 


> [!quote] Věta 4.
>  Nechť ${}\mathbf{A}{}$ je matice typu ${}m/n{}$. Řádková hodnost matice ${}\mathbf{A}{}$ je rovna ${}k{}$ právě tehdy, když existuje nenulový minor řádu ${}k{}$ a všechny minory vyšších řádů jsou rovny nule.
>  > [!done]- Důkaz
> Řádkové elementární úpravy nemění hodnost ani nulovost / nenulovost determinantu
> ${}\implies{}$ vystupňuji matice a vyberu největší řád matice které má nenulový determinant
> ${}\implies{}$ nemůže obsahovat prvky nulového řádku



**Důsledek 5.** 
	Pro libovolnou matici ${}\mathbf{A}{}$ je ${}\mathrm{h}^r (\mathbf{A}) = \mathrm{h}^r (\mathbf{A}^T ){}$, a tím také ${}\mathrm{h}^r (\mathbf{A}) = \mathrm{h}^s (\mathbf{A}){}$.

> [!done]- Důkaz
> Z věty 4 a tvrzení ${}\det \mathbf{A}=\det \mathbf{A}^T{}$ → plyne ${}\mathrm{h(\mathbf{A})=\mathrm{h}(\mathbf{A})^T}\implies \mathrm{h}^r(\mathbf{A})=\mathrm{h}^s(\mathbf{A}){}$


**Důsledek 6.**
	Jestliže ${}\mathbf{A}{}$ je čtvercová matice řádu ${}n{}$, potom ${}\mathrm{n}(A) = n{}$ právě tehdy, když ${}\det \mathbf{A} \neq 0{}$.

> [!done]- Důkaz
> ${}\mathrm{h}(\mathbf{A})=n\Leftrightarrow{}$ po vystupňování není nulový řádek ${}\Leftrightarrow \exists{}$ minor řádku ${}n\neq 0\Leftrightarrow \det \mathbf{A\neq 0}{}$


> [!note] Definice 5.
> Čtvercová matice se nazývá **regulární**, jestliže se její hodnost rovná řádu matice.
> - ${}\Leftrightarrow \det(\mathbf{A})\neq 0\Leftrightarrow{}$ všechny řádky / sloupce jsou LN ${}\Leftrightarrow \exists \mathbf{A}^{-1}{}$
> 
> Čtvercová matice se nazývá **singulární**, jestliže se její hodnost nerovná řádu matice.
> - ${}\Leftrightarrow \det(\mathbf{A})=0\Leftrightarrow{}$ všechny řádky / sloupce jsou LZ ${}\Leftrightarrow \nexists \mathbf{A}^{-1}{}$

Regulární matici lze pomocí řádkových elementárních úprav převést na matici jednotkovou. (Regulární matici lze pomocí sloupcových elementárních úprav převést na jednotkovou matici.)

**Gauss-Jordanova eliminační metoda**
> [!example]-
> 
> $$
\begin{align}
> \mathbf{A}&= \begin{bmatrix}
> 1 & -1 & 2 \\
> 2 & 1 & 1 \\
> -3 & 2 & 1
> \end{bmatrix}\sim \begin{bmatrix}
> 1 & -1 & 2 \\
> 0 & 3 & -3 \\
> 0 & -1 & 7
> \end{bmatrix}\sim \begin{bmatrix}
> 1 & -1 & 2 \\
> 0 & 1 & -1 \\
> 0 & 0 & 6
> \end{bmatrix}\implies \mathrm{h}(\mathbf{A}),\det(\mathbf{A})=18\neq 0 \\
> &\sim \begin{bmatrix}
> 1 & -1 & 2 \\
> 0 & 1 & -1  \\
> 0 & 0 & 1 
> \end{bmatrix}\sim \begin{bmatrix}
> 1 & -1 & 0 \\
> 0 & 1 & 0 \\
> 0 & 0 & 1
> \end{bmatrix}\sim \begin{bmatrix}
> 1 & 0 & 0 \\
> 0 & 1 & 0 \\
> 0 & 0 & 1
> \end{bmatrix}
\end{align}
> $$


> [!note] Definice 6.
> Matice, která vznikne z jednotkové matice provedením jedné řádkové (resp. sloupcové) elementární úpravy, se nazývá **řádková** (resp. **sloupcová**) **elementární** matice.

> [!example]-
>  
>  $$
\begin{align}
>  &\mathbf{A}=\begin{bmatrix}
>  a & b & c \\
>  d & e & f \\
>  g & h & i
>  \end{bmatrix} ~~~ \mathbf{T}=\begin{bmatrix}
>  0 & 1 & 0 \\
>  1 & 0 & 0 \\
>  0 & 0 & 1
>  \end{bmatrix}~~~ \mathbf{T} \text{ je elemtární matice, v } \mathbf{I} \text{ jsem prohodil 1. a 2. řádek} \\
>  &\begin{bmatrix}
>  0 & 1 & 0 \\
>  1 & 0 & 0 \\
>  0 & 0 & 1
>  \end{bmatrix} \cdot\begin{bmatrix}
>  a & b & c \\
>  d & e & f \\
>  g & h & i
>  \end{bmatrix}=\begin{bmatrix}
>  d & e & f \\
>  a & b & c \\
>  g & h & i
>  \end{bmatrix}
\end{align}
>  $$

Provádět řádkovou elementární úpravu matice je totéž jako násobit matici zleva vhodnou řádkovou elementární maticí. Totéž platí pro sloupcové elementární úpravy a násobení zprava vhodnou sloupcovou elementární maticí.

> [!quote] Lemma 7.
>  Nechť ${}\mathbf{A}{}$ je čtvercová matice řádu ${}n{}$, nechť ${}\mathbf{T}{}$ je řádková elementární matice řádu ${}n{}$. Potom ${}\det \mathbf{TA} = \det \mathbf{T} \cdot \det \mathbf{A}{}$.

> [!quote] Věta 8.
> Nechť existuje součin ${}\mathbf{AB}{}$ matic ${}\mathbf{A}{}$, ${}\mathbf{B}{}$. Potom ${}\mathrm{h}(\mathbf{AB}) \leq \min \{ \mathrm{h}(\mathbf{A}),\mathrm{h}(\mathbf{B}) \}{}$.

