---
type: concept
aliases:
status: todo
katedra: KMA
---

> [!note] Definice (číselná řada)
> Nechť ${}(a_{n}){}$ je [[posloupnost]] reálných čísel. Symbol
> 
> $$
> \sum_{n=1}^{+\infty}a_{n}=a_{1}+a_{2}+a_{3}+\dots
> $$
> nazveme **nekonečnou číselnou řadu**.

> [!note] Definice (konvergence číselné řady)
> Buď ${}(a_{n}){}$ posloupnost. Řekneme, že nekonečná číselná řada ${}\sum_{n=1}^{+\infty}a_{n}{}$ **konverguje v ${}\mathbb{R}{}$**, pokud je konvergentní posloupnost číselných součtů ${}(s_{n}){}$, kde 
> $$
> s_n=\sum_{k=1}^n a_{k}=a_{1}+a_{2}+\dots+a_{n}
> $$
> 
> Pozn.: 
> $$
> \begin{align}
> s_{1}&=a_{1} \\
> s_{2}&=a_{1}+a_{2} \\
> s_{3}&=a_{1}+a_{2}+a_{3} \\
> &\vdots
> \end{align}
> $$
> 
> $$
> S\in \mathbb{R} \text{ součet řady }\sum_{n=1}^{+\infty}a_{n}=s
> $$
> Řada je divergentní, pokud není konvergentní


# Nezáporné řady

> [!note] Nezáporné řady
> 
> $$
> \sum_{n=1}^{\infty} a_{n}\text{ kde }a_{n}\geq 0~~\forall n\in \mathbb{N} ~~(\text{p.s.v.}n\in \mathbb{N})
> $$


 (\*) **Platí**: ${}\sum_{n=1}^{\infty}a_{n}{}$ konvergentní ${}\Leftrightarrow \sum_{n=1}^{\infty}a_{n_{0}+n}{}$ pro lib. pevné ${}n_{0}\in N{}$ je konvergentní (Součet může být jiný)

> [!quote] Věta (srovnávací kritérium)
> 
> $$
> 0\leq a_{n}\leq b_{n}~~p.s.v.~n\in \mathbb{N}
> $$
> ${}\implies{}$
> 1) ${}\sum_{n=1}^{\infty}b_{n}{}$ je konvergentní ${}\implies \sum_{n=1}^{\infty}a_{n}{}$ je konvergentní
> 2) ${}\sum_{n=1}^{\infty}a_{n}{}$ je divergentní ${}\implies \sum_{n=1}^{\infty}b_{n}{}$ je divergentní
> 
> > [!done]- Důkaz
> > **búno** (Bez újmy na obecnosti): ${}0\leq a_{n}\leq b_{n}~~~\forall n\in \mathbb{N}{}$
> > ${}s_{n}^a=\sum_{k=1}^{n}a_{n},~~s_{n}^b=\sum_{k=1}^{n}b_{n}{}$
> > (\*) ${}0\leq s_{n^a}=a_{1}+\dots+a_{n}\leq b_{1}+\dots+n_{b}=s_{n}^b{}$
> > 
> > Předpoklad. 1) ${}\sum_{n=1}^{\infty}b_{n}{}$ je konvergentní ${}\Leftrightarrow s_{n}^b\to s^b\in \mathbb{R}=\sup(s_{n}^b){}$ 
> > 
> > (\*) ${}\implies 0\leq s_{n}^a\leq s_{n}^b\leq\sup(s_{n}^b)=s^b{}$
> > ${}\implies \forall n \in \mathbb{N}:~~d\leq s_{n}^a\leq h\implies(s_{n}^a){}$ je omezená
> > 
> > ${}s_{n}^a=a_{1}+\dots+a_{n}\leq s_{n+1}^a=a_{1}+\dots+a_{n}+a_{n+1}, ~~a_{n+1}\geq 0{}$
> > ${}\implies \forall n\in \mathbb{N}: ~~s_{n}^a\leq s_{n+1}^a{}$
> > ${}\implies(s_{n}^a){}$ je rostoucí
> > 
> > ${}\implies s_{n}^a\to s^a\in \mathbb{R}\implies \sum_{n=1}^{\infty}a_{n}{}$ je konv.
> > 
> > **Navíc**: pokud vlastnost ${}\forall n \in \mathbb{N}:~~a_{n}\leq b_{n}\implies s^a \leq s^b{}$

