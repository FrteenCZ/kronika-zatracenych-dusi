---
type: exercise
status: todo
date: 30-09-2026
katedra: KMA
---

> **Téma:** 
> **Koncepty:** [[Výroková logika]]


$$
\begin{align}
\neg(a\lor b)&=\neg a\land \neg b \\
\neg(a\land b)&=\neg a\lor \neg b \\
\neg(a\implies b)&=a\land \neg b \\
\neg(a\Leftrightarrow b)&=(a\land \neg b)\lor(\neg a\land b)
\end{align}
$$
př.:
${}\neg(a\implies b)\land(c\Leftrightarrow (\neg a\lor b)){}$

|  a  |  b  |  c  | ${}\neg a\lor b{}$ | ${}c\Leftrightarrow(\neg a\lor b){}$ | ${}\neg(a\implies b){}$ | ${}\varphi{}$ |
| :-: | :-: | :-: | :----------------: | :----------------------------------: | :---------------------: | :-----------: |
|  1  |  1  |  1  |         1          |                  1                   |            0            |       0       |
|  1  |  1  |  0  |         1          |                  0                   |            0            |       0       |
|  1  |  0  |  1  |         0          |                  0                   |            1            |       0       |
|  1  |  0  |  0  |         0          |                  1                   |            1            |       1       |
|  0  |  1  |  1  |         1          |                  1                   |            0            |       0       |
|  0  |  1  |  0  |         1          |                  0                   |            0            |       0       |
|  0  |  0  |  1  |         1          |                  1                   |            0            |       0       |
|  0  |  0  |  0  |         1          |                  0                   |            0            |       0       |

---

důkaz ${}(\text{mod}_{9}{(n)}=0)\Leftrightarrow (\text{mod}_{9}(\text{ciferný součet }n)=0){}$
13 taky dělal

---

# Důkaz indukcí
${}1+2+3+\dots+n=\frac{n(n+1)}{2}=\frac{n^{2}}{2}+\frac{n}{2}{}$
${}1^{2}+2^{2}+3^{2}+\dots n^{2}=\frac{n^{3}}{3}+\frac{n^{2}}{2}+\frac{n}{6}{}$

${}n=1\to \frac{1^{2}}{2}+\frac{1}{2}=\frac{1}{2}+\frac{1}{2}=1{}$
platí pro ${}n_{1}\implies^?{}$ platí pro, $n+1$
$$
\begin{align}
1+2+3+\dots+n&=\frac{n(n+1)}{2} \\
1+2+3+\dots+n+(n+1)&= \frac{(n+1)((n+1)+1)}{2}=\frac{(n+1)(n+2)}{2} \\
 \\
(1+2+3+\dots+n+(n+1))-(1+2+3+\dots+n)&=\frac{(n+1)(n+2)}{2}-\frac{n(n+1)}{2} \\
n+1&=\frac{(n+1)(n+2)-n(n+1)}{2} \\
n+1&=\frac{(n+1)(n+2-n)}{2} \\
n+1&=\frac{(n+1)(2)}{2} \\
n+1&=n+1
\end{align}
$$



