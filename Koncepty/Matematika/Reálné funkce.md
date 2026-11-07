---
type: concept
aliases:
status: todo
katedra: KMA
---

![[Přehled funkcí.pdf]]

# Reálné funkce jedné reálné proměnné
> [!note] Definice (Reálné funkce jedné reálné proměnné)
> Zobrazení ${}f:D\subset \mathbb{R\to \mathbb{R}}{}$ se nazývá **reálná funkce jedné reálné proměnné**:
> 
> $$
> \begin{gathered}
> f:D\subset \mathbb{R}\to \mathbb{R} \\ \\
> \hline \\
> x \in D\subset \mathbb{R} \to f(x)=y \in \mathbb{R}
> \end{gathered}
> $$
> ${}x{}$ se říká: vzor, nezávislá proměnná, vstup
> ${}y{}$ se říká: obraz, závislá proměnná, výstup
> 
> Zápis: 
> $$
> f:~~y=f(x),~ x \in D\subset \mathbb{R}
> $$

> [!example]
> $$
\begin{align}
& f_{1}:y=x+1,~ x \in \left< 0,1 \right>  \\
& f_{2}:y=x^{2}, ~ x \in \left( -\infty,0 \right>  \\
& f_{3}:y=\ln x, ~ x >0 \\
& f_{4}: y=\begin{cases}
0 & x \not\in \mathbb{Q} \\
1 & x \in \mathbb{Q}
\end{cases} \text{ Dirichletova}
\end{align}
> $$

**definiční obor** ${}D=D(f)=D_{f}=\{ x \in \mathbb{R} : ~~ \exists y\in \mathbb{R}:~~ y=f(x)\}{}$
- pokud není zadán, tak je implicitně nejširší množina na které vzorec dává smysl
**obor hodnot** #fixme

#fixme grafy

Restrikce funkce (zúžení)
Mějme funkci ${}f: D \subset \mathbb{R}\to \mathbb{R}{}$. ${}M \subsetneq D{}$ #fixme



Rovnost funkcí:
Funkce ${}f: D(f)\subset \mathbb{R}\to \mathbb{R}{}$ a ${}g:D(g)\subset \mathbb{R}\to \mathbb{R}{}$ **se rovnají**, píšeme ${}f=g{}$, pokud:
1. ${}D(f)=D(g){}$
2. ${}\forall x \in D(f)=D(g):~f(x)=g(x){}$

> [!example]-
> ${}f:y=1{}$
> ${}g:y=\frac{x}{x}{}$
> 
> ${}D(f)=\mathbb{R}\neq D(g)=\mathbb{R}\setminus \{ 0 \}{}$


> [!note] Definice (omezenost fce)
> ${}f:D\subset \mathbb{R}\to \mathbb{R},~~M\subset D{}$
> Řekneme, že funkce ${}f{}$ je:
> 1) **Omezená zdola na** ${}M{}$, pokud ${}\exists d\in \mathbb{R}~~\forall x \in M:~~~ d\leq f(x){}$
> 2) **Omezená zhora na** ${}M{}$, pokud ${}\exists h\in \mathbb{R}~~\forall x \in M:~~~ h \geq f(x){}$
> 3) **omezená na** ${}M{}$, pokud je na ${}M{}$ omezená zdola ${}\land{}$ omezená zdola
> 
> tj. #fixme 


> [!note] Definice (min / max / inf / sup)
> ${}f:D\subset \mathbb{R}\to \mathbb{R},~~M\subset D{}$. Potom
> 1) **maximum funkce ${}f{}$ na ${}M{}$**, je číslo ${}M=\max \{ f(x): x \in M \}{}$ (pokud existuje)
>    značíme : ${}\max_{x \in M}f(x){}$
> 2) **minimum funkce ${}f{}$ na ${}M{}$**, je číslo ${}m=\min \{ f(x): x \in M \}{}$ (pokud existuje)
>    značíme : ${}\min_{x \in M}f(x){}$
> 3) **suprémum funkce ${}f{}$ na ${}M{}$**, je číslo ${}s=\sup \{ f(x): x \in M \}{}$ (pokud existuje)
>    značíme : ${}\sup_{x \in M}f(x){}$
> 4) **infimum funkce ${}f{}$ na ${}M{}$**, je číslo ${}i=\inf \{ f(x): x \in M \}{}$ (pokud existuje)
>    značíme : ${}\inf_{x \in M}f(x){}$

> [!example]-
> # 1
> ${}f(x)=\sin x{}$, ${}D=\mathbb{R}{}$
> ${}\forall x \in \mathbb{R}: ~~ -1\leq \sin x\leq 1\implies d:=-1\land h:=1\implies{}$ ${}f{}$ omezená na ${}D=\mathbb{R}{}$
> ${}\sin \frac{\pi}{2}=1=h\implies \max_{x \in \mathbb{R}}(\sin x)=1=\sup_{x \in \mathbb{R}}(\sin x){}$
> ${}\sin -\frac{\pi}{2}=-1=d\implies \min_{x \in \mathbb{R}}(\sin x)=1=\inf_{x \in \mathbb{R}}(\sin x)> {}$
> 
> # 2
> ${}f(x)=e^x{}$
> ${}\forall x \in \mathbb{R}:~~~e^x>0=:d\implies f{}$ je omezená zdola
> 
> ${}f(x){}$ **není omezená zhora**
> ${}\overset{\text{def.}}{\Leftrightarrow}\forall h \in \mathbb{R}~\exists x \in \mathbb{R}: ~~~ e^x>h{}$
> Buď ${}h\in \mathbb{R}{}$ libovolné : ${}x_{h}>\ln h{}$
> ${}x_{h}:=\ln h+1>\ln h+1{}$
> 
> ${}\inf_{x \in \mathbb{R}}f(x)=\inf_{x \in \mathbb{R}}(e^x)=0{}$
> ${}\forall\epsilon>0 ~ \exists x_{\epsilon} \in \mathbb{R}: ~~~ 0+\epsilon>f(x_{\epsilon})=e^{x_{\epsilon}}{}$
> Buď ${}\epsilon>0{}$ libovolné : ${}x_{\epsilon}:=\ln\epsilon-1<\ln\epsilon{}$
> 
> ${}\nexists \min_{x \in \mathbb{R}}(e^x){}$ neboť  ${}\nexists x \in \mathbb{R}:~~~ e^x=0{}$


