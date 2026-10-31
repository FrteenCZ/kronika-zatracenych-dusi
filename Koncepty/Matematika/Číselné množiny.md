---
handwriting-page-id: a30764ee-fc56-4fab-9bd8-2cd42026a084
type: concept
aliases:
status: done
katedra: KMA
---
# Podmnožiny ${}\mathbb{R}{}$
- $\mathbb{N}=\{ 1,2,3,\dots \}$
- ${}\mathbb{N}_{0}=\mathbb{N}\cup \{ 0 \}{}$
- $\mathbb{Z}=\{\dots, -3, -2, -1, 0, 1,2,3,\dots \}$
- $\mathbb{Q}=\left\{  \frac{p}{q}:p\in\mathbb{Z} \land q\in\mathbb{N} \right\}$
- $\mathbb{R}$


---
# Omezenost
>[!note] Definice (omezenost podmnožiny ${}\mathbb{R}{}$)
>${}A\subset \mathbb{R}{}$. Řekneme, že množina ${}A{}$ je:
>1) **Omezená zdola**, pokud ${}\exists d\in \mathbb{R}~~~\forall x\in A:~~~d\leq x{}$
>2) **Omezená zhore**, pokud ${}\exists h\in \mathbb{R}~~~\forall x\in A:~~~x\leq h{}$
>3) **Omezená**, pokud ${}A{}$ je omezená zhora a zároveň zdola
>
>${}d{}$ je dolní závora, ${}h{}$ je horní závora

---

# min/inf max/sup
>[!note] Definice (max/min)
>${}A\subset \mathbb{R}{}$. Řekneme, že:
>1) číslo ${}d \in \mathbb{R}{}$ je **minimem** množiny ${}A{}$ (${}d=\min A{}$), pokud:
>	1) ${}d\in A{}$
>	2) ${}\forall x\in A:d\leq x{}$
>2) číslo ${}h\in \mathbb{R}{}$ je **maximem** množiny ${}A{}$ (${}h=\max A{}$), pokud:
>	1) ${}h\in A{}$
>	2) ${}\forall x\in A:x\leq h{}$

> [!example]-
> ${}A= \left< 2,3 \right){}$
> - ${}\min A = 2{}$
> - ${}\nexists\max A{}$ ↓
> 
> > [!done] Důkaz - sporem
> > ${}\exists\max A=h{}$
> > (1.) ${}h\in \left< 2,3 \right)\implies 2\leq h<3{}$
> > ${}\implies x_{h}=\frac{h+3}{2}\in \left< 2,3 \right){}$
> > ${}x_{h}>h\to{}$ spor s (2.)


>[!note] Definice (sup/inf)
>${}\emptyset\neq A{}$ je omezená.  Řekneme, že:
>1) číslo ${}d\in \mathbb{R}{}$ je **infímem** množiny ${}A{}$, pokud:
>	1) ${}\forall x\in A:d\leq x{}$
>	2) ${}\forall\epsilon>0~~~\exists x_{\epsilon}\in A:~~~d+\epsilon>x_{\epsilon}{}$
>2) číslo ${}h\in \mathbb{R}{}$ je **suprémem** množiny ${}A{}$, pokud:
>	1) ${}\forall x\in A:x\leq h{}$
>	2) ${}\forall \epsilon>0~~~\exists x_{\epsilon}\in A:~~~x_{\epsilon}>h-\epsilon{}$

> [!example]-
> ${}\inf A=\min A=2{}$
> ${}\sup A=3{}$
> 
> ---
> |                           A                            |      minA      |      maxA      | infA | supA |
> | :----------------------------------------------------: | :------------: | :------------: | :--: | :--: |
> |                ${}\langle 5,7\rangle{}$                |       5        |       7        |  5   |  7   |
> |                   ${}(-2,e\rangle{}$                   | ${}\nexists{}$ |       e        |  -2  |  e   |
> |                       $(-10,-8)$                       | ${}\nexists{}$ | ${}\nexists{}$ | -10  |  -8  |
> | ${}\left\{  \frac{n+1}{n}:n\in \mathbb{N}  \right\}{}$ | ${}\nexists{}$ |       2        |  1   |  2   |



> [!quote] Lemma
> Buď ${}\emptyset\neq A\subset \mathbb{R}{}$ omezená. Potom platí:
> 1) ${}\exists \min A\implies \inf A=\min A{}$
> 2) ${}\exists \max A\implies \sup A=\max A{}$
> 
> > [!done]- Důkaz
> > 1) 
> >    ${}d=\min A{}$
> >    (1.) ${}d\in A{}$ 
> >    (2.) ${}\forall x \in A:~~~d\leq x{}$ 
> >    
> >    ${}\inf A=d{}$    (1.) ✔️
> >    
> >    (2.) ${}\epsilon>0{}$ lib. ${}\exists x_{\epsilon}=d{}$
> >    ${}d+\epsilon>d=x_{\epsilon}{}$
> > 
> > 2) analogicky
   

> [!quote] Věta
> Buď ${}\emptyset\neq A\subset \mathbb{R}{}$ omezená. Potom existuje právě jedno ${}\inf A{}$ a právě jedno ${}\sup A{}$
> 
> > [!done]- Důkaz
> > ${}\exists h_{1}=\sup A, \exists h_{2}=\sup A,h_{1}<h_{2}{}$
> > ${}\epsilon:= \frac{h_{2}-h_{1}}{2}\implies\epsilon>0{}$
> > ${}x_{\epsilon}:=h_{2}-\epsilon{}$
> > ${}x_{\epsilon}\in A\land h_{1}<x_{\epsilon}\to{}$ spor s (2.)


>[!quote] Lemma (základní vlastnosti inf/sup)
>Buď ${}\emptyset\neq A\subset \mathbb{R}{}$ omezená,  ${}\emptyset\neq B\subset \mathbb{R}{}$ omezená. Potom platí:
>1) ${}\inf A\leq \sup A{}$
>2) ${}A\subset B\implies \inf B\leq \inf A\land \sup A\leq \sup B{}$
> 
> > [!done]- Důkaz
> > **1**
> > ${}A\neq \emptyset\implies \exists x \in A{}$
> > ${}\left . \begin{aligned}&(1) \inf \\  &(2) \sup\end{aligned}\right \}\implies\inf \leq x\leq\sup A{}$
> > ---
> > **2** (sporem)
> > ${}\inf B>\inf A{}$
> > ${}\epsilon:= \frac{\inf B-\inf A}{2}{}$
> > ${}\exists x_{\epsilon}\in A:~~~x_{\epsilon}<\inf A+\epsilon{}$
> > ${}\implies x_{\epsilon}\not\in B\to A{}$ není ${}\subset B{}$

---
# Mohutnost
- konečná m. : $A=\{ 1,10,\pi \}$
- spočetná m. : $\mathbb{N},\mathbb{Z},\mathbb{Q}$
- nespočetná m. : $\mathbb{R}, \langle 1,5\rangle$
