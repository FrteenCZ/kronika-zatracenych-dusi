---
type: exercise
status: todo
katedra: KKY
date: 22-10-2026
---

> **Téma:** Úloha užívání léků
> **Koncepty:**

**Doba užívání**
**Množství v dávce** - ${}D{}$
**Interval** - ${}n{}$
Podmínka metabolizace
Rychlost eliminace
Bezpečnostní rizika
Kontraindikace
Rychlost účinku
**Koncentrace v krvi** - ${}d{}$
Věk
Hmotnost
Pohlaví
**% vyloučení látky** - ${}p{}$

---


$$
\begin{align}
d_{0}&=D \\
d_{1}&=d_{0}-d_{0}p+D \\
d_{2}&=d_{1}-d_{1}p+D \\
d_{2}&=d_{1}(1-p)+D \\
d_{2}&=D(1-p)^{2}+D(1-p)+D \\
 \\
d_{n}&=D\sum_{i=0}^n(1-p)^i=D \frac{1-(1-p)^{n+1}}{p}
\end{align}
$$


$$
\begin{align}
(1-p)^n\left( D-\frac{D}{p} \right)+\frac{D}{p}<(1-p)^{1-p}\left( D-\frac{D}{p} \right)-\frac{D}{p} \\
(1-p)^n<(1-p)^{n+1} \\
(1-p)^n(1-1+p)<0 \\
(1-p)^np<0
\end{align}
$$