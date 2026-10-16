---
type: lecture
status: todo
date: 08-10-2026
katedra: KMA
---

> **Téma:** Grupy a tělesa
> **Koncepty:**
> **Zdroj**: [[P03b.pdf]]

> [!info] Definice 1.
>  Rekněme, že množina  ${}G{}$ je **GRUPA**, jestliže na $G$ je definována binární operace ${}G \times G \to G :{}$ 
>  
>  $$
>  (g, h) \to g \star h \text{ pro každé } g, h \in G
>  $$ 
>  
>  taková, že platí:
> 1. $\forall g, h, k \in G: ~~(g \star h) \star k = g \star (h \star k)$. 
> 2. existuje prvek $g_{0} \in G$ takový, že pro všechny prvky $g \in G$ je $g \star g_{0} = g_{0} \star g = g$.
> 3. Pro každý prvek $g \in G$ existuje $g^{-1}$ tak, že $g \star g^{-1} = g^{-1} \star g = g_{0}$. Přesně lze psát ($G$, $\star$) je grupa s operací ${}\star{}$.


Poznámka 1. 
1. Znak ${}\star{}$ pro grupovou operaci lze vynechat, tedy $gh$ je totéž jako $g \star h$.
2. Prvek $g_{0}$ je určen jednoznačně, nazývá se JEDNOTKOVÝ PRVEK a označuje se $1$.
3. Pro každý prvek $g \in G$ je prvek $g^{-1}$ určen jednoznačně a nazývá se INVERZNÍ PRVEK k prvku $g$.


> [!quote] Lemma 1.
 Nechť ${}G{}$ je grupa. Potom platí:
> 1. $(g^{-1} )^{-1} = g$ pro $\forall g \in G$;
> 2. $(gh)^{-1} = h^{-1} g^{-1}$ pro $\forall g, h \in G$;
> 3. $1^{-1} = 1$.

> Př.:
> ${}(\mathbb{N}_{0},+){}$ ... není grupa kvůli *3.*
> ${}(\mathbb{N}_{0},\cdot){}$ ... není grupa kvůli *3.*
> ${}(\mathbb{Z},+ ){}$ ... je grupa :D
> ${}(\mathbb{Z},\cdot){}$ ... není grupa kvůli *3.*
> ${}(\mathbb{Q},+), (\mathbb{R},+){}$ ... jsou grupa :D
> ${}(\mathbb{Q},\cdot){}$ ... není grupa kvůli *3.* (kvůli ${}0{}$)
> ${}(\mathbb{Q}\setminus \{ 0 \},\cdot){}$ ... je grupa :D



> [!note] Definice 2. 
> Jestliže $G$ je grupa, v níž pro každé dva prvky $g, h \in G$ platí, že $gh = hg$, potom $G$ se nazývá komutativní nebo též ABELOVA GRUPA.


Poznámka 2. 
. Je-li G Abelova grupa, b´yv´a zvykem operaci ps´at znakem +, tedy g + h. Prvek g0 se naz´yv´a nulov´y prvek grupy G a znaˇc´ı se 0. Pro kaˇzd´y prvek g ∈ G se inverzn´ı prvek oznaˇcuje −g a naz´yv´a se opaˇcn´y prvek k prvku g. Takovou grupu pak budeme pˇresnˇe oznaˇcovat (G, +).


> Další př.:
> ${}(P_{n}, +){}$ .... ${}P_{n}{}$ = polynom stupně n ... není grupa (${}(x^{2}+1)+(-x^{2}+x)=x+1{}$)
> ! (${}P_{n},+{}$) ...... ${}P_{n}{}$ = polynom stupně ${}\leq{}$ n .... je grupa i abelovská :D
> (${}P_{n},\cdot{}$) ......... ${}P_{n}{}$ = množina všech polynomů .... není grupa 
> (${}M_{m/n},+{}$) ... ${}M_{m/n}{}$ matice typu m/n .... abelovská grupa :D
> (${}M_{m/n},\cdot{}$) ... ${}M_{m/n}{}$ matice typu m/n .... není


> [!note] Definice 3.
>  Mějme neprázdnou množinu $R$ se dvěma operacemi ${}\star{}$, ${}circ{}$, pro něž platí:
>  1. $(R, \star)$ je Abelova grupa.
>  2. Pro každé $a, b, c \in R$ je 
>  
>  $$
> a \circ (b \circ c) = (a \circ b) \circ c. 
>  $$ 
>  
>   3. Pro každé $a, b, c \in R$ je
>    
>$$
>\begin{align}
>a \circ (b \star c) = (a \circ b) \star (a \circ c), \\
>(b \star c) \circ a = (b \circ a) \star (c \circ a).
>\end{align}
>$$
>    Potom se množina $R$ nazývá OKRUH. 
>    Jestliže operace ${}\circ{}$ je komutativn´ı, tj. a ◦ b = b ◦ a pro kaˇzd´e a, b ∈ R, potom okruh R je komutativn´ı okruh. Prvek e ∈ R okruhu R se naz´yv´a jednotkov´y prvek okruhu R, jestliˇze a ◦ e = e ◦ a = a pro kaˇzd´e a ∈ R. 