**Dohoda:** odsud dále předpokládáme, že ${}D{}$ obsahuje alespoň **2 různé** body

> [!note] Definice (monotónnost funkce)
> ${}f:D\subset \mathbb{R}\to \mathbb{R},~~M\subset D{}$. Řekneme, že:
> 1) ${}f{}$ je **ostře roustoucí na ${}M{}$**, pokud ${}\forall x_{1},x_{2} \in M:x_{1}<x_{2}\implies f(x_{1})<f(x_{2}){}$
> 2) ${}f{}$ je **ostře klesající na ${}M{}$**, pokud ${}\forall x_{1},x_{2} \in M:x_{1}<x_{2}\implies f(x_{1})>f(x_{2}){}$
> 3) ${}f{}$ je **roustoucí na ${}M{}$**, pokud ${}\forall x_{1},x_{2} \in M:x_{1}<x_{2}\implies f(x_{1})\leq f(x_{2}){}$
> 4) ${}f{}$ je **klesající na ${}M{}$**, pokud ${}\forall x_{1},x_{2} \in M:x_{1}<x_{2}\implies f(x_{1})\geq f(x_{2}){}$
> 
> 1 a 2 jsou ostře monotónní
> 3 a 4 jsou monotónní

> [!example]-
> # 1
> #fixme : od Augiho


> [!note] Definice (prostá funkce)
> ${}f:D\subset \mathbb{R}\to \mathbb{R},~~M\subset D{}$. Řekneme, že
> ${}f{}$ je **prostá na ${}M{}$**, pokud ${}\forall x_{1},x_{2} \in M: ~~~ x_{1}\neq x_{2}\implies f(x_{1})\neq f(x_{2}){}$

> [!example]-
> # 1
> ${}f(x)=\ln x{}$ je prostá na ${}(0,\infty){}$
> 
> # 2
> ${}f(x)=x^{2}{}$ není prostá na ${}\mathbb{R}{}$, ale je prostá na ${}\left< 0,+\infty \right){}$


> [!quote] Věta (monotonnost a prostost)
> ${}f:D\subset \mathbb{R}\to \mathbb{R},~~M\subset D{}$. Potom:
> ${}f{}$ je ostře monotónní na ${}M\implies f{}$ je prostá na ${}M{}$
> 
> > [!done]- Důkaz
> > Búno ${}f{}$ je ostře rostoucí na ${}M{}$:
> > 
> > $$
> > \forall x_{1},x_{2}\in M: ~~~ x_{1}<x_{2}\implies f(x_{1})<f(x_{2})
> > $$
> > chceme
> > $$
> > \forall x_{1},x_{2}\in M: ~~~ x_{1}\neq x_{2}\implies f(x_{1})\neq f(x_{2})
> > $$
> > potom #fixme
> > $$
> > x_{1}\neq x_{2}\implies x_{1}<x_{2}
> > $$


**Poznámka:**
${}\cancel{\impliedby}{}$ protipříklad : ${}f(x)=\frac{1}{x}{}$
je prostá na ${}\mathbb{R}\setminus \{ 0 \}{}$
ALE není monotónní na ${}\mathbb{R}\setminus \{ 0 \}{}$ ${}\impliedby f(-1)<f(1)\land f(1)>f(2){}$


> [!note] Definice (sudá / lichá funkce)
> ${}f:D\subset \mathbb{R}\to \mathbb{R},~~M\subset D{}$. Řekneme, že:
> 1) ${}f{}$ je **lichá**, pokud : 
> 	i) ${}\forall x \in D: ~~~ -x \in D{}$
> 	ii) ${}\forall x \in D: ~~~ f(x) =-f(-x){}$ 
> 2) ${}f{}$ je **sudá**, pokud : 
> 	i) ${}\forall x \in D: ~~~ -x \in D{}$
> 	ii) ${}\forall x \in D: ~~~ f(x) =f(-x){}$ 

> [!example]-
> # 1
> ${}f(x)=x^{2}{}$ - sudá
> 
> # 2
> ${}f(x)=x^{3}{}$ - lichá
> 
> # 3
> ${}f(x)=\ln x{}$ - není sudá ani lichá ${}\impliedby D=(0,\infty){}$


> [!note] Definice (periodická funkce)
> ${}f:D\subset \mathbb{R}\to \mathbb{R},~~M\subset D{}$. Řekneme, že ${}f{}$ je **periodická** pokud:
> ${}\exists T>0: ~~~ \forall x \in D{}$
> i) ${}x-T \in D \land x+T \in D{}$
> ii) ${}f(x)=f(x+T){}$

> [!example]-
> ${}f(x)=\sin x{}$
