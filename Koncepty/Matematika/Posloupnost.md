---
type: concept
aliases:
status: todo
katedra: KMA
---

> [!note] Definice
> Posloupnost reálných čísel je zobrazení
> 
> $$
> a:\mathbb{N}\to \mathbb{R}
> $$
> a definičním oborem je ${}D_{a}=\mathbb{N}{}$
> 
> *(zobrazení - funkce (input:* ${}\mathbb{N}{}$ *a output:* ${}\mathbb{R}{}$))
> 
> 
> $$
> \begin{gathered}
> a:1\to a(1)=a_{1} \\
> a:2\to a(2)=a_{2} \\
> a:3\to a(3)=a_{3} \\
> \vdots
> \end{gathered}
> $$
> 
> Zápis: 
> $$
> \begin{align}
> (a_n)^{+ \infty}_{n=1}. &  & (a_{n}),  &  & (a_{1},a_{2},a_{3},\dots)
> \end{align}
> $$

Graf: ${}(a_{n}){}$, kde ${}a_{n}=\frac{1}{n}{}$

#fixme : graf

${}H_{a}{}$ ..... obor hodnot ..... ${}H_{A}=\{ a\in \mathbb{R} : \exists n\in \mathbb{N}:a_{n}=a\}{}$


**Způsoby zadání**:
1) Vzorcem pro n-tý člen (funkční předpis)
	- ${}a_{n}=\frac{1}{n}{}$
	- ${}a_{n}=(-1)^n{}$
	- $a_{n}=\begin{cases} -\frac{1}{n} &&n-\text{liché} \\0 &&n-\text{sudé}\end{cases}$
2) Rekurentní
	- ${}a_{n+1}=a_{n}+1, a_{1}=1{}$
	- $\begin{align}	a_{n+2}=a_{n}+a_{n+1} \\	a_{1},a_{2} \text{ zadáno}	\end{align}$

> [!note] Definice (omezenost posloupnosti)
> Mějme posloupnost ${}(a_{n}){}$. Řekneme, že posloupnost ${}(a_{n}){}$ je :
> 1) **Omezená zdola**, pokud ${}\exists d\in \mathbb{R}\forall n\in \mathbb{N}:d\leq a_{n}{}$ (tzn. ${}H{}$ je množina omezená zdola)
> 2) **Omezená zhora**, pokud ${}\exists d\in \mathbb{R}\forall n\in \mathbb{N}:d\geq a_{n}{}$ (tzn. ${}H{}$ je množina omezená zhora)
> 3) **Omezená**, pokud je omezená shora ${}\land{}$ zdola

#fixme : příklady


> [!warning] Poznámka (absolutní hodnota)
> Buď ${}a\in \mathbb{R}{}$.
> Absolutní hodnota čísla ${}a\in \mathbb{R}{}$ je číslo:
> 
> $$
> |a|:=\begin{cases}
> a\text{ pro }a\geq 0 \\
> -a \text{ pro } a<0
> \end{cases}
> $$
>
> **Platí** 
> 1) ${}\forall a\in \mathbb{R}:\sqrt{ a^{2} }=|a|{}$
> > [!done]- Důkaz
> > - ${}a\geq 0:\sqrt{ a^{2} }=a{}$
> > - ${}a<0:\sqrt{ a^{2} }=-a{}$
> 2) (${}\Delta-\text{nerovnost}{}$) ${} \forall a,b\in \mathbb{R}:|a+b|\leq|a|+|b|{}$
> > [!done]- Důkaz
> > - ${}a^{2}+2ab+b^{2}\leq|a|^{2}+2|a||b|+|b|^{2}{}$
> > - ${}(a+b)^{2}\leq(|a|+|b|)^{2}{}$
> > - ${}|a+b|\leq||a|+|b||{}$

> [!quote] Lemma:
> Posloubnost ${}(a_{n}){}$ je omezená ${}\Leftrightarrow \exists c\geq 0~~\forall n\in \mathbb{N}:~~|a_{n}|\leq c{}$
>
> >[!done]- Důkaz
> ># ${}\implies{}$
> >${}|a_{n}|\leq c{}$
> >${}d:=-c\leq a_{n} \leq c =:h{}$
> >
> ># ${}\impliedby{}$
> >${}\exists d,h\in \mathbb{R}~~\forall n\in \mathbb{N}:~~c:= \max \{ |d|,|h| \}{}$