Pozn´amka 3. 1. Operace ⋆ se obvykle znaˇc´ı + a naz´yv´a se sˇc´ıt´an´ı v okruhu R a operace ◦ se vˇetˇsinou znaˇc´ı · a naz´yv´a se n´asoben´ı v okruhu R. 2. V okruhu (R, +, ·) plat´ı: a · 0 = 0 · a = 0 pro kaˇzd´e a ∈ R, a · (−b) = (−a) · b = −(a · b) pro kaˇzd´e a, b ∈ R. 3. M´a-li okruh R jednotkov´y prvek, potom je tento prvek urˇcen jednoznaˇcnˇe a znaˇc´ı se 1. 

Definice 4. Netrivi´aln´ı okruh (R, +), · se naz´yv´a TELESO, jestliˇze ( ˇ R\ {0}, ·) je grupa, kde 0 je nulov´y prvek pro operaci +.

> Př.:
> (${}\mathbb{Q},+,\cdot{}$) jsou těleso oproti (${}\mathbb{Z},+,\cdot{}$)
> (${}\mathbb{R},+,\cdot{}$) jsou těleso
> (${}P_{n},+,\cdot{}$) není těleso, je to okruh, ...
 #fixme
  
# LINEARNÍ PROSTORY
> [!note] Definice 5. 
> Neprázdná množina $\mathcal{L}$ se nazývá lineární vektorový prostor, jestliže platí:
>  1. ∀u, v ∈ L existuje jednoznaˇcnˇe urˇcen´y prvek u + v ∈ L naz´yvan´y souˇcet prvk˚u u a v. 
>  2. ∀u ∈ L, ∀λ ˇc´ıslo existuje jednoznaˇcnˇe urˇcen´y prvek λu ∈ L naz´yvan´y n´asobek prvku u ˇc´ıslem λ. 
>  3. u + v = v + u ∀u, v ∈ L. 
>  4. (u + v) + w = u + (v + w) ∀u, v, w ∈ L. 
>  5. ∃ 0 ∈ L tak, ˇze ∀u ∈ L plat´ı u + 0 = 0 + u = u. 
>  6. ∀u ∈ L ∃ − u ∈ L tak, ˇze u + (−u) = (−u) + u = 0. 
>  7. λ(u + v) = λu + λv ∀u, v ∈ L, ∀λ ˇc´ıslo. 
>  8. (λ + α)u = λu + αu ∀u ∈ L, ∀λ, α ˇc´ısla. 
>  9. (λα)u = λ(αu) ∀u ∈ L, ∀λ, α ˇc´ıslo. 
>  10. 1u = u ∀u ∈ L. 

> Př.: 
> 1) ${}P_{n}{}$ ... polynomy stupně nejvýše ${}n{}$ jsou lineární prostor    ! pro LAA
> 2) ${}M_{m/n}{}$ ... množina všech matic stejného typu                    !!! pro LAA
> 	- Speciálně ${}\mathbb{R}_{n}{}$ ... vektory o n-souřadnicích
> 3) ${}C(\langle a,b\rangle){}$ ... množina všech spojitých funkcí na ${}\langle a,b\rangle{}$            pro MA1


Vˇeta 2. Nechˇt L je line´arn´ı vektorov´y prostor. Potom plat´ı: 1. Nulov´y prvek je urˇcen jednoznaˇcnˇe. 2. Jestliˇze x + y = x + z, potom y = z. 3. Ke kaˇzd´emu prvku x ∈ L je opaˇcn´y prvek urˇcen jednoznaˇcnˇe. 4. Jestliˇze x + y = z, potom x = z + (−y). 5. 0x = 0 ∀x ∈ L, λ0 = 0 ∀λ ˇc´ıslo. 6. (−1)x = −x ∀x ∈ L. 7. Jestliˇze λx = 0, potom budˇ λ = 0 nebo x = 0. 

> [!note] Definice 6.
>  Rekneme, ˇze nepr´azdn´a podmnoˇzina ˇ L ′ line´arn´ıho vektorov´eho prostoru L je podprostor prostoru L, jestliˇze plat´ı: x + y ∈ L′ ∀x, y ∈ L′ , λx ∈ L′ ∀x ∈ L′ , ∀λ ˇc´ıslo. 5


