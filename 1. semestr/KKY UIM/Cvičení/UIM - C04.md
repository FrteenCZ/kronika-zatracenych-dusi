---
type: exercise
status: todo
katedra: KKY
date: 15-10-2026
---

> **Téma:** Fibonacciho posloupnost
> **Koncepty:** 

# Králíci
**staří** - od 2. měsíce života
**mladí**
měsíc
**počáteční počet** - 1 pár mladých - ${}F(0){}$ = 1
**kolik rodí** - ${}2{}$
**jak často** - $1/\text{měsíc}$
kapacita prostředí - ${}\infty{}$
**délka experimentu**  - ${}F(n){}$
délka života - ${}\infty{}$
migrace - ${}0{}$
období

--- 

| n   | staří | mladí | F(n) |
| --- | ----- | ----- | ---- |
| 0   | 0     | 1     | 1    |
| 1   | 1     | 0     | 1    |
| 2   | 1     | 1     | 2    |
| 3   | 2     | 1     | 3    |
| 4   | 3     | 2     | 5    |

$$
\begin{align}
F(n+2)&=F(n+1)+F(n); F(0)=1;F(1)=1
 \\
F(n+2)-F(n+1)-F(n)&=0 \\
y(n+2)-y(n+1)-y(n)&=0 \\
\lambda^{2}-\lambda-1&=0 \\
 \\
F(n)&=c_{1}\cdot\lambda_{1}^n +c_{2}\lambda_{2}^n \\
 \\
F(0)&=c_{1}+c_{2}=1 \\
F(1)&=c_{1} \frac{1+\sqrt{ 5 }}{2}+c_{2} \frac{1-\sqrt{ 5 }}{2}=1 \\
 \\
1--\frac{1+\sqrt{ 5 }}{2}&=c_{2}\cdot\left( \frac{1-\sqrt{ 5 }}{2}-\frac{1+\sqrt{ 5 }}{2} \right) \\
\frac{1-\sqrt{ 5 }}{2}&=c_{2}\cdot\left( \frac{1-\sqrt{ 5 }-1-\sqrt{ 5 }}{2} \right) \\
\frac{1-\sqrt{ 5 }}{2}&=c_{2}\cdot \sqrt{ 5 } \\
\frac{1-\sqrt{ 5 }}{2 \sqrt{ 5 }}&=c_{2} \\
\frac{\sqrt{ 5 }-5}{10}&=c_{2} \\
1-\frac{\sqrt{ 5 }-5}{10}&=c_{1} \\
\frac{10-\sqrt{ 5 }+5}{10}&=c_{1} \\
\frac{15-\sqrt{ 5 }}{10}&=c_{1}
\end{align}$$


$$
f(n)\approx \frac{\sqrt{ 5 }}{5}\left( \frac{1+\sqrt{ 5 }}{2} \right)^{n+1}
$$