> [!example]-
> # 1
> $$
> \begin{align}
> a_{n}&=\frac{n}{n+1} \\
> d:=0&< \frac{n}{n+1} \\
>    \\
> \frac{n}{n+1}&\leq 1000 \\
> n&\leq1000(n+1) \\
> n&\leq 1000n+1000 \\
> -1000&\leq 999n \\
> -\frac{1000}{999}&\leq n & \forall n\in \mathbb{N}\implies(a_{n})\text{ je omezená shora}
> \end{align}
> $$
> 
> ---
> 
> # 2
> $$
> a_{n}=n^{2}+1
> $$
>    
> $$
> \begin{align}
> (a_{n})\text{ není omezená shora} &\Leftrightarrow \exists h\in \mathbb{R}\forall m\in > \mathbb{N}:a_{n}\leq h \\
> &\Leftrightarrow \forall h\in \mathbb{R}\exists n\in \mathbb{N}:a_{n}>h \\
> &\Leftrightarrow \forall h\in \mathbb{R}\exists n\in\mathbb{N}:n^{2}+1>h \\
> \end{align}
> $$
>    
> $$
> \begin{align}
> \text{Buď } h\in \mathbb{R}\text{ lib. dané} &: n^{2}+1>h \\
> &: n^{2}>h-1 \\
>    \\
> h<1:n=1 \\
> h\geq 1&:|n|>\sqrt{ h-1 } \\
> &:n>\sqrt{ h-1 } \\
>    \\
> [\sqrt{ h-1 }]+1=n&\implies n>\sqrt{ h-1 }\implies n^{2}+1>h
> \end{align}
> $$
   

# Min, max, inf, sup
> [!note] Definice
> Máme posloupnost ${}a_{n}{}$ a ${}H{}$ obor hodnot
> Definujeme:
> - ${}\mathrm{min}(a_{n})=\mathrm{min}(H){}$ 
> - ${}\mathrm{max}(a_{n})=\mathrm{max}(H){}$ 
> - ${}\mathrm{inf}(a_{n})=\mathrm{inf}(H){}$ 
> - ${}\mathrm{sup}(a_{n})=\mathrm{sup}(H){}$ 

#fixme : příklad

# Monotonie
> [!note] Definice (monotonie)
> Řekněme že posloupnost ${}(a_{n}){}$ je:
> 1) **rostoucí**, pokud ${}\forall n\in \mathbb{N}{}$ platí ${}a_{n}\leq a_{n+1}{}$
> 2) **klesající**, pokud ${}\forall n\in \mathbb{N}{}$ platí ${}a_{n}\geq a_{n+1}{}$
> 3) **ostře rostoucí**, pokud ${}\forall n\in \mathbb{N}{}$ platí ${}a_{n} < a_{n+1}{}$
> 4) **ostře klesající**, pokud ${}\forall n\in \mathbb{N}{}$ platí ${}a_{n} > a_{n+1}{}$

#fixme : příklady

> [!quote] Věta (omezenost vs monotonie)
> 1) ${}(a_{n}){}$ je rostoucí posloupnost ${}\implies(a_{n}){}$ je omezená zdola a ${}\min(a_{n})=a_{1}{}$
> 2) ${}(a_{n}){}$ je klesající posloupnost ${}\implies(a_{n}){}$ je omezená zhora a ${}\max(a_{n})=a_{1}{}$
> 
> > [!done]- Důkaz
> > 1) ${}(a_{n}){}$ je rostoucí ${}\implies{}$ ${}\forall n\in \mathbb{N}:~~~a_{n}\leq a_{n+1}{}$
> >    ${}\implies \forall n\in \mathbb{N}:~~d:=a_{1}\leq a_{n}\implies(a_{n}){}$ je omezená zdola a ${}\min(a_{n})=a_{1}{}$
> > 2) analogicky

---

> [!note] Definice (podposloupnost, vybrání podposloupnosti)
> Mějme ${}(a_{n}){}$ posloupnost. Buď ${}(k_{n}){}$ posloupnost taková, že
> 1) ${}(k_{n}){}$ je ostře rostoucí
> 2) ${}k_{n}\in \mathbb{N}~~\forall n\in \mathbb{N}{}$
> 
> Potom ${}(a_{k_{n}}){}$ nazýváme **podposloupnost** ${}(a_{n}){}$ 

