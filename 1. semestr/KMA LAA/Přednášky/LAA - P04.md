---
type: lecture
status: todo
katedra: KMA
date: 15-10-2026
---

> **Téma:** LINEÁRNÍ ZÁVISLOST A NEZÁVISLOST, BÁZE A DIMENZE PROSTORU, SOUŘADNICE PRVKU
> **Koncepty:**
> **Zdroj**: [[P04.pdf]], [[P04-vyplneny.pdf]]

# LINEÁRNÍ ZÁVISLOST A NEZÁVISLOST, BÁZE A DIMENZE PROSTORU, SOUŘADNICE PRVKU
 >[!note] Definice 1.
 > Nechť ${}\mathcal{L}{}$ je lineární vektorový prostor, nechť ${}v_{1}, v_{2} , \dots, v_{n} \in \mathcal{L}{}$, nechť ${}\lambda_{1} , \lambda_{2} , \dots, \lambda_{n}{}$ jsou čísla. Prvek ${}\lambda_{1} v_{1} + \lambda_{2} v_{2} + \dots + \lambda_{n} v_{n} \in \mathcal{L}{}$ se nazývá **lineární kombinace** prvků ${}v_{1} , v_{2} , \dots, v_{n}{}$ s koeficienty ${}\lambda_{1} , \lambda_{2}, \dots, \lambda_{n}{}$.
 
 
Lineární kombinace ${}\lambda_{1} v_{1} + \lambda_{2}v_{2} + \dots +\lambda_{n}v_{n}{}$ se nazývá **netriviální**, jestliže existuje ${}i \in \{ 1, 2, \dots, n \}{}$ takové, že ${}\lambda_{i} \neq 0{}$. Lineární kombinace ${}\lambda_{1}v_{1} + \lambda_{2} v_{2} +\dots +\lambda_{n} v_{n} {}$ se nazývá **triviální**, jestliže ${}\lambda_{i} = 0{}$ pro každé ${}i = 1, 2, \dots, n{}$.

> ${}0v_{1}+0v_{2}+0v_{3}=\mathbb{0}{}$ - nulový prvek


Prvky ${}v_{1} , v_{2} , \dots, v_{n}{}$ se nazývají **lineárně nezávislé** (LN), jestliže každá jejich netriviální lineární kombinace je nenulový prvek.

Prvky ${}v_{1} , v_{2} , \dots, v_{n}{}$ se nazývají **lineárně závislé** (LZ), jestliže nejsou lineárně nezávislé, t.j. jestliže existuje jejich netriviální lineární kombinace, která se rovná nulovému prvku.

> [!example]-
> 1) ${}P_{2}:\begin{align}p_{1}(x)&=x^{2}-1\\ p_{2}(x)&=-2x^{2}+2\end{align}{}$ ? ${}p_{1}(x),p_{2}(x){}$ jsou LZ nebo LN
> 	${}2p_{1}(x)+1p_{2}(x)=0{}$ je netriviální LK ${}\implies{}$ jsou LZ
> 	${}p_{2}(x)=-2p_{1}(x){}$
>
>
>2) ${}\mathbb{R}_{2}:\begin{align}&x=(1,3)^T \\  &y=(2,1)^T\end{align}{}$  ? ${}x,y{}$ jsou LN? 
>	
>	$$
>	\begin{align}
>	k_{1}x+k_{2}y&=\mathbb{0} \\
>	k_{1}\begin{bmatrix}
>	1 \\
>	3
>	\end{bmatrix}+k_{2}\begin{bmatrix}
>	2 \\
>	1
>	\end{bmatrix}&=\begin{bmatrix}
>	0 \\
>	0
>	\end{bmatrix} \\ \\
>	k_{1}+2k_{2}&=0 \\
>	3k_{1}+k_{2}&=0 \\
>	 \\
>	
>	k_{1}&=0 \\
>	k_{2}&=0 \\
>	\text{ pouze triviální LK } &\implies x,y \text{ jsou LN}
>	\end{align}
>	$$

> [!quote] Věta 1.
>  Nechť ${}\mathcal{L}{}$ je lineární vektorový prostor, nechť ${}v_{1}, v_{2} , \dots, v_{n} \in \mathcal L{}$ jsou prvky tohoto prostoru. Tyto prvky jsou lineárně závislé právě tehdy, když alespoň jeden z nich se dá vyjádřit jako lineární kombinace ostatních.