> [!example]-
> $$
> \sum_{n=1}^{\infty} \frac{1}{\ln(n+1)}
> $$
> NPK .... ${}\lim_{ n \to \infty } \frac{1}{\ln(n+1)}=0 ~~ \checkmark{}$ 
> 
> ${}\frac{1}{\ln (n+1)}>0~~\forall n\in \mathbb{N}{}$
> 
> ${}0< \frac{1}{\ln(n+1)}\leq{}$ "něco, téhož řádu konverguje" ${}\times{}$
>     ${}\frac{1}{\ln(n+1)}\geq{}$ "něco, jehož řada diverguje" ${}\checkmark{}$
> 
> ${}\frac{1}{\ln(n+1)} > \frac{1}{n+1}{}$
> ${}\sum_{n=1}^{\infty} \frac{1}{n+1}=\sum_{n=2}^{\infty} \frac{1}{n}{}$ harmonická řada bez ${}a_{1}\implies{}$ div.
> 
> 
> ${}\forall n\in \mathbb{N}:~~ \frac{1}{\ln(n+1)}> \frac{1}{n+1}{}$
> ${}\sum_{n=1}^{\infty} \frac{1}{n+1}{}$ je divergentní ${}\implies \sum_{n=1}^{\infty}{}$ je divergentní
> 
> ---
> 
> 
> $$
> \sum_{n=1}^{\infty} \frac{1}{n^{2}}
> $$
> **Platí**: ${}a_{n}=\frac{1}{n^{2}}=\frac{1}{n\cdot n}\leq \frac{1}{n(n-1)}=b_{n}{}$ pro ${}n\geq2{}$ (${}n_{0}=1{}$)
> ${}a_{n}\leq b_{n}{}$ p.s.v. ${}n\in \mathbb{N}{}$  (pro ${}n_{0}=1{}$)
> 
> ${}\sum_{n=2}^{\infty} \frac{1}{n(n-1)}=\sum_{n=1}^{\infty}\left( \frac{1}{n-1}-\frac{1}{n} \right){}$
> ${}s_{n}=\left( 1-\frac{1}{2} \right)+\left( \frac{1}{2}-\frac{1}{3} \right)+\left( \frac{1}{3}-\frac{1}{4} \right)+\dots+\left( \frac{1}{n-2}-\frac{1}{n-1} \right)+\left( > \frac{1}{n-1}-\frac{1}{n} \right){}$
> ${}=1-\frac{1}{n}\to 1{}$
> ${}\implies(s_{n}){}$ je konv.
> ${}\implies \sum_{n=2}^{\infty} \frac{1}{n(n-1)}{}$ je konv.
> 
> ${}\sum_{n=2}^{\infty} b_{n}{}$ je konvergentní
> ${}\implies \sum_{n=1}^{\infty}a_{n}{}$ je konvergentní
>       ${}\sum_{n=1}^{\infty} \frac{1}{n^{2}}{}$


