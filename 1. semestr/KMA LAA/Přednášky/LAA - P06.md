---
type: lecture
status: todo
katedra: KMA
date: 29-10-2026
---

> **Téma:** LINEÁRNÍ ZOBRAZENÍ
> **Koncepty:**
> **Zdroje**: [[P06.pdf]]


 > [!note] Definice 1.
 >  Nechť ${}\mathcal{U}, \mathcal{V}{}$ jsou lineární prostory, nechť ${}\mathbf{L}: \mathcal{U}\to\mathcal{V}{}$ je zobrazení z množiny ${}\mathcal{U}{}$ do množiny ${}\mathcal{V}{}$. Zobrazení ${}\mathbf{L}{}$ se nazývá **lineární**, jestliže pro každé ${}x, y \in \mathcal{U}{}$ a pro každé číslo ${}\lambda{}$ platí:
 >
> $$
 \begin{gathered}
 \mathbf{L}(x + y) = \mathbf{L}(x) + \mathbf{L}(y)\\ \\
 \mathbf{L}(\lambda x) = \lambda\mathbf{L}(x).
 \end{gathered}
> $$
 
**Poznámka** 1.: Pro každé lineární zobrazení ${}\mathbf{L}: \mathcal{U}\to\mathcal{V}{}$ platí ${}\mathbf{L}(0) = 0{}$.

> [!done]- Důkaz
> ${}\forall x \in \mathcal{U}~~\mathbf{L}(x)+0=\mathbf{L}(x)=\mathbf{L}(x+0)=\mathbf{L}(x)+\mathbf{L}(0)\implies 0=\mathbf{L}(0)~~\square{}$

**Příklady**:
1) ${}\mathbf{L}:\mathcal{U}\to \mathcal{U},~\forall x \in \mathcal{U}:~~\mathbf{L}(x)=x\to \mathbf{L}{}$ nazýváme **identické** ${}\equiv{}$ **identita**.
2) geometrické zobrazení: otočení o úhel, stejnolehlost, symetrie, středová souměrnost ${}\implies{}$ lineární
   ! posunutí o vektor ${}\vec{u}{}$ ${}\implies{}$ není lineární
3) ${}\mathbf{D}:P_{n}\to P_{n}:~~\mathbf{D}(p(x))=p'(x){}$ derivace v `MA1`
4) ${}\mathbf{L}:\mathbb{R}_{n}\to \mathbb{R}_{m}{}$ matice ${}\mathbf{A}_{m,n}{}$    ${}\mathbf{L}:\mathbf{L}(x \in \mathbb{R}_{n})=\mathbf{A}x\implies \mathbf{A}x \in \mathbb{R}_{m}{}$
   Úzká souvislost se soustavami lineárních rovnice
5) ...



> [!note] Definice 2. 
> Nechť ${}\mathcal{U}, \mathcal{V}{}$ jsou lineární prostory a ${}\mathbf{L}: \mathcal{U}\to\mathcal{V}{}$ je lineární zobrazení.
> 
> Množina všech prvků prostoru ${}\mathcal{U}{}$, které se zobrazí do prvku ${}0{}$, se nazývá **jádro zobrazení** ${}\mathbf{L}{}$ a značí ${}\mathrm{Ker}~ \mathbf{L}{}$. 
> 
> $$
> \mathrm{Ker}~ \mathbf{L} = \{ x \in \mathcal{U} : \mathbf{L}(x) = 0 \}.
> $$
> 
> Množina obrazů všech prvků prostoru ${}\mathcal{U}{}$ se nazývá **obraz zobrazení** ${}\mathbf{L}{}$ a značí ${}\mathrm{Im}~ \mathbf{L}{}$.
> 
> $$
> \mathrm{Im}~ \mathbf{L} = \{ y \in \mathcal{V} : \exists x \in \mathcal{U} ~~\mathbf{L}(x) = y \}.
> $$
>
> ![[Kernel_and_image_of_linear_map.svg|592]]

#fixme : důkaz o tom že ${}\mathrm{Ker}{}$ a ${}\mathrm{\mathrm{Im}}{}$ jsou podprostory


