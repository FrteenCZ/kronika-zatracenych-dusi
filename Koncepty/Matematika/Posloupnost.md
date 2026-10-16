---
type: concept
aliases:
status: todo
katedra: KMA
---
# Min, max, inf, sup
> [!note] Definice
> Máme posloupnost ${}a_{n}{}$ a ${}H{}$ obor hodnot
> Definujeme:
> - ${}\mathrm{min}(a_{n})=\mathrm{min}(H){}$ 
> - ${}\mathrm{max}(a_{n})=\mathrm{max}(H){}$ 
> - ${}\mathrm{inf}(a_{n})=\mathrm{inf}(H){}$ 
> - ${}\mathrm{sup}(a_{n})=\mathrm{sup}(H){}$ 


# Konvergence
![[Pasted image 20261010230946.png]]

> [!note] Definice (konvergence posloupnosti, limita)
> Mějme posloupnost (${}a_{n}{}$). Řekněme, že posloupnoust (${}a_{n}{}$) je **konvergentní**, pokud existuje číslo ${}a\in \mathbb{R}{}$ tzv. **limita posloupnosti** platí že:
> $$\forall\epsilon>0~\exists n_{0}\in \mathbb{N}  ~~~~~~~~~~ \forall n\in \mathbb{N}:n>n_{0} \implies |a_{n}-a|<\epsilon$$
> ${}n_{0}{}$ - mezní index
> ${}|a_{n}-a|<\epsilon\implies a-\epsilon<a_{n}<a+\epsilon{}$

**Zápis**:
- ${}\lim_{ n \to \infty }=a{}$
- ${}a_{n}\to a{}$ pro ${}n\to \infty{}$
- ${}a_{n}\xrightarrow{n\to \infty}a{}$
- ${}a_{n}\to a{}$

**Příklad**:
$\lim_{ n \to \infty } \frac{1}{n}=0$
buď $\epsilon>0$ libovolné pevné
chci ${}| \dfrac{1}{n}-0|<\epsilon{}$             použiji na něj ${}n_{0} \in \mathbb{N}{}$
${}\dfrac{1}{n}<\epsilon{}$  →  ${}\dfrac{1}{\epsilon}<n{}$

![[Pasted image 20261011121038.png]]

${}n_{0}:= \left[ \frac{1}{\epsilon} \right]+1=\left\lceil  \frac{1}{\epsilon}  \right\rceil{}$ 
${}\forall n\in \mathbb{N}:n> n_{0}\implies\left[ n>\cancel {n_{0}}> \frac{1}{\epsilon} \right]{}$

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
	 "p.s.v. ${}n\in \mathbb{N}{}$" ${}\Leftrightarrow \exists n_{0}\in\mathbb{N}\forall n\in \mathbb{N}:n>n_{0}\implies V(n){}$ 
	 ${}\lim_{ n \to \infty }a_{n}=a\Leftrightarrow \forall\epsilon>0:|a_{n}-a|<\epsilon{}$ p.s.v. ${}n\in \mathbb{N}{}$


> [!quote] Věta (jednoznačnost limity)
> Každá konvergentní posloupnost má právě 1 limitu

**Dk**.: (sporem)
- ${}a_{n}\to a{}$
- ${}a_{n}\to b{}$
- ${}a<b{}$
![[Pasted image 20261011152110.png]]

${}\epsilon=\dfrac{b-a}{4}{}$
${}a+\epsilon<b-\epsilon{}$

${}{}$↯ ${}\forall n\in \mathbb{N}:n> \mathrm{max}\{ n_{0a},n_{0b} \}{}$
	${}|a_{n}-a|<\epsilon \land|a_{n}-b|<\epsilon\implies{}$ ↯ nejde: ${}\epsilon{}$ pásy se nepřekrývají 


