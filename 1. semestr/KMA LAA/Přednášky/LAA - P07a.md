---
type: lecture
status: todo
katedra: KMA
date: 04-11-2026
---

> **Téma:** MATICE LINEÁRNÍHO ZOBRAZENÍ
> **Koncepty:** [[Matice]], [[Lineární zobrazení]]
> **Zdroje**: [[P07ab.pdf]] [[P07ab-vyplneny.pdf]]

# MATICE LINEÁRNÍHO ZOBRAZENÍ
→ maticový popis lineárního zobrazení

> [!note] Definice (matice zobrazení)
> Nechť  ${}\mathbf{L}: \mathcal{U}\to \mathcal{V}{}$ je lineární zobrazení.
> Buď ${}u_{1} , u_{2} , \dots, u_{k}{}$ báze prostoru ${}\mathcal{U}, \dim \mathcal{U} = k{}$,
> ${}v_{1}, v_{2} , \dots, v_{n}{}$ báze prostoru ${}\mathcal{V}, \dim \mathcal{V} = n{}$.
> 
> Pro libovolný prvek ${}x \in  \mathcal{U}{}$ je ${}y = \mathbf{L}(x){}$, kde ${}y \in \mathcal{V}{}$. Vyjádříme ${}x = \lambda_{1}u_{1} +\lambda_{2} u_{2} +\dots +\lambda_{K} u_{k},~ \hat{x} = [\lambda_{1} , \lambda_{2} , \dots, \lambda_{k} ]^T{}$    ${}y = \eta_{1}v_{1} + \eta_{2}v_{2} + \dots + \eta_{n} v_{n},~ \hat{y} = [\eta_{1} , \eta_{2} , \dots, \eta_{n} ]^T {}$.
> 
> ${}y = \mathbf{L}(x) = \mathbf{L}(\lambda_{1} u_{1} + \lambda_{2} u_{2} + \dots + \lambda_{k} u_{k} ) = \lambda_{1}\mathbf{L}(u_{1} ) + \lambda_{2}\mathbf{L}(u_{2} ) + \dots + \lambda_{k} \mathbf{L}(u_{k} ){}$
> ${}\hat{y} = \lambda_{1} \widehat{\mathbf{L}(u_{1})} + \lambda_{2}\widehat{\mathbf{L}(u_{2})} + \dots + \lambda_{k} \widehat{\mathbf{L}(u_{k})}{}$.
> 
> Označme pro ${}\forall  i = 1, \dots, k ~~~ \widehat{\mathbf{L}(u_{i})} = [ \alpha_{1i} , \alpha_{2i} , \dots, \alpha_{ni}]^T{}$, kde ${} \mathbf{L}(u_{i}) = \alpha_{1i} v_{1} +\alpha_{2i}v_{2} +\dots+\alpha_{ni}v_{n} {}$.
> 
> $$
> \begin{gathered}
> \widehat{\mathbf{L}(x)}=\hat{y}=\begin{bmatrix}
> \eta_{1} \\
> \eta_{2} \\
> \vdots \\
> \eta_{n}
> \end{bmatrix}=\lambda_{1}\begin{bmatrix}
> \alpha_{11} \\
> \alpha_{21} \\
> \vdots \\
> \alpha_{n1}
> \end{bmatrix}+\lambda_{2}\begin{bmatrix}
> \alpha_{12} \\
> \alpha_{22} \\
> \vdots \\
> \alpha_{n2}
> \end{bmatrix}+\dots+\lambda_{k}\begin{bmatrix}
> \alpha_{1k} \\
> \alpha_{2k} \\
> \vdots \\
> \alpha_{nk}
> \end{bmatrix}=\begin{bmatrix}
> \alpha_{11} & \alpha_{12} & \dots & \alpha_{1k} \\
> \alpha_{21} & \alpha_{22} & \dots & \alpha_{2k} \\
> \vdots & \vdots & \ddots & \vdots \\
> \alpha_{n1} & \alpha_{n2} & \dots & \alpha_{nk}
> \end{bmatrix} \begin{bmatrix}
> \lambda_{1} \\
> \lambda_{2} \\
> \vdots \\
> \lambda_{k}
> \end{bmatrix}= \\ \\
> =\mathbf{A}\hat{x}
> \end{gathered}
> $$
> 
> Matice ${}\mathbf{A}{}$ se nazývá **matice lineárního zobrazení** ${}\mathbf{L}{}$ v bázích ${}u_{1}, u_{2} , \dots, u_{k}{}$ prostoru ${}\mathcal{U}{}$ a ${}v_{1}, v_{2}, \dots, v_{n}{}$ prostoru ${}\mathcal{V}{}$.
> 
> ${}\mathbf{A} = \left[ \widehat{\mathbf{L}(u1)} ~~ \widehat{\mathbf{L}(u2)} ~~ \dots ~~ \widehat{\mathbf{L}(uk)} \right], ~~ \mathbf{A}\hat{x} = \hat{y}{}$ , pro každé ${}x \in \mathcal{U}, ~~ \mathbf{L}(x) = y{}$.

