---
handwriting-page-id: a30764ee-fc56-4fab-9bd8-2cd42026a084
type: concept
aliases:
status: todo
katedra: KMA
---

$\mathbb{N}=\{ 1,2,3,\dots \}$
${}\mathbb{N}_{0}=\mathbb{N}\cup \{ 0 \}{}$
$\mathbb{Z}=\{\dots, -3, -2, -1, 0, 1,2,3,\dots \}$
$\mathbb{Q}=\left\{  \frac{p}{q}:p\in\mathbb{Z} \land q\in\mathbb{N} \right\}$
$\mathbb{R}$

---
>[!quote] Definice (max/min)
>${}A\subset \mathbb{R}{}$. Řekneme, že:
>1) číslo ${}d \in \mathbb{R}{}$ je **minimem** množiny ${}A{}$, pokud:
>	1) ${}d\in A{}$
>	2) ${}\forall x\in A:d\leq x{}$
>2) číslo ${}h\in \mathbb{R}{}$ je **maximem** množiny ${}A{}$, pokud:
>	1) ${}h\in A{}$
>	2) ${}\forall x\in A:x\leq h{}$

>[!quote] Definice (sup/inf)
>${}\emptyset\neq A{}$ je omezená.  Řekneme, že:
>1) číslo ${}d\in \mathbb{R}{}$ je **infímem** množiny ${}A{}$, pokud:
>	1) ${}\forall x\in A:d\leq x{}$
>	2) ${}\forall\epsilon>0\exists x_{\epsilon}\in A:d+\epsilon>x_{\epsilon}{}$
>2) číslo ${}h\in \mathbb{R}{}$ je **suprémem** množiny ${}A{}$, pokud:
>	1) ${}\forall x\in A:x\leq h{}$
>	2) ${}\forall \epsilon>0\exists x_{\epsilon}\in A:x_{\epsilon}>h-\epsilon{}$

---
# omezenost:
>[!quote]
>${}A\subset \mathbb{R}{}$. Řekneme, že množina ${}A{}$ je:
>1) **Omezená zdola**, pokud ${}\exists d\in \mathbb{R}\forall x\in A:d\leq x{}$
>2) **Omezená zhore**, pokud ${}\exists h\in \mathbb{R}\forall x\in A:x\leq h{}$
>3) **Omezená**, pokud je omezená shora a zároveň zdola
>${}d{}$ je dolní závora, ${}h{}$ je horní závora

if inf(A) == $-\infty$ or sup(A) == $\infty$:
	neomezená
else:
	omezená

---
# mohutnost:
- konečná m. : $A=\{ 1,10,\pi \}$
- spočetná m. : $\mathbb{N},\mathbb{Z},\mathbb{Q}$
- nespočetná m. : $\mathbb{R}, \langle 1,5\rangle$

---

|                           A                            |      minA      |      maxA      | infA | supA |
| :----------------------------------------------------: | :------------: | :------------: | :--: | :--: |
|                ${}\langle 5,7\rangle{}$                |       5        |       7        |  5   |  7   |
|                   ${}(-2,e\rangle{}$                   | ${}\nexists{}$ |       e        |  -2  |  e   |
|                       $(-10,-8)$                       | ${}\nexists{}$ | ${}\nexists{}$ | -10  |  -8  |
| ${}\left\{  \frac{n+1}{n}:n\in \mathbb{N}  \right\}{}$ | ${}\nexists{}$ |       2        |  1   |  2   |

>[!note] Lemma
>Buď ${}\emptyset\neq A\subset \mathbb{R}{}$ omezená. Potom platí:
>1) ${}\exists minA\implies infA=minA{}$
>2) ${}\exists maxA\implies supA=maxA{}$

>[!note] Věta
>Buď ${}\emptyset\neq A\subset \mathbb{R}{}$ omezená. Potom existuje právě jedno ${}infA{}$ a právě jedno ${}supA{}$

>[!note] Lemma (základní vlastnosti inf/sup)
>Buďte ${}\emptyset\neq A\subset \mathbb{R}{}$ omezená,  ${}\emptyset\neq B\subset \mathbb{R}{}$ omezená. Potom platí:
>1) ${}infA\leq supA{}$
>2) ${}A\subset B\implies infB\leq infA\land supA\leq supB{}$

