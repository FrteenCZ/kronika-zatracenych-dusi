---
type: lecture
status: todo
date: 08-10-2026
katedra: KMA
---

> **Téma:** Grupy a tělesa, LINEÁRNÍ PROSTORY
> **Koncepty:**
> **Zdroj**: [[P03b.pdf]], [[P03b-vyplneny.pdf]]

> [!info] Definice 1.
>  Rekněme, že množina  ${}G{}$ je **GRUPA**, jestliže na $G$ je definována binární operace ${}G \times G \to G {}$ (*uzavřenost*) : 
>  
>  $$
>  (g, h) \to g \star h \text{ pro každé } g, h \in G
>  $$ 
>  
>  taková, že platí:
> 1. $\forall g, h, k \in G: ~~(g \star h) \star k = g \star (h \star k)$. (*asociativita*)
> 2. existuje prvek $g_{0} \in G$ takový, že pro všechny prvky $g \in G$ je $g \star g_{0} = g_{0} \star g = g$. (*existence neutrálního prvku*)
> 3. Pro každý prvek $g \in G$ existuje $g^{-1}$ tak, že $g \star g^{-1} = g^{-1} \star g = g_{0}$.  (*existence inverzních prvků*)
> 
> Přesně lze psát ($G$, $\star$) je grupa s operací ${}\star{}$.


Poznámka 1. 
1. Znak ${}\star{}$ pro grupovou operaci lze vynechat, tedy $gh$ je totéž jako $g \star h$.
2. Prvek $g_{0}$ je určen jednoznačně, nazývá se JEDNOTKOVÝ PRVEK a označuje se $1$.
3. Pro každý prvek $g \in G$ je prvek $g^{-1}$ určen jednoznačně a nazývá se INVERZNÍ PRVEK k prvku $g$.


> [!quote] Lemma 1.
 Nechť ${}G{}$ je grupa. Potom platí:
> 1. $(g^{-1} )^{-1} = g$ pro $\forall g \in G$;
> 2. $(gh)^{-1} = h^{-1} g^{-1}$ pro $\forall g, h \in G$;
> 3. $1^{-1} = 1$.

> [!example]-
> 1) ${}(\mathbb{N}_{0},+){}$ ... není grupa kvůli *3.*
> 2) ${}(\mathbb{N}_{0},\cdot){}$ ... není grupa kvůli *3.*
> 3) ${}(\mathbb{Z},+ ){}$ ... je grupa :D
> 4) ${}(\mathbb{Z},\cdot){}$ ... není grupa kvůli *3.*
> 5) ${}(\mathbb{Q},+), (\mathbb{R},+){}$ ... jsou grupa :D
> 6) ${}(\mathbb{Q},\cdot){}$ ... není grupa kvůli *3.* (kvůli ${}0{}$)
> 7) ${}(\mathbb{Q}\setminus \{ 0 \},\cdot),(\mathbb{R}\setminus \{ 0 \},\cdot),(\mathbb{C}\setminus \{ 0 \},\cdot){}$ ... je grupa :D



> [!note] Definice 2. 
> Jestliže $G$ je grupa, v níž pro každé dva prvky $g, h \in G$ platí, že $gh = hg$, potom $G$ se nazývá komutativní nebo též ABELOVA GRUPA.

→ u číselných množin jsou všechny grupy abelovksé


**Poznámka 2.** 
Je-li ${}G{}$ Abelova grupa, bývá zvykem operaci psát znakem ${}+{}$, tedy ${}g + h{}$. 
Prvek ${}g_{0}{}$ se nazývá nulový prvek grupy ${}G{}$ a značí se ${}0{}$. 
Pro každý prvek ${}g \in G{}$ se inverzní prvek označuje ${}−g{}$ a nazývá se opačný prvek k prvku ${}g{}$.
Takovou grupu pak budeme přesně označovat ${}(G, +){}$.


> [!example]-
> 8) ${}(P_{n}, +){}$ .... ${}P_{n}{}$ = polynom stupně n ... není grupa (${}(x^{2}+1)+(-x^{2}+x)=x+1{}$)
> 9) ! (${}P_{n},+{}$) ...... ${}P_{n}{}$ = polynom stupně ${}\leq{}$ n .... je grupa i abelovská :D
> 10) (${}P_{n},\cdot{}$) ......... ${}P_{n}{}$ = množina všech polynomů .... není grupa 
> 11) (${}M_{m/n},+{}$) ... ${}M_{m/n}{}$ matice typu m/n .... abelovská grupa :D
> 12) (${}M_{m/n},\cdot{}$) ... ${}M_{m/n}{}$ matice typu m/n .... není
> 13) Množina všech permutací a operace skládání je grup ale není komutativní (není abelovksá)
> 14) Množina všech regulačních matic řádu ${}n{}$ a násobení je grup ale není komutativní (není abelovksá)


