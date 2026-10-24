---
type: lecture
status: todo
katedra: KMA
date: 22-10-2026
---

> **Téma:** INVERZNÍ MATICE
> **Koncepty:** [[Matice]]
> **Zdroj**: [[P05b.pdf]]


> [!note] Definice 1. 
> Jestliže ${}\mathbf{A}{}$ je čtvercová matice řádu ${}n{}$, potom čtvercová matice ${}\mathbf{A}^{-1}{}$ řádu ${}n{}$ se nazývá **inverzní matice** k matici ${}\mathbf{A}{}$, jestliže ${}\mathbf{A}\mathbf{A}^{-1}=\mathbf{A}^{-1}\mathbf{A}=\mathbf{I}{}$.

Pozn.:  ${}(\mathbf{A}^{-1})^{-1}=\mathbf{A}{}$

> [!quote] Věta 1. 
> Ke čtvercové matici existuje nejvýše jedna inverzní matice.
>
> > [!done]- Důkaz
> > ${}\mathbf{A}{}$ ... dvě inverzní ${}\mathbf{A}_{1},\mathbf{A}_{2}{}$ různé (${}\mathbf{A_{1}}\neq \mathbf{A}_{2}{}$)
> > ${}\mathbf{A}\mathbf{A}_{1}=\mathbf{A}_{1}\mathbf{A}=\mathbf{I}{}$
> > ${}\mathbf{A}\mathbf{A}_{2}=\mathbf{A}_{2}\mathbf{A}=\mathbf{I}{}$
> >
> > $$\mathbf{A}_{1}=\mathbf{A}_{1}\mathbf{I}=\mathbf{I}\mathbf{A}\mathbf{A}_{2}=\mathbf{I}\mathbf{A}_{2}=\mathbf{A}_{2}\implies \text{ nejsou různé, } \mathbf{A}_{1}=\mathbf{A}_{2}=\mathbf{A}^{-1}$$


> [!quote] Věta 2. 
> Nechť ${}\mathbf{A}{}$ je čtvercová matice řádu ${}n{}$. Potom k matici ${}\mathbf{A}{}$ existuje inverzní matice ${}\mathbf{A}^{-1}{}$ právě tehdy, když matice ${}\mathbf{A}{}$ je regulární.
> 
> > [!done]- Důkaz
> > - ${}\implies{}$
> >   
> >  $$
> >  \begin{align}
> >  \exists \mathbf{A}^{-1}~~~\mathbf{A}^{-1}\mathbf{A}=\mathbf{A}\mathbf{A}^{-1}=\mathbf{I}\implies \mathrm{h}(\mathbf{I})=n=h(\mathbf{A}\mathbf{A}^{-1})\leq \min \{ \mathrm{h}(\mathbf{A}),\mathrm{h}(\mathbf{A}^{-1}) \}\leq n\implies \\
> >  \implies \mathrm{h}(\mathbf{A})=n\implies \mathbf{A} \text{ je regulární}
> >  \end{align}
> >  $$
> > - ${}\impliedby \mathbf{A}{}$ je regulární - existují řádkové úpravy, tedy existují elem. řádkové matice, které ${}\mathbf{A}{}$ převedou na ${}\mathbf{I}{}$.
> >
> >$$
> >   \begin{align}
> >  \mathbf{T}_{k}\dotsb \mathbf{T}_{2}\mathbf{T}_{1}\mathbf{A}=\mathbf{I} \\
> >  \mathbf{T}_{k}\dotsb \mathbf{T}_{2}\mathbf{T}_{1} = \mathbf{T}
> >  \end{align}
> >  $$
>  >  stejně přes sloupcové úpravy
>  >
> >  $$
> >   \begin{align}
> >   \mathbf{A}\mathbf{T}_{1}'\mathbf{T}_{2}'\dotsb \mathbf{T}_{k}'=\mathbf{I} \\
> >   \mathbf{T}_{1}'\mathbf{T}_{2}'\dotsb \mathbf{T}_{k}'=\mathbf{T}'
> >  \end{align}
> >  $$
>  > 
>  > $$
> >  \mathbf{T}=\mathbf{T}\mathbf{I}=\mathbf{T}\mathbf{A}\mathbf{T}'=\mathbf{I}\mathbf{T}'=\mathbf{T}'\implies \mathbf{T}'=\mathbf{T} \text{ a platí } \mathbf{T}\mathbf{A}=\mathbf{I}\land \mathbf{A}\mathbf{T}=\mathbf{I}\implies \mathbf{T}=\mathbf{A}^{-1}
> >  $$

**Užití**
Jestliže ${}\mathbf{A}{}$ je regulární matice, potom ty řádkové elementární úpravy, které převedou matici ${}\mathbf{A}{}$ na matici jednotkovou, ty stejné řádkové elementární úpravy převedou matici jednotkovou na matici ${}\mathbf{A}^{-1}{}$.

Zapíšeme-li vedle sebe matici ${}\mathbf{A}{}$ a jednotkovou matici ${}\mathbf{I}{}$, a budeme-li provádět na obě matice stejné řádkové elementární úpravy tak dlouho, až z matice ${}\mathbf{A}{}$ vznikne matice jednotková, potom z jednotkové matice ${}\mathbf{I}{}$ musíme získat matici ${}\mathbf{A}^{-1}{}$. Symbolicky zapsáno
$$
[\mathbf{A}|\mathbf{I}]\sim\dots \sim[\mathbf{I}|\mathbf{A}^{-1}].
$$

**Důsledek 3.** 
Ke každé elementární matici existuje inverzní matice a je to opět elementární matice.

Nyní lze dokázat větu:
> [!quote] Věta 4. 
> Nechť ${}\mathbf{A}{}$, ${}\mathbf{B}{}$ jsou matice řádu ${}n{}$. Potom
> 
> $$
> \det \mathbf{AB} = \det \mathbf{A} \cdot \det \mathbf{B}.
> $$
> > [!done]- Důkaz
> Zřejmý pomocí poznámky u hodnosti matice





> [!note] Definice 2.
> Ke čtvercové matici ${}\mathbf{A}{}$ řádu ${}n{}$ se matice ${}\mathbf{A}^A{}$, kterou vytvoříme tím, že transponovaně skládáme algebraické doplňky matice ${}\mathbf{A}{}$, nazývá **matice adjungovaná** k matici ${}\mathbf{A}{}$. → *Transponovaná matice algebraických doplňků k místům matice ${}\mathbf{A}{}$*
> 
> $$
> \mathbf{A}^A=\begin{bmatrix}
> A_{11} & A_{21} & \dots & A_{n1} \\
> A_{12} & A_{22} & \dots & A_{n2} \\
> \vdots  & \vdots  & \ddots  & \vdots \\
> A_{1n} & A_{2n}  &  \dots  & A_{nn}
> \end{bmatrix}
> $$

> [!quote] Věta 5. 
> Je-li čtvercová matice ${}\mathbf{A}{}$ řádu ${}n{}$ regulární, potom ${}\mathbf{A}^{-1}=\frac{1}{\det \mathbf{A}}\mathbf{A}^{\mathbf{A}}{}$
>
> > [!done]- Důkaz
> > 
> > $$
\begin{align}
> > \mathbf{A}\mathbf{A}^{\mathbf{A}}=\begin{bmatrix}
> > a_{11} & \dots & a_{1n} \\
> > \vdots & \ddots  & \vdots \\
> > a_{n_{1}}  & \dots  & a_{nn}
> > \end{bmatrix}\cdot \begin{bmatrix}
> > A_{11} & A_{21} & \dots & A_{n1} \\
> > A_{12} & A_{22} & \dots & A_{n2} \\
> > \vdots  & \vdots  & \ddots  & \vdots \\
> > A_{1n} & A_{2n}  &  \dots  & A_{nn}
> > \end{bmatrix} = \begin{bmatrix}
> > \det \mathbf{A} & 0 & \dots & 0 \\
> > 0 & \det \mathbf{A} & \dots & 0 \\
> > \vdots \\
> > 0 & 0 & \dots & \det \mathbf{A}
> > \end{bmatrix}= \\
> > =  \mathrm{diag}(\det \mathbf{A}, \det \mathbf{A}, \dots, \det \mathbf{A})=\det \mathbf{A}\mathbf{I}
\end{align}
> > $$
> > 
> > $$
> > \begin{align}
> > b_{11}=a_{11}\cdot \mathbf{A}_{11}+a_{12}\cdot \mathbf{A}_{12}+\dots+a_{1n}\cdot \mathbf{A}_{1n}=\det \mathbf{A} \text{ rozvoj determinantu podle 1. řádku}\\
> > b_{12}=a_{11}\cdot \mathbf{A}_{21}+a_{12}\mathbf{A}_{22}+\dots+a_{1n}\mathbf{A}_{1n}=\begin{vmatrix}
> > a_{11} & a_{12} & \dots & a_{1n} \\
> > a_{11} & a_{12} & \dots & a_{1n} \\
> > \vdots \\
> > a_{n_{1}} & a_{n2} & \dots & a_{nn}
> > \end{vmatrix}=0
> > \end{align}
> > $$
> > 
> > 
> > $$
> > \mathbf{I}=\frac{1}{\det \mathbf{A}}\cdot \mathbf{A}\cdot \mathbf{A}^\mathbf{A}=\mathbf{A}\cdot \frac{1}{\det \mathbf{A}}\cdot \mathbf{A}^A
> > $$


# Příklady
$$
\mathbf{A}=\begin{bmatrix}
3 & 5 \\
4 & 1
\end{bmatrix}
$$
I) 
$$
\begin{align}
\begin{bmatrix*}[cc|cc]
3 & 5 & 1 & 0 \\
4 & 1 & 0 & 1
\end{bmatrix*}\sim \begin{bmatrix*}[cc|cc]
-1 & 4 & 1 & -1 \\
4 & 1 & 0 & 1
\end{bmatrix*}\sim \begin{bmatrix*}[cc|cc]
-1 & 4 & 1 & -1 \\
0 & 17 & 4 & -3
\end{bmatrix*}\sim \begin{bmatrix*}[cc|cc]
1 & -4 & -1 & 1 \\
0 & 1 & \frac{4}{17} & -\frac{3}{17}
\end{bmatrix*}\sim \\
\sim \begin{bmatrix*}[cc|cc]
1 & 0 & -\frac{1}{17} & \frac{5}{17} \\
0 & 1 & \frac{4}{17} & -\frac{3}{17}
\end{bmatrix*}\dotsb \mathbf{A}^{-1}=\frac{1}{17}\begin{bmatrix}
-1 & 5 \\
4 & -3
\end{bmatrix}
\end{align}
$$
II)
$$
\mathbf{A}^{-1}=\frac{1}{-17}\begin{bmatrix}
1 & -5 \\
-4 & 3
\end{bmatrix}
$$

---


$$
\mathbf{A}=\begin{bmatrix}
1 & 2 & -3 \\
-2 & -3 & 8 \\
1 & 3 & 0
\end{bmatrix}
$$
I)
$$
\begin{align}
\begin{bmatrix*}[ccc|ccc]
1 & 2 & -3 & 1 & 0 & 0 \\
-2 & -3 & 8 & 0 & 1 & 0 \\
1 & 3 & 0 & 0 & 0 & 1
\end{bmatrix*}\sim\begin{bmatrix*}[ccc|ccc]
1 & 3 & 0 & 0 & 0 & 1 \\
0 & -1 & -3 & 1 & 0 & -1 \\
0 & 3 & 8 & 0 & 1 & 2 \\
\end{bmatrix*}\sim\begin{bmatrix*}[ccc|ccc]
1 & 3 & 0 & 0 & 0 & 1 \\
0 & -1 & -3 & 1 & 0 & -1 \\
0 & 0 & -1 & 3 & 1 & -1 \\
\end{bmatrix*}\sim \\
\sim\begin{bmatrix*}[ccc|ccc]
1 & 0 & 0 & -24 & -9 & 7 \\
0 & -1 & 0 & -8 & -3 & 2 \\
0 & 0 & -1 & 3 & 1 & -1 \\
\end{bmatrix*}\sim\begin{bmatrix*}[ccc|ccc]
1 & 0 & 0 & -24 & -9 & 7 \\
0 & 1 & 0 & 8 & 3 & -2 \\
0 & 0 & 1 & -3 & -1 & 1 \\
\end{bmatrix*}\implies \mathbf{A}^{-1}=\begin{bmatrix}
-24 & -9 & 7 \\
8 & 3 & -2 \\
-3 & -1 & 1
\end{bmatrix}
\end{align}
$$

II)
$$
\mathbf{A}^{-1}=\frac{1}{1}\begin{bmatrix}
-24 & 8 & -3 \\
-9 & 3 & -1 \\
7 & -2 & 1
\end{bmatrix}^T=\begin{bmatrix}
-24 & -9 & 7 \\
8 & 3 & -2 \\
-3 & -1 & 1
\end{bmatrix}
$$
