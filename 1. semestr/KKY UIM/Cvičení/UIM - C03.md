---
type: exercise
status: todo
date: 08-10-2026
katedra: KKY
---

> **Téma:** Umořování dluhu
> **Koncepty:** [[Model]]

- výše dluhu
- solidita
- výše půjčky - ${}D{}$
- frekvence splácení
- úrok - ${}p{}$
- stabilita úroku
- doba fixace
- zástava
- rpsn
- kdy dochází k úročení
- splátka - ${}z{}$
---
- doba splácení?
- Kolik zaplatíme navíc?
- Mimořádné splátky?
- Výše dluhu v n-tém roce? ${}d_{n}{}$
- Výše splátky?
- Kdy nedojde ke splacení?


---

- Výše půjčky
- kdy úročení
- úrok
- výše dluhu
- frekvence splácení
- splátka

$$
\begin{align}
D=d_{0} \\
d_{1}=d_{0}+d_{0}\cdot p-z=D+D\cdot p-z = D(1+p)-z\\
d_{2}=d_{1}+d_{1}\cdotp p-z=(D(1+p)-z)+(D(1+p)-z)\cdot p-z=D+Dp-z+Dp+Dp^{2}-pz-z= \\
=D+2Dp-2z+Dp^{2}-pz=D(1+p)^{2}-z(1+p)-z \\
d_{3}=d_{2}(1+p)-z=(D(1+p)^{2}-z(1+p)-z)(1+p)-z=D(1+p)^{3}-z(1+p)^{2}-z(1+p)-z
\end{align}
$$

$$
\begin{align}
d_{n}=D(1+p)^n -z \frac{(1+p)^n-1}{p} \text{ pro } n<f, d_{f}=0
\end{align}
$$