> [!quote] Věta 1. 
> Nechť ${}\mathcal{U}, \mathcal{V}{}$ jsou lineární vektorové prostory konečné dimenze, nechť ${}\mathbf{L}: \mathcal{U}\to\mathcal{V}{}$ je lineární zobrazení, nechť ${}u_{1} , u_{2} , \dots, u_{k}{}$ je báze prostoru ${}\mathcal{U}{}$, tedy ${}\dim \mathcal{U} = k{}$, nechť ${}v_{1} , v_{2} , \dots, v_{n}{}$ je báze prostoru ${}\mathcal{V}{}$, tedy ${}\dim \mathcal{V} = n{}$. Utvořme právě popsaným způsobem matici lineárního zobrazení ${}\mathbf{A}{}$ typu ${}n/k{}$, t.j. ${}\mathbf{A} = \left[ \widehat{\mathbf{L}(u_{1})} ~~ \widehat{\mathbf{L}(u_{2} )} ~~ \dots ~~ \widehat{\mathbf{L}(u_{k} )} \right]{}$. Potom pro každé ${}x \in \mathcal{U}{}$ takové, že ${}\mathbf{L}(x) = y{}$, je ${}\mathbf{A}\hat{x} = \hat{y} {}$.
> 
> > [!done]- Důkaz
> > Výše uvedená konstrukce

>[!example]
>${}\mathbf{A}{}$ ... matice lineárního zobrazení v kanonických bázích ${}P_{2}{}$ a ${}\mathbb{R}_{2}{}$ (${}\{ x^{2},x,1 \}{}$, ${}\{ [1,0]^T,[0,1]^T \}{}$)
>
>
> $$
\begin{align}
& \mathbf{A}=[\widehat{\mathbf{L(x^{2})}} ~~ \widehat{\mathbf{L}(x)} ~~ \widehat{\mathbf{L}(1)}] \\
& \mathbf{L}(x^{2})=[1,0]^T \implies \widehat{\mathbf{L}(x^{2})}=[1,0]^T  \\
& \mathbf{L}(x)=[2,1]^T \implies\widehat{\mathbf{L}(x)}=[2,1]^T \\
& \mathbf{L}(x)=[0,3]^T \implies \widehat{\mathbf{L}(x)}=[0,3]^T \\
 \\
& \mathbf{A}=\begin{bmatrix}
1 & 2 & 0 \\
0 & 1 & 3
\end{bmatrix} \\
 \\
& p(x)=2x^{2}-x+3\implies \hat{p(x)}=[2,-1,3]^T \\
 \\