> [!done]- Důkaz
> ${}\implies{}$ předpokládám, že ${}u_{1},\dots,u_{n}{}$, které jsou LZ
> 	${}k_{1}v_{1}+\dots+k_{i}v_{i}+k_{n}v_{n}=\mathbb{0}{}$  ${}\exists k_{i}\neq 0{}$
> 	vyjádříme ${}k_{i}\implies \begin{align}k_{i}b_{i}&=-k_{1}v_{1}-\dots-k_{n}v_{n} \\  v_{i}&=\frac{k_{1}}{k_{i}}v_{1}-\dots-\frac{k_{n}}{k_{i}}v_{i}\end{align}{}$ lze vyjádřit LK ostatních
> 	${}\impliedby v_{i}{}$ lze vyjádřit LK ostatních ${}\to v_{i}=k_{1}v_{1}+\dots+k_{n}v_{n}\implies k_{1}v_{1}+\dots-1v_{1}+\dots+k_{n}v_{n}=\mathbb{0}{}$
> 	${}k_{i}=-1{}$ ... netriviální ... ${}v_{1},v_{2},\dots,v_{n}{}$ jsou LZ

Každá podmnožina lineárně nezávislé množiny je opět lineárně nezávislá.

> [!quote] Věta 2.
>  Jestliže ${}M = \{ u_{1} , u_{2} , \dots, u_{n} \}{}$ je podmnožina lineárního vektorového
prostoru ${}\mathcal{L}{}$, potom množina všech lineárních kombinací prvků ${}u_{1}, u_{2}, \dots, u_{n}{}$ se nazývá lineární obal množiny ${}M{}$ a značí ${}\langle M \rangle = \{ \lambda_{1} u_{1} + \lambda_{2} u_{2} + \dots + \lambda_{n} u_{n} : \lambda_{1}, \lambda_{2} , \dots, \lambda_{n} \text{ čísla} \}{}$
>
> Pro každou neprázdnou konečnou množinu ${}M \subseteq  \mathcal{L}{}$ je ${}\langle M \rangle{}$ podprostor prostoru ${}\mathcal{L}{}$.

> [!done]- Důkaz
> ${}\begin{align}\forall x \in \left< M \right>~x=\alpha_{1}u_{1}+\dots+\alpha_{n}u_{n} \\  \forall y \in \left< M \right>~y=\beta_{1}u_{1}+\dots+\beta_{n}u_{n}\end{align}{}$ ${}\begin{align}x+y&=(\alpha_{1}u_{1}+\dots+\alpha_{n}u_{n})+(\beta_{1}u_{1}+\dots+\beta_{n}u_{n})= \\  &=(\alpha_{1}+\beta_{1})u_{1}+\dots(\alpha_{n}+\beta_{n})u_{n}\in \left< M \right>\end{align}{}$
> *uzavřenost na sčítání*
>
>${}\begin{align}&\forall x \in \left< M \right>~x=\alpha_{1}u_{1}+\dots+\alpha_{n}u_{n} \\  &\forall k \in \mathbb{R}\end{align}{}$ ${}k\cdot x=k(\alpha_{1}u_{1}+\dots+\alpha_{n}u_{n})=k\cdot\alpha_{1}\cdot u_{1}+\dots+k\cdot\alpha_{n}\cdot u_{n} \in \left< M \right>{}$


> [!note] Definice 2.
>  Říkáme, že množina ${}M{}$ **generuje** lineární vektorový prostor ${}\mathcal{L}{}$ (je množinou generátorů, je generující množinou), jestliže ${}\mathcal{L} = \langle M \rangle{}$, t.j. každý prvek prostoru ${}\mathcal{L}{}$ lze psát jako lineární kombinaci prvků množiny ${}M{}$.
>  
>  Existuje-li konečná generující množina ${}M{}$ prostoru ${}\mathcal{L}{}$, říkáme, že prostor ${}\mathcal{L}{}$ je **konečně generovaný**.

> Nadmnožina generující množiny je generující


> [!note] Definice 3.
>  Nechť  ${}\mathcal{L}{}$ je konečně generovaný lineární vektorový prostor. Lineárně nezávislá, generující množina prostoru ${}\mathcal{L}{}$ se nazývá **báze prostoru** ${}\mathcal{L}{}$.

> Maximální LN a minimální generující

> [!quote] Věta 3.
>  V každém nenulovém, konečně generovaném lineárním vektorovém prostoru existuje báze.