> [!quote] Věta (limitní srovnávací kritérium)
> Pokud ${}b_{n}>0{}$ p.s.v. ${}n\in \mathbb{N}{}$ a ${}\exists \lim_{ n \to \infty }\frac{a_{n}}{b_{n}}=L\in (0,\infty){}$
> ${}\implies \left( \sum_{n=1}^{\infty}a_{n} \text{ je konv. }\Leftrightarrow \sum_{n=1}^{\infty}b_{n} \text{ je konv. }\right){}$
>
> > [!done]- Důkaz
> > ${}\forall \epsilon>0: |\frac{a_{n}}{b_{n}}-L|<\epsilon{}$ p.s.v. ${}n\in \mathbb{N}{}$
> > ${}L-\epsilon< \frac{a_{n}}{b_{n}}<L+\epsilon{}$
> > Zvolíme ${}\epsilon:=\frac{L}{2}>0{}$   ${}\frac{L}{2}< \frac{a_{n}}{b_{n}}<\frac{3L}{2}{}$ p.s.v. ${}n\in \mathbb{N}{}$
> > 
> > ${}\frac{L}{2}b_{n}<a_{n}< \frac{3L}{2}b_{n}{}$
> > 
> > předp. ${}\sum_{n=1}^{\infty}a_{n}{}$ konvergentní ${}\implies \sum_{n=1}^{\infty}\frac{L}{2}b_{n}{}$ je konv. ${}\implies \sum_{n=1}^{\infty} b_{n}{}$ je konv.
> > předp. ${}\sum_{n=1}^{\infty}b_{n}{}$ konvergentní ${}\implies \sum_{n=1}^{\infty}\frac{3L}{2}b_{n}{}$ je konv. ${}\implies \sum_{n=1}^{\infty} a_{n}{}$ je konv.

> [!example]-
> 
> $$
> \sum_{n=1}^{\infty} \frac{n}{n^{2}+3} 
> $$
> 
> srovnam s ${}\sum_{n=1}^{\infty} \frac{1}{n}{}$
> ${}\lim_{ n \to \infty } \frac{a_{n}}{b_{n}} = \lim_{ n \to \infty } \frac{\frac{n}{n^{2}+3}}{\frac{1}{n}}=\lim_{ n \to \infty }\frac{n^{2}}{n^{2}+3}=1=L{}$


> [!quote] Věta (předopkladové kritérium - d'Alembertovo)
> Předp. ${}a_{n}>0{}$ p.s.v. ${}n\in \mathbb{N}{}$ Potom:
> 1) ${}\exists q\in(0,1):~~~ \frac{a_{n+1}}{a_{n}}\leq q{}$ p.s.v. ${}n\in \mathbb{N}\implies \sum_{n=1}^{\infty}a_{n}{}$ je konvergentní
> 2) ${}\frac{a_{n+1}}{a_{n}}\geq 1{}$ p.s.v. ${}n\in \mathbb{N}\implies \sum_{n=1}^{\infty}a_{n}{}$ je divergentní
> 
> > [!done]- Důkaz
> > 1) búno:   ${}\exists q\in(0,1)~~\forall n\in \mathbb{N}:~~~ \frac{a_{n+1}}{a_{n}}\leq q{}$
> >    ${}a_{n+1}\leq a_{n}\cdot q{}$
> >    ${}a_{2}\leq a_{1}q{}$
> >    ${}a_{3}\leq a_{2}q<a_{1}q^n{}$
> >    ${}\vdots{}$
> >    ${}a_{n}\leq a_{1}q^{n-1}{}$
> >    ${}\sum_{n=1}^{\infty}b_{n}=\sum_{n=1}^{\infty}a_{1}q^{n-1}{}$ geom řada s koeficientem ${}q<1\implies{}$ konv.
> >    ${}\implies \sum_{n=1}^{\infty}a_{n}{}$ konv.
> > 
> > 2) sporem
> > 
> > búno: ${}\forall n\in \mathbb{N}:~~\frac{a_{n+1}}{a_{n}}\geq 1 \land \sum_{n=1}^{\infty}a_{n}{}$ je konv.
> > ${}\implies a_{n+1}\geq a_{n}\implies a_{n}\geq a_{1}>0{}$
> > ${}\times{}$
> > ${}\overset{\text{NPK}}{\implies}\lim_{ n \to \infty }a_{n}=0{}$

