---
type: concept
aliases:
  - Populace
status: todo
katedra: KKY
---
[[Model]]

- births - ${}b{}$ - ${}x_{b}=b\cdot x_{k}{}$
- deaths - ${}d{}$ - ${}x_{d}=d\cdot x_{k}{}$


${}x_{k+1}=x_{k}b-x_{k}d+x_{k}=x_{k}(1+b-d)~~~~ r:=(1+b-d){}$    →   ${}0<r{}$

$$
\begin{gathered}
x_{k+1}=r\cdot x_{k} ~~~~ x(0)=x_{0} \\ \\
\boxed{x_{k}=x_{0}\cdot r^k} \\
\boxed{x_{k+1}=f(x_{k})\cdot x_{k}}
\end{gathered}
$$

- kapacita prostředí - ${}K{}$ - ${}0<K{}$
$$
f(x)=r\left( 1-\frac{x}{K} \right)
$$
- rovnovážný stav - ${}x^r{}$


$$
\begin{gathered}
x^r:x_{k+1}=x_{k} \\
\text{smysluplnost}:x_{k+1}\geq x_{k}
\end{gathered}
$$