> [!done]- Důkaz
> generující množina ${}v_{1},\dots,v_{n}\to{}$ jsou ${}v_{1},\dots,v_{n}{}$ LN?
> - ANO ... je to báze
> - NE ... umím podle věty 1 aspoň jeden prvek vyjádřit pomocí ostatních
> 	- např. ${}v_{1}{}$ ... ${}v_{1}=\alpha_{2}\cdot v_{2}+\dots+\alpha_{n}v_{n}{}$
> 	- ${}v_{1}{}$ vyhodíme z generující množiny a ukážeme, že ${}v_{2},\dots,v_{n}{}$ opět generuj ${}\mathcal{L}{}$
> 	- ${}\forall x \in \mathcal{L}{}$
> 	- ${}x=\lambda_{1}v_{1}+\lambda_{2}+v_{2}+\dots+\lambda_{n}v_{n}{}$
> 	- ${}x=\lambda_{1}(\alpha_{2}v_{2}+\dots+\alpha_{n}v_{n})+\lambda_{2}v_{2}+\dots+\lambda_{n}v_{n}{}$
> 	- ${}x=(\lambda_{1}\alpha_{2}+\lambda_{2})v_{2}+\dots+(\lambda_{1}\alpha_{n}+\lambda_{n})v_{n}\implies{}$ je generující


> [!quote] Věta 4 (Steinitz) (věta o výměně).
>  Nechť ${}\mathcal{L}{}$ je nenulový lineární vektorový prostor, nechť ${}M = \{ g_{1} , g_{2}, \dots, g_{m} \}{}$ je množina generátorů prostoru ${}\mathcal{L}{}$, nechť ${}N = \{ b_{1}, b_{2}, \dots, b_{n} \}{}$ je množina lineárně nezávislých prvků prostoru ${}\mathcal{L}{}$. Potom ${}n \leq m{}$ a některých ${}n{}$ prvků množiny ${}M{}$ lze nahradit prvky množiny ${}N{}$ tak, že vzniklá množina opět generuje prostor ${}\mathcal{L}{}$.



**Důsledky**
1. Jestliže množina ${}\{ g1 , g2, ..., gm \}{}$ generuje prostor ${}\mathcal{L}{}$, pak každá lineárně nezávislá množina v ${}\mathcal{L}{}$ má maximálně ${}m{}$ prvků.
> [!done]- Důkaz
> Ze Steinitzovy věty ${}n\leq m{}$

2. Každou lineárně nezávislou množinu v prostoru ${}\mathcal{L}{}$ lze doplnit do báze prostoru ${}\mathcal{L}{}$.
> [!done]- Důkaz
> Vezmu ji a doplním podle Steinitzovy věty do libovolné generující množiny z ${}\mathcal{L}{}$, podle důkazu Věty 3 z ní vyberu LN podmnožinu

3. Každé dvě báze nenulového, konečně generovaného lineárního vektorového prostoru mají stejný počet prvků.
> [!done]- Důkaz
> 2x použiju Steinitzovu větu, kdy ${}N{}$ i ${}M{}$ jsou báze ${}\implies \begin{aligned}n\leq m \text{ z 1. použití} \\  n\geq m \text{ z 2. použití}\end{aligned}, n=m{}$


> [!note] Definice 4.
>  Počet prvků báze konečně generovaného lineárního vektorového prostoru se nazývá **dimenze prostoru** ${}\mathcal{L}{}$ a značí dim ${}\mathcal{L}{}$.


4. Nechť ${}g_{1} , g_{2} , \dots, g_{n}{}$ je ${}n{}$ lineárně nezávislých prvků lineárního vektorového prostoru ${}\mathcal{L}{}$, nechť dim ${}\mathcal{L} = n{}$. Potom ${}g_{1}, g_{2} , \dots, g_{n}{}$ je báze prostoru ${}\mathcal{L}{}$.

> [!quote] Věta 5.
>  Každý prvek lineárního vektorového prostoru ${}\mathcal{L}{}$ lze jednoznačně vyjádřit jako lineární kombinaci prvků báze.

> [!done]- Důkaz
> Zvolme bázi ${}b_{1},b_{2},\dots,b_{n}{}$ a pro ${}\forall x \in \mathcal{L}{}$ existují 2 různé vyjádření
> ${}\begin{aligned}x=\alpha_{1}b_{1}+\alpha_{2}b_{2}+\dots+\alpha_{n}b_{n} \\  x=\beta_{1}b_{1}+\beta_{2}b_{2}+\dots+\beta_{n}b_{n}\end{aligned}{}$, potom: $\begin{aligned}0 = x - x &= (\alpha_{1}b_{1}+\dots+\alpha_{n}b_{n}) - (\beta_{1}b_{1}+\dots+\beta_{n}b_{n})= \\&= (\alpha_{1}-\beta_{1})b_{1}+\dots+(\alpha_{n}-\beta_{n})b_{n}\end{aligned}$
> ale ${}b_{1},b_{2},\dots ,b_{n}{}$ jsou LN a tedy ${}\alpha_{1}-\beta_{1}=0,\alpha_{2}-\beta_{2}=0,\dots,\alpha_{n}-\beta_{n}=0{}$
> ${}\implies \alpha_{1}=\beta_{1} \land\alpha_{2}=\beta_{2}\land\dots \land\alpha_{n}=\beta_{n}{}$ a nemáme 2 různé ale jen jedno vyjádření 