& \widehat{\mathbf{L}(p(x))}=\mathbf{A}\cdot \hat{p(x)} \\
& \widehat{\mathbf{L}(p(x))}=\begin{bmatrix}
1 & 2 & 0 \\
0 & 1 & 3
\end{bmatrix}\cdot \begin{bmatrix}
2 \\
-1 \\
3
\end{bmatrix}=\begin{bmatrix}
0 \\
8
\end{bmatrix}=\mathbf{L}(p(x))\to \text{ protože máme }\mathbb{R}_{2} \text{ a kononickou bázi}
\end{align}
> $$


> [!quote] Věta 2. 
> Nechť ${}\mathcal{U}, \mathcal{V}{}$ jsou lineární vektorové prostory, nechť ${}\mathbf{L}: \mathcal{U}\to\mathcal{V}{}$ je lineární zobrazení. Jestliže báze prostoru ${}\mathcal{U}{}$ je ${}u_{1} , u_{2} , \dots, u_{k}{}$, báze prostoru ${}\mathcal{V}{}$ je ${}v_{1} , v_{2}, \dots, v_{n}{}$ a ${}\mathbf{A}{}$ je matice lineárního zobrazení ${}\mathbf{L}{}$ v těchto bázích, potom ${}\dim(\mathrm{Im}~ \mathbf{L}) = \mathrm{h}(\mathbf{A}){}$.

#fixme : důkaz


**Důsledek 3.** 
Nechť ${}\mathcal{U}, \mathcal{V}{}$ jsou lineární vektorové prostory konečné dimenze, nechť ${}\mathbf{L}: \mathcal{U}\to\mathcal{V}{}$ je izomorfismus. Je-li ${}\mathbf{A}{}$ matice izomorfismu ${}\mathbf{L}{}$ v daných bázích, potom matice ${}\mathbf{A}{}$ je
regulární. 

#fixme : důkaz


> [!quote] Věta 4. 
> Nechť ${}\mathbf{L}_{1} : \mathcal{U}\to\mathcal{V}, ~\mathbf{L}_{2} : \mathcal{V}\to \mathcal{W}{}$ jsou lineární zobrazení. Jestliže ${}\mathbf{A}{}$ je matice lineárního zobrazení ${}\mathbf{L}_{1}{}$ a ${}\mathbf{B}{}$ je matice lineárního zobrazení ${}\mathbf{L}_{2}{}$ v daných bázích, potom složené zobrazení ${}\mathbf{L}: \mathcal{U}\to \mathcal{W}{}$ dané předpisem ${}\mathbf{L}(x) = \mathbf{L}_{2} (\mathbf{L}_{1}(x)){}$ pro každé ${}x \in \mathcal{U}{}$ je opět lineární a matice složeného zobrazení ${}\mathbf{L}{}$ v daných bázích je ${}\mathbf{C} = \mathbf{B}\mathbf{A}{}$.

#fixme : důkaz


Nyní lze dokázat větu:
> [!quote] Věta 5. 
> Nechť ${}\mathbf{A}, \mathbf{B}{}$ jsou matice takové, že existuje součin ${}\mathbf{AB}{}$. Potom
> 
> $$
 \mathrm{h}(\mathbf{AB}) \leq \min \{ \mathrm{h}(\mathbf{A}), \mathrm{h}(\mathbf{B}) \}.
 $$

#fixme : důkaz


**Důsledek 6.** 
Nechť ${}\mathcal{U}, \mathcal{V}{}$ jsou lineární vektorové prostory konečné dimenze, nechť ${}\mathbf{L}: \mathcal{U}\to\mathcal{V}{}$ je izomorfismus. Je-li ${}u_{1}, u_{2}, \dots, u_{n}{}$ báze prostoru ${}\mathcal{U}{}$, ${} v_{1} , v_{2} , \dots, v_{n}{}$ báze prostoru ${}\mathcal{V}{}$ a ${}\mathbf{A}{}$ matice izomorfismu ${}\mathbf{L}{}$ v daných bázích, potom inverzní zobrazení ${}\mathbf{L}^{-1}: \mathcal{V}\to\mathcal{U}{}$ má v těchto bázích matici ${}\mathbf{A}^{-1}{}$.

#fixme : důkaz