> [!example]- 
> 
> $$
> \sum_{n=1}^{\infty}  \frac{2^n}{(n+1)!}
> $$
> NPK: ${}\lim_{ n \to \infty } \frac{2^n}{(n+1)!}=\lim_{ n \to \infty } \frac{2^n}{n!(n+1)}=0~\checkmark{}$
> 
> POD: ${}\frac{a_{n+1}}{a_{n}}= \frac{\frac{2^{n+1}}{(n+2)!}}{\frac{2^n}{(n+1)!}}=\frac{2}{n+2}\leq \frac{2}{1+3}=\frac{2}{3}=:q{}$
> ${}\implies \sum_{n=1}^{\infty} \frac{2^n}{(n+1)!}{}$ je konv.

> [!warning] Pozor
> ${}\frac{a_{n+1}}{a_{n}}<1{}$ .... ${}\sum_{n=1}^{\infty} \frac{1}{n}:{}$ div.
> ${}\frac{a_{n+1}}{a_{n}}=\frac{n}{n+1}<1{}$


> [!quote] Věta (limitní podílové kritérium)
> 
> **Předp.:** $a_n > 0$ p.s.v. $n \in \mathbb{N}$
> 
>   
> 
> $$\lim_{n \to \infty} \frac{a_{n+1}}{a_n} < 1 \implies \sum_{n=1}^{+\infty} a_n \text{ je konvergentní}$$
> 
> $$\lim_{n \to \infty} \frac{a_{n+1}}{a_n} > 1 \implies \sum_{n=1}^{+\infty} a_n \text{ je divergentní}$$
> 
> **Pozn.:**
> 
>   
> 
> $$\lim_{n \to \infty} \frac{a_{n+1}}{a_n} = 1 \implies ?$$
> 
> _(V případě rovnosti $1$ kritérium nedává žádnou informaci – řada může konvergovat i divergovat a je nutné použít jiné kritérium)._
>
> >[!done]- Důkaz
> >1) ${}\lim_{ n \to \infty } \frac{a_{n+1}}{a_{n}}=L<1{}$
> >   ${}\implies \forall\epsilon>0:| \frac{a_{n+1}}{a_{n}-L}|<\epsilon{}$ p.s.v. ${}n\in \mathbb{N}{}$
> >   ${}L-\epsilon< \frac{a_{n+1}}{a_{n}}<L+\epsilon=q<1{}$
> >   ${}\epsilon:=\frac{1-L}{2}{}$


> [!quote] Věta (odmocninové kritérium - Cauchyovo)
> ${}a_{n}>0{}$ p.s.v. ${}n\in \mathbb{N}{}$ Potom
> 1) ${}\exists q\in(0,1):~~\sqrt[n]{ a_{n} }\leq q{}$ p.s.v. ${}n\in \mathbb{N}{}$
>    ${}\implies \sum_{n=1}^{\infty}a_{n}{}$ konv.
> 2) ${}\sqrt[n]{ a_{n} }\geq 1{}$ p.s.v. ${}n\in \mathbb{N}{}$
>    ${}\implies \sum_{n=1}^{\infty}a_{n}{}$ div.
>
> > [!done]- Důkaz
> > $$
> > \begin{align}
> > \sqrt[n]{ a_{n} }&\leq q \text{ p.s.v. } n\in \mathbb{N} \\
> > a_{n}&\leq q^n \text{ p.s.v. } n\in \mathbb{N}
> > \end{align}
> > $$ 


> [!quote] Věta (limitní odmocninové kritérium)
> ${}a_{n}\geq 0{}$ p.s.v. ${}n\in \mathbb{N}{}$ Potom
> ${}a_{n}\geq 0{}$ p.s.v. ${}n \in \mathbb{N}{}$ Ptom
> 1) ${}\lim_{ n \to \infty }\sqrt[n]{ a_{n} }<1\implies \sum_{n=1}^{\infty}a_{n}{}$ konv.
> 2) ${}\lim_{ n \to \infty }\sqrt[n]{ a_{n} }>1\implies \sum_{n=1}^{\infty}a_{n}{}$ div.
> 
> **Poznámka**: ${}\lim_{ n \to \infty }\sqrt[n]{ a_{n} }=1\implies ?{}$ 