> [!note] Definice 3.
>  Mějme neprázdnou množinu $R$ se dvěma operacemi ${}\star{}$, ${}\circ{}$, pro něž platí:
>  1. $(R, \star)$ je Abelova grupa.
>  2. Pro každé $a, b, c \in R$ je *asociativní*
>  
>  $$
> a \circ (b \circ c) = (a \circ b) \circ c. 
>  $$ 
>  
>   3. Pro každé $a, b, c \in R$ je *distributivní*
>    
>$$
>\begin{align}
>a \circ (b \star c) = (a \circ b) \star (a \circ c), \\
>(b \star c) \circ a = (b \circ a) \star (c \circ a).
>\end{align}
>$$
> Potom se množina $R$ nazývá **OKRUH**. 
> 
> Jestliže operace ${}\circ{}$ je *komutativní*, tj. ${}a \circ b = b \circ a{}$ pro každé ${}a, b \in R{}$, potom okruh ${}R{}$ je **komutativní okruh**.
> 
> Prvek ${}e \in R{}$ **okruhu** ${}R{}$ se nazývá jednotkový prvek okruhu ${}R{}$, jestliže ${}a \circ e = e \circ a = a{}$ pro každé ${}a \in R{}$. 

**Poznámka 3**.
1. Operace ${}\star{}$ se obvykle značí ${}+{}$ a nazývá se sčítání v okruhu ${}R{}$ a operace ${}\circ{}$ se většinou značí ${}\cdot{}$ a nazývá se násobení v okruhu ${}R{}$.
2. V okruhu ${}(R, +, \cdot){}$ 
	1. platí: ${}a \cdot 0 = 0 \cdot a = 0{}$ pro každé ${}a \in R{}$,
	2. ${}a \cdot (-b) = (-a) \cdot b = -(a \cdot b){}$ pro každé ${}a, b \in R{}$. 
3. Má-li okruh ${}R{}$ jednotkový prvek, potom je tento prvek určen jednoznačně a značí se ${}1{}$. 
→ v okruhu nemusí existovat ${}a^{-1}{}$ pro operaci ${}\circ{}$

> [!note] Definice 4.
> Netriviální okruh ${}(R, +,\cdot){}$ se nazývá **TĚLESO**, jestliže ${}( R \setminus {0}, \cdot){}$ je grupa, kde ${}0{}$ je nulový prvek pro operaci ${}+{}$.

→ ${}(R\setminus \{ 0 \},\cdot){}$ nemusí být komutativní
	pokud ano, jde o komutativní těleso

> [!example]
> (${}\mathbb{Q},+,\cdot{}$) jsou těleso oproti (${}\mathbb{Z},+,\cdot{}$)
> (${}\mathbb{R},+,\cdot{}$) jsou těleso ${}\Leftrightarrow(\mathbb{R},+){}$ je abelovská grupa, ${}(\mathbb{R}\setminus \{ 0 \},\cdot){}$ je abelovská grupa a platí distributivita
> (${}P_{n},+,\cdot{}$) není těleso, je to okruh, komutativní, s jednotkovým prvkem nemáme inverzní prvky
> ${}(\mathbf{M}_{m,n},+,\cdot){}$ není těleso, ani okruh 
  
# LINEÁRNÍ PROSTORY
> [!note] Definice 5. 
> Neprázdná množina $\mathcal{L}$ se nazývá lineární vektorový prostor, jestliže platí:
>  1. ${}\forall u, v \in \mathcal{L}{}$ existuje jednoznačně určený prvek ${}u + v \in  \mathcal{L}{}$ nazývaný součet prvků ${}u{}$ a ${}v{}$. - *sčítání prvků (uzavřená)*
>  2. ${}\forall u \in  \mathcal{L}, \forall \lambda {}$ číslo existuje jednoznačně určený prvek ${}\lambda u \in  \mathcal{L}{}$ nazývaný násobek prvku ${}u{}$ číslem ${}\lambda{}$. - *násobení prvků (uzavřená)*
>  3. ${}u + v = v + u ~~~~~~ \forall u, v \in  \mathcal{L}{}$. - *komutativní*
>  4. ${}(u + v) + w = u + (v + w) ~~~~~~ \forall u, v, w \in  \mathcal{L}{}$.  - *asociativní*
>  5. ${}\exists 0 \in  \mathcal{L}{}$ tak, že ${}\forall u \in  \mathcal{L}{}$ platí ${}u + 0 = 0 + u = u{}$. - *nulový prvek*
>  6. ${}\forall u \in  \mathcal{L} ~~~~~~~~ \exists - u \in  \mathcal{L}{}$ tak, že ${}u + (-u) = (-u) + u = 0{}$.  - *opečné prvky*
>  7. ${}\lambda (u + v) = \lambda u + \lambda v ~~~~~~~~ \forall u, v \in  \mathcal{L}, \forall \lambda{}$  číslo. 
>  8. ${}(\lambda  + \alpha )u = \lambda u + \alpha u ~~~~~~~~ \forall u \in  \mathcal{L}, \forall \lambda , \alpha{}$  čísla. 
>  9. ${}(\lambda \alpha )u = \lambda (\alpha u) ~~~~~~~~ \forall u \in  \mathcal{L}, \forall \lambda , \alpha{}$  číslo. 
>  10. ${}1u = u ~~~~~~~~ \forall u \in  \mathcal{L}{}$. 