#fixme : příklad

--- 
# Konvergence posloupnosti

![[Pasted image 20261010230946.png]]

> [!note] Definice (konvergence posloupnosti, limita)
> Mějme posloupnost (${}a_{n}{}$). Řekněme, že posloupnoust (${}a_{n}{}$) je **konvergentní**, pokud existuje číslo ${}a\in \mathbb{R}{}$ tzv. **limita posloupnosti** platí že:
> $$\forall\epsilon>0~~\exists n_{0}\in \mathbb{N}  ~~~ \forall n\in \mathbb{N}: ~~~ n>n_{0} \implies |a_{n}-a|<\epsilon$$
> ${}n_{0}{}$ - mezní index
> ${}|a_{n}-a|<\epsilon\implies a-\epsilon<a_{n}<a+\epsilon{}$

**Zápis**:
- ${}\lim_{ n \to \infty }a_{n}=a{}$
- ${}a_{n}\to a{}$ pro ${}n\to \infty{}$
- ${}a_{n}\xrightarrow{n\to \infty}a{}$
- ${}a_{n}\to a{}$

> [!example]-
> $\lim_{ n \to \infty } \frac{1}{n}=0$
> buď $\epsilon>0$ libovolné pevné
> chci ${}| \dfrac{1}{n}-0|<\epsilon{}$             použiji na něj ${}n_{0} \in \mathbb{N}{}$
> ${}\dfrac{1}{n}<\epsilon{}$  →  ${}\dfrac{1}{\epsilon}<n{}$
> 
> ![[Pasted image 20261011121038.png]]
> 
> ${}n_{0}:= \left[ \frac{1}{\epsilon} \right]+1=\left\lceil  \frac{1}{\epsilon}  \right\rceil{}$ 
> ${}\forall n\in \mathbb{N}:n> n_{0}\implies\left[ n>\cancel {n_{0}}> \frac{1}{\epsilon} \right]{}$

**Poznámka**:
1) ${}\lim_{ n \to \infty }a_{n}=a\implies{}$ pro libovolnou podposloupnost (${}a_{k_{n}}{}$) platí 
	$$	\lim_{ n \to \infty } a_{k_{n}}=a	$$	
	př.
	 (${}a_{n}{}$), kde ${}a_{n}=(-1)^n{}$
	![[Pasted image 20261011151014.png]]
	${}\lim_{ n \to \infty }(-1)^n=\nexists{}$
	- ${}\lim_{ k \to \infty }(-1)^{2k}=1{}$
	- ${}\lim_{ k \to \infty }(-1)^{2k-1}=-1{}$

2) $V (n)$ platí pro skoro všechna ${}n\in \mathbb{N}{}$ 
	 "p.s.v. ${}n\in \mathbb{N}{}$" ${}\Leftrightarrow \exists n_{0}\in\mathbb{N}~~\forall n\in \mathbb{N}: ~~~ n>n_{0}\implies V(n){}$ 
	 ${}\lim_{ n \to \infty }a_{n}=a\Leftrightarrow \forall\epsilon>0:|a_{n}-a|<\epsilon{}$ p.s.v. ${}n\in \mathbb{N}{}$


> [!quote] Věta (jednoznačnost limity)
> Každá konvergentní posloupnost má právě 1 limitu
> 
> > [!done]- Důkaz (sporem)
> > - ${}a_{n}\to a{}$
> > - ${}a_{n}\to b{}$
> > - ${}a<b{}$
> > ![[Pasted image 20261011152110.png]]
> > 
> > ${}\epsilon=\dfrac{b-a}{4}{}$
> > ${}a+\epsilon<b-\epsilon{}$
> > 
> > ${}{}$↯ ${}\forall n\in \mathbb{N}:n> \mathrm{max}\{ n_{0a},n_{0b} \}{}$
> > 	${}|a_{n}-a|<\epsilon \land|a_{n}-b|<\epsilon\implies{}$ ↯ nejde: ${}\epsilon{}$ pásy se nepřekrývají 