> [!quote] Věta 1. 
> Nechť ${}\mathcal{U}, \mathcal{V}{}$ jsou lineární prostory, ${}\mathbf{L}: \mathcal{U}\to\mathcal{V}{}$ je lineární zobrazení. Potom ${}\mathrm{Ker}~ \mathbf{L}{}$ je podprostor prostoru ${}\mathcal{U}, \mathrm{Im}~ \mathbf{L}{}$ je podprostor prostoru ${}\mathcal{V}{}$ a platí 
> 
> $$
> \dim(\mathrm{Ker}~ \mathbf{L}) + \dim(\mathrm{Im}~ \mathbf{L}) = \dim \mathcal{U}.
> $$
> 
> "*Dobrá kontrola při počítání příkladu*"

# Speciální typ lineárního zobrazení

> [!note] Definice 3. 
> Nechť ${}\mathcal{U}, \mathcal{V}{}$ jsou lineární prostory a ${}\mathbf{L}: \mathcal{U}\to\mathcal{V}{}$ je lineární zobrazení.
> 
> Zobrazení ${}\mathbf{L}{}$ se nazývá **izomorfismus** (vzájemně jednoznačné), je-li *prosté* a na prostor, t.j. pro každé ${}x, y \in \mathcal{U},x\neq y{}$ je ${} \mathbf{L}(x)\neq \mathbf{L}(y){}$ a pro každé ${}y \in \mathcal{V}{}$ existuje ${}x \in \mathcal{U}{}$ tak, že ${}\mathbf{L}(x) = y{}$.
> 
> Prostory ${}\mathcal{U}, \mathcal{V}{}$ se nazývají **izomorfní**, jestliže existuje izomorfismus ${}\mathbf{L}: \mathcal{U}\to\mathcal{V}{}$.


> [!quote] Věta 2. 
> Nechť ${}\mathbf{L}: \mathcal{U}\to\mathcal{V}{}$ je lineární zobrazení. Potom zobrazení ${}\mathbf{L}{}$ je izomorfismus právě tehdy, když ${}\mathrm{Ker}~ \mathbf{L} = 0{}$ a ${}\mathrm{Im}~ \mathbf{L} = \mathcal{V}{}$.

#fixme : Důkaz


> [!quote] Věta 3. 
> Jestliže ${}\mathbf{L}: \mathcal{U}\to\mathcal{V}{}$ je izomorfismus, potom existuje inverzní zobrazení ${}\mathbf{L}^{-1} : \mathcal{V}\to\mathcal{U}{}$, které je také izomorfismus.



> [!quote] Věta 4. 
> Jestliže ${}\mathbf{L}: \mathcal{U}\to\mathcal{V}{}$ je izomorfismus, potom prvky ${}x_{1} , x_{2}, \dots, x_{k} \in \mathcal{U}{}$ jsou lineárně závislé právě tehdy, když prvky ${}\mathbf{L}(x_{1}), \mathbf{L}(x_{2}), \dots, \mathbf{L}(x_{k} ) \in \mathcal{V}{}$ jsou také lineárně závislé.

#fixme : Důkaz


> [!quote] Věta 5. 
> Lineární prostory ${}\mathcal{U}, \mathcal{V}{}$ jsou izomorfní právě tehdy, když ${}\dim \mathcal{U} = \dim \mathcal{V}{}$.

#fixme : Důkaz

# Důležitý příklad izoformismu

Nechť  ${}\mathcal{U}{}$ je lineární prostor, ${}\dim \mathcal{U} = k{}$, zvolme ${}u_{1} , u_{2} , \dots, u_{k}{}$ bázi prostoru ${}\mathcal{U}{}$.

Pro každý prvek ${}x \in \mathcal{U}{}$ je ${}x = \lambda_{1}u_{1} + \lambda_{2} u_{2} + \dots + \lambda_{k} u_{k} {}$. A tedy ${}\hat{x}= [\lambda_{1}, \lambda_{2} , \dots, \lambda_{K} ]^T{}$ jsou souřadnice prvku ${}x{}$ v bázi ${}u_{1}, u_{2} , \dots, u_{k}{}$.

Definujme zobrazení ${}\mathbf{L}: \mathcal{U}\to \mathbb{R}_{k}{}$ předpisem ${}\mathbf{L}(x) = \hat{x}{}$. Toto zobrazení je izomorfismus, který se nazývá **souřadnicový izomorfismus**.

#fixme : příklady