${}\implies{}$ pro + platí 1., 2., 3., 4., 5., 6. - abelovská grupa s vnější operací číselného násobku

> [!example]- Příklady lineárních prostorů
> 1) ${}P_{n}{}$ ... polynomy stupně nejvýše ${}n{}$ jsou lineární prostor - *! pro LAA*
> 2) ${}M_{m/n}{}$ ... množina všech matic stejného typu - *!!! pro LAA*
> 	- Speciálně ${}\mathbb{R}_{n}{}$ ... vektory o n-souřadnicích
> 3) ${}C(\langle a,b\rangle){}$ ... množina všech spojitých funkcí na ${}\langle a,b\rangle{}$ - *pro MA1*

Pravidla pro počítání v lineárních prostorech
> [!quote] Věta 2.
>  Nechť ${}\mathcal{L}{}$ je lineární vektorový prostor. Potom platí:
>   1. Nulový prvek je určen jednoznačně.
>   2. Jestliže ${}x + y = x + z{}$, potom ${}y = z{}$.
>   3. Ke každému prvku ${}x \in  \mathcal{L}{}$ je opačný prvek určen jednoznačně.
>   4. Jestliže ${}x + y = z{}$, potom ${}x = z + (-y){}$.
>   5. ${}0x = 0 ~~~~~ \forall x \in  \mathcal{L}{}$,
>       ${}\lambda 0 = 0 ~~~~\forall \lambda{}$  číslo.
>   6. ${}(-1)x = -x ~~~~ \forall x \in  \mathcal{L}{}$.
>   7. Jestliže ${}\lambda x = 0{}$, potom buď ${}\lambda  = 0{}$ nebo ${}x = 0{}$. 

> [!done]- Důkaz
> 1) Nechť ${}o_{1},o_{2}{}$ jsou 2 různé nulové prvky
>    ${}o_{1}=o_{1}+o_{2}=o_{2}{}$ ! ${}o_{1}=o_{2}\implies{}$ je pouze jeden
> 
> 2) ${}x+y=x+z ~~~ /+(-x){}$
>    ${}(-x)+x+y=(-x)+x+z{}$
>    ${}y=z{}$
> 
> 3) pro ${}x{}$ jsou ${}x_{1},x_{2}{}$ 2 různé opačné prvky
>    ${}x+x_{1}=\mathbb{0} \land x+x_{2}=\mathbb{0}{}$
>    ${}x+x_{1}=x+x_{2}{}$
>    ${}x_{1}=x_{2}{}$ ! jsou stejné ${}\implies-x{}$ je pouze jeden
> 
> 4) ${}x+y=z ~~~~ /+(-y){}$
>    ${}x+y+(-y)=z+(-y){}$
>    ${}x=z+(-y){}$
> 
> 5) ${}\lambda x=(\lambda+0)x=\lambda+0x{}$
>    ${}0x=\lambda x+(-\lambda)x=\mathbb{0}{}$
>    ${}\lambda x=\lambda(x+\mathbb{0})=\lambda x+\lambda \mathbb{0}\implies\lambda \mathbb{0}=\lambda x+(-\lambda)x=\mathbb{0}{}$
> 
> 6) ${}x+(-1)x=1x+(-1)x=(1-1)x=0x=\mathbb{0}{}$
> 
> 7) ${}\lambda x=\mathbb{0}\to \begin{cases}\lambda=0  & 0x=\mathbb{0} \\  \lambda\neq 0 & x=1x=\frac{\lambda}{\lambda}x=\frac{1}{\lambda}\lambda x=\mathbb{0}\end{cases}{}$


> [!note] Definice 6.
>  Rekneme, že neprázdná podmnožina  ${}\mathcal{L}'{}$ lineárního vektorového prostoru ${}\mathcal{L}{}$ je **podprostor** prostoru ${}\mathcal{L}{}$, jestliže platí:
>  
> ${}x + y \in  \mathcal{L}'  ~~~~ \forall x, y \in  \mathcal{L}'{}$, - *uzavřené na sčítání prvků*
>  ${} \lambda x \in  \mathcal{L}' ~~~~ \forall x \in  \mathcal{L}' , \forall \lambda  \text{ číslo}{}$. - *a násobení prvků číslem*


