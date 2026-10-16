---
type: exercise
status: todo
date: 07-10-2026
katedra: KMA
---

> **Téma:** 
> **Koncepty:**


$$
\begin{align}
\sum_{j=1}^{n}j^k=1^{k}+2^k+3^k+\dots+n^k=\sum_{j=0}^{k+1}a_{j}n^j= \\
=a_{k+1}\cdot n^{k+1}+a_{k}n^k+a_{k-1}n^{k-1}+\dots+a_{1}n+a_{0} \\
\text{indukce:} \sum_{j=1}^{n+1}j^k=1^{k}+2^k+3^k+\dots+n^k\cdot(n+1)^k= \\
=a_{k+1}\cdot (n+1)^{k+1}+a_{k}(n+1)^k+a_{k-1}(n+1)^{k-1}+\dots+a_{1}(n+1)+a_{0} \\
 \\
\to(n+1)^k  =a_{k+1}((n+1)^{k+1}-n^{k+1})+a_{k}((n+1)^k-n^k)+\dots+a_{1}((n+1)^1-n^1)+a_{0}(1-1) \\
\text{z binomické věty } \to n^{2}+  \binom{k}{1}n\dots
\end{align}
$$