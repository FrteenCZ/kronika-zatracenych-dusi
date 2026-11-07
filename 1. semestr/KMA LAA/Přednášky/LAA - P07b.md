---
type: lecture
status: todo
katedra: KMA
date: 05-11-2026
---

> **Téma:** MATICE PŘECHODU, SOUSTAVY LINEÁRNÍCH ROVNIC
> **Koncepty:** [[Matice]], [[Lineární zobrazení]]
> **Zdroj**: [[P07ab.pdf]] [[P07ab-vyplneny.pdf]] [[P08.pdf]]

# MATICE PŘECHODU

> [!note] Definice (matice přechodu)
> Jestliže ${}f_{1} , f_{2} , \dots, f_{n}{}$ je báze prostoru ${}\mathcal{U}{}$ a ${}g_{1}, g_{2} , \dots, g_{n}{}$ je také báze prostoru ${}\mathcal{U}{}$, pak pro libovolný prvek ${}x \in \mathcal{U}{}$ lze napsat jeho souřadnice v obou bázích.
> 
> $$
> \begin{align}
> & x = \lambda_{1}f_{1} + \lambda_{2} f_{2} + \dots + \lambda_{n}f_{n} , &  \hat{x} = [\lambda_{1} , \lambda_{2} , \dots, \lambda_{n}]^T \\ \\
> & x = \eta_{1}g_{1} + \eta_{2} g_{2} + \dots + \eta_{n}g_{n} , &  \tilde{x} = [\eta_{1} , \eta_{2} , \dots \eta_{n} ]^T .
> \end{align}
> $$
> 
> Buď ${}\mathbf{L}: \mathcal{U}\to\mathcal{U}{}$ identické zobrazení, ${}\mathbf{L}(x) = x{}$ pro každé ${}x \in \mathcal{U}{}$.
> 
> Označme ${}\mathbf{T}{}$ matici tohoto lineárního zobrazení, v bázi ${}g_{1}, g_{2} , \dots, g_{n}{}$ a v bázi ${}f_{1} , f_{2} , \dots, f_{n}{}$ prostoru ${}\mathcal{U}{}$.
> 
> 
> $$
> \mathbf{T} = [\widehat{\mathbf{L}(g_{1})} ~~ \widehat{\mathbf{L}(g_{2})} ~~  \dots ~~ \widehat{\mathbf{L}(g_{n})}] = [\hat{g_{1}} ~~ \hat{g_{2}} ~~ \dots \hat{g_{n}}] 
> $$
> 
> neboť ${}\mathbf{L}(x) = x{}$ pro každé ${}x \in \mathcal{U}{}$.
> 
> Pro každé ${}x \in \mathcal{U}{}$ platí ${}\mathbf{T}\tilde{x} = \widehat{\mathbf{L}(x)} = \hat{x}{}$ a matice ${}\mathbf{T}{}$ je regulární. Takto vytvořená matice ${}\mathbf{T}{}$ se nazývá **matice přechodu** od báze ${}f_{1}, f_{2} , \dots, f_{n}{}$ k bázi ${}g_{1} , g_{2} , \dots, g_{n}{}$ prostoru ${}\mathcal{U}{}$.


> [!quote] Věta 7. 
> Nechť ${}\mathcal{U}{}$ je lineární vektorový prostor dimenze ${}n{}$, nechť ${}f_{1} , f_{2} , \dots, f_{n} ,~ g_{1}, g_{2} , \dots, g_{n}{}$ jsou dvě báze prostoru ${}\mathcal{U}{}$. Pro libovolný prvek ${}x \in \mathcal{U}{}$ označme ${}\hat{x}{}$ souřadnice prvku ${}x{}$ v bázi ${}f_{1} , f_{2}, \dots, f_{n}{}$ a ${}\tilde{x}{}$ souřadnice prvku ${}x{}$ v bázi ${}g_{1}, g_{2} , \dots, g_{n}{}$. Označíme-li ${}\mathbf{T}{}$ matici přechodu od báze ${}f_{1} , f_{2} , \dots, f_{n}{}$ k bázi ${}g_{1} , g_{2}, \dots, g_{n}{}$, potom platí:
> 1. ${}\mathbf{T}{}$ je regulární matice,
> 2. ${}\mathbf{T} \tilde{x} = \hat{x}{}$ pro každé ${}x \in \mathcal{U}{}$,
> 3. ${}\mathbf{T}^{-1}{}$ je matice přechodu od báze ${}g_{1}, g_{2} , \dots, g_{n}{}$ k bázi ${}f_{1} , f_{2} , \dots, f_{n}{}$,
> 4. ${}T^{-1} \hat{x} = \tilde{x}{}$ pro každé ${}x \in \mathcal{U}{}$.
> 
> > [!done]- Důkaz
> > Důsledek konstrukce ${}\mathbf{T}{}$

> [!example]-
> # 1
> ${}P_{2}:{}$${}\begin{aligned}&u_{1}=x^{2} \\ &u_{2}=x \\ &u_{3}=1\end{aligned}{}$ báze ${}P_{2}{}$    ${}\begin{aligned}&b_{1}=x^{2}+x \\  &b_{2}=x+1 \\  &b_{3}=1\end{aligned} {}$ báze${}P_{2}{}$          ${}\begin{aligned}&p(x)=2x^{2}-x+3 \\  &\hat{p(x)}=[2,-1,3]^T \\  &\tilde{p(x)}=[2,-3,6]^T\end{aligned}{}$
> 
> 
> ${}\mathbf{T}{}$ ..... matice ${}\mathbf{T}{}$ zobrazení v bázi ${}b_{1},b_{2},b_{3}{}$ a bázi ${}u_{1},u_{2},u_{3}{}$
> matice přechodu od báze ${}u_{1},u_{2},u_{3}{}$ k bázi ${}b_{1},b_{2},b_{3}{}$
> 
> $$
> \mathbf{T}=\begin{bmatrix}
> \hat{b_{1}} & \hat{b_{2}} & \hat{b_{3}}
> \end{bmatrix}=\begin{bmatrix}
> 1 & 0 & 0 \\
> 1 & 1 & 0 \\
> 0 & 1 & 1
> \end{bmatrix}
> $$
> 
> $$
> \begin{align}
> & \hat{p(x)}=\mathbf{T} \cdot \tilde{p(x)} \\
> & \hat{p(x)}= \begin{bmatrix}
> 1 & 0 & 0 \\
> 1 & 1 & 0 \\
> 0 & 1 & 1
> \end{bmatrix} \cdot \begin{bmatrix}
> 2 \\
> -3 \\
> 6
> \end{bmatrix}=\begin{bmatrix}
> 2 \\
> -1 \\
> 3
> \end{bmatrix}
> \end{align}
> $$
> 
> ${}\mathbf{T}^{-1}{}$ ... matice indentity v bázi ${}u_{1},u_{2},u_{3}{}$ a bázi ${}b_{1},b_{2},b_{3}{}$
> matice přechodu od báze ${}b_{1},b_{2},b_{3}{}$ k bázi ${}u_{1},u_{2},u_{3}{}$
> 
> ${}\mathbf{T}^{-1}=\begin{bmatrix} \tilde{u_{1}} & \tilde{u_{2}} & \tilde{u_{3}}\end{bmatrix}{}$
> ${}k_{1}b_{1}+k_{2}b_{2}+k_{3}b_{3}=u_{1},u_{2},u_{3}{}$
> 
> $$
> \begin{bmatrix*}[ccc|ccc]
> 1 & 0 & 0 & 1 & 0 & 0 \\
> 1 & 1 & 0 & 0 & 1 & 0 \\
> 0 & 1 & 1 & 0 & 0 & 1
> \end{bmatrix*}\sim\begin{bmatrix*}[ccc|ccc]
> 1 & 0 & 0 & 1 & 0 & 0 \\
> 0 & 1 & 0 & -1 & 1 & 0 \\
> 0 & 0 & 1 & 1& -1 & 1
> \end{bmatrix*}
> $$
> 
> 
> $$
> \tilde{p(x)}=\mathbf{T}^{-1}\hat{p(x)}=\begin{bmatrix}
> 1 & 0 & 0 \\
> -1 & 1 & 0 \\
> 1 & -1 & 1
> \end{bmatrix} \cdot \begin{bmatrix}
> 2 \\
> -1 \\
> 3
> \end{bmatrix}=\begin{bmatrix}
> 2 \\
> -3 \\
> 6
> \end{bmatrix}
> $$


# SOUSTAVY LINEÁRNÍCH ROVNIC

> [!note] Definice 1. 
> Nechť je dána matice ${}\mathbf{A}{}$ typu ${}m/n{}$, ${}n{}$-členný aritmetický vektor ${}x = [x_{1} , x_{2}, \dots, x_{n} ]^T{}$ , ${}m{}$-členný aritmetický vektor ${}b = [b_{1} , b_{2} , \dots, b_{m} ]^T{}$.
> 
> Potom ${}\mathbf{A}x = b{}$ je **soustava ${}m{}$ lineárních rovnic o ${}n{}$ neznámých**.
> 
> Matice ${}\mathbf{A} = [a_{ij} ]{}$ se nazývá **matice soustavy**. Vektor ${}x = [x_{1} , x_{2} , \dots, x_{n} ]^T{}$ **vektor neznámých**. Vektor ${}b = [b_{1}, b_{2}, \dots, b_{m}]^T{}$ **vektor pravých stran**.
> 
> Matici ${}[\mathbf{A}|b]=\begin{bmatrix*}[cccc|c]a_{11} & a_{12} & \dots & a_{1n} & b_{1} \\  a_{21} & a_{22} & \dots & a_{2n} & b_{2} \\ \vdots & \vdots & \ddots & \vdots & \vdots  \\  a_{m1} & a_{m2} & \dots & a_{mn} & b_{m}\end{bmatrix*}{}$ nazýváme **rozšířená matice soustavy**.


> [!note] Definice 2. 
> Nechť ${}\mathbf{A}x = b{}$ je soustava ${}m{}$ lineárních rovnic o ${}n{}$ neznámých. Potom každý ${}n{}$-členný aritmetický vektor ${}x{}$, pro který platí ${}\mathbf{A}x = b{}$, nazýváme **řešení soustavy rovnic**.


> [!note] Definice 3. 
> Nechť ${}\mathbf{A}x = b{}$ je soustava rovnic.
> - Soustava se nazývá **homogenní**, jestliže ${}b = 0{}$.
> - Soustava se nazývá **nehomogenní**, jestliže ${}b \neq 0{}$.


> [!quote] Věta 1. 
> Nechť ${}\mathbf{A}x = 0{}$ je homogenní soustava lineárních rovnic, nechť matice soustavy ${}\mathbf{A}{}$ je typu ${}m/n{}$. Potom množina všech řešení homogenní soustavy rovnic je lineární vektorový prostor dimenze ${}n - \mathrm{h}(\mathbf{A}){}$.


> [!quote] Věta 2 (Frobeniova podmínka řešitelnosti). 
> Soustava lineárních rovnic ${}\mathbf{A}x = b{}$ má řešení právě tehdy, když ${}\mathrm{h}([\mathbf{A}|b]) = \mathrm{h}(\mathbf{A}){}$.


> [!quote] Věta 3.
> Nechť ${}v{}$ je řešení soustavy lineárních rovnic ${}\mathbf{A}x = b{}$. Potom ${}w{}$ je řešení soustavy rovnic ${}\mathbf{A}x = b{}$ právě tehdy, když ${}w = v + u{}$, kde ${}u{}$ je řešení homogenní soustavy rovnic ${}\mathbf{A}x = 0{}$.


> [!quote] Věta 4.
> Jestliže soustava lineárních rovnic ${}\mathbf{A}x = b{}$ má regulární matici ${}\mathbf{A}{}$, potom tato soustava má jediné řešení.


> [!quote] Věta 5 (Cramerovo pravidlo). 
> Nechť ${}\mathbf{A}x = b{}$ je soustava lineárních rovnic s regulární maticí ${}\mathbf{A}{}$ řádu ${}n{}$. Pro každé ${}i = 1, \dots, n{}$ označme ${}\mathbf{A}_{i}{}$ matici, která vznikne z matice ${}\mathbf{A}{}$ tím, že ${}i{}$-tý sloupec matice ${}\mathbf{A}{}$ nahradíme sloupcem ${}b{}$. Potom pro řešení soustavy rovnic ${}\mathbf{A}x = b{}$ platí ${}x = [x_{1} , x_{2} , \dots, x_{n}]^T{}$, kde pro každé ${}i = 1, \dots, n{}$ je ${}x_{i} = \dfrac{\det \mathbf{A}_{i}}{\det \mathbf{A}}{}$.