> [!note] Definice 5.
>  Nechť ${}\mathcal{L}{}$ je nenulový, konečně generovaný lineární vektorový prostor, nechť ${}b_{1} , b_{2}, \dots, b_{n}{}$ je báze prostoru ${}\mathcal{L}{}$. Je-li ${}x \in \mathcal{L}{}$ libovolný prvek, potom jednoznačně určené koeficienty ${}\lambda_{1} , \lambda_{2}, \dots, \lambda_{n}{}$ v lineární kombinaci ${}x =\lambda_{1}b_{1} +\lambda_{2} b_{2}+\dots+\lambda_{n}b_{n}{}$ budeme nazývat **souřadnice** prvku ${}x{}$ v bázi ${}b_{1} , b_{2}, \dots, b_{n}{}$.
>  
>  Píšeme ${}\hat{x} = [\lambda_{1} , \lambda_{2} , \dots, \lambda_{n} ]^T {}$.

> [!quote] Věta 6.
>  Průnik libovolného neprázdného systému podprostorů lineárního vektorového prostoru ${}\mathcal{L}{}$ je podprostor prostoru ${}\mathcal{L}{}$.

> [!note] Definice 6.
>  Jestliže ${}U{}$ a ${}V{}$ jsou podprostory lineárního vektorového prostoru ${}\mathcal{L}{}$, potom ${}U + V{}$ označuje lineární obal množiny ${}U \cup V{}$, tj. ${}U + V =\langle U \cup V \rangle{}$.

> [!quote] Věta 7.
>  Nechť ${}U{}$ a ${}V{}$ jsou podprostory lineárního vektorového prostoru ${}\mathcal{L}{}$ konečné dimenze. Potom platí ${}\dim(U + V ) + \dim(U \cap V ) = \dim U + \dim V{}$ .

**Poznámka**:
Jestliže ${}U{}$ a ${}V{}$ jsou podprostory konečně generovaného lineárního vektorového prostoru ${}\mathcal{L}{}$ takové, že ${}U \cap V = 0{}$ a ${}U + V = \mathcal{L}{}$, potom se takový součet podprostorů nazývá **direktní** a píšeme ${}\mathcal{L} = U \oplus V{}$.


# Příklady: *Důležité*
1) ${}\mathbb{R}:{}$

$$
\begin{align}
\left . \begin{aligned}
e_{1}=[1,0,0]^T \\
e_{2}=[0,1,0]^T \\
e_{3}=[0,0,1]^T
\end{aligned} \right \} \text{ LN a generující} \to \text{báze }\mathbb{R}_{3} \text{ kanonická; standartní} \\ \\

x=[3,11,-7]^T=3e_{1}+11e_{2}-7e_{3}
\end{align}
$$

$$
\begin{align}
v_{1}=[3,4,1]^T \\
v_{2}=[1,1,2]^T \\
v_{3}=[2,1,-2]^T
\end{align}
$$

2) ${}\mathbb{R}_{n}{}$: kanonická báze ${}\mathbb{R}_{n}:\begin{aligned}e_{1}=[1,0,\dots 0]^T \\  e_{2}=[0,1,\dots,0]^T \\  \vdots \\  e_{n}=[0,0,\dots,1]^T\end{aligned}\implies \dim \mathbb{R}_{n}=n{}$
	!${}\implies{}$ tedy v ${}\mathbb{R}_{n}{}$
	- každých **méně než ${}n{}$** prvků není **generující**
	- každých **více než ${}n{}$** prvků jsou **LZ**
	- každých **${}n{}$ prvků** je báze ${}\mathbb{R}_{n}{}$, pokud jsou **LN**

3) ${}P_{2}{}$: kanonická bázé ${}P_{2}: \begin{aligned}p_{1}(x)=1 \\  p_{2}(x)=x \\  p_{3}(x)=x^{2}\end{aligned}\implies \dim P_{2}=3{}$   *(n+1)*

4) $$
   \begin{align}
   \mathbf{M}_{2,3}:& \mathbf{M}_1 =\begin{bmatrix}
1 & 0 & 0 \\
0 & 0 & 0
\end{bmatrix},\mathbf{M}_{2}=\begin{bmatrix}
0 & 1 & 0 \\
0 & 0 & 0
\end{bmatrix}, \dots,\mathbf{M}_{3}=\begin{bmatrix}
0 & 0 & 0 \\
0 & 0 & 1
\end{bmatrix}\dots \text{ kanonická báze }\mathbf{M}_{2,3} \\
&\implies \dim \mathbf{M}_{2,3}=6=2.3 \\
\text{obecně: }&\dim \mathbf{M}_{m,n}=m\cdot n
   \end{align}
   $$
