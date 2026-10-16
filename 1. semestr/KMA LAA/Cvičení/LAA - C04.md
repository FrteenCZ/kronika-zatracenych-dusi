---
type: exercise
status: todo
katedra: KMA
date: 13-10-2026
---

> **Téma:** 
> **Koncepty:** [[Matice]] [[Matice#Determinant]]


Vyřešte (maticově) soustavu rovnic:

$$
\begin{aligned}
a+b+2 c+d & =1 \\
a-b+c-d & =10 \\
a+c+d & =0 \\
3 a+b-c-d & =2
\end{aligned}
$$

$$
\begin{align}
\begin{bmatrix*}[cccc|c]
1 & 1 & 2 & 1 & 1 \\
1 & -1 & 1 & -1 & 10 \\
1 & 0 & 1 & 1 & 0 \\
3 & 1 & -1 & -1 & 2
\end{bmatrix*}\sim\begin{bmatrix*}[cccc|c]
1 & 1 & 2 & 1 & 1 \\
0 & -2 & -1 & -2 & 9 \\
0 & -1 & -1 & 0 & -1 \\
0 & -2 & -7 & -4 & -1
\end{bmatrix*}\sim\begin{bmatrix*}[cccc|c]
1 & 1 & 2 & 1 & 1 \\
0 & 1 & 1 & 0 & 1 \\
0 & -2 & -1 & -2 & 9 \\
0 & 2 & 7 & 4 & 1
\end{bmatrix*}\sim \\
\sim\begin{bmatrix*}[cccc|c]
1 & 1 & 2 & 1 & 1 \\
0 & 1 & 1 & 0 & 1 \\
0 & 0 & 1 & -2 & 11 \\
0 & 0 & 5 & 4 & -1
\end{bmatrix*}\sim\begin{bmatrix*}[cccc|c]
1 & 1 & 2 & 1 & 1 \\
0 & 1 & 1 & 0 & 1 \\
0 & 0 & 1 & -2 & 11 \\
0 & 0 & 0 & 14 & -56
\end{bmatrix*}\sim\begin{bmatrix*}[cccc|c]
1 & 1 & 2 & 1 & 1 \\
0 & 1 & 1 & 0 & 1 \\
0 & 0 & 1 & -2 & 11 \\
0 & 0 & 0 & 1 & -4
\end{bmatrix*} \\
 \\
d=-4 \\
c=11+2(-4)=3 \\
b=1-3=-2 \\
a=1+2-6+4=1
\end{align}
$$
---
Vyřešte (maticově) soustavu rovnic:

$$
\begin{aligned}
& x+2 y-z=3 \\
& x-y+2 z=3 \\
& 2 x+y+z=5
\end{aligned}
$$


$$
\begin{align}
\begin{bmatrix*}[ccc|c]
1 & 2 & -1 & 3 \\
1 & -1 & 2 & 3 \\
2 & 1 & 1 & 5
\end{bmatrix*}\sim\begin{bmatrix*}[ccc|c]
1 & 2 & -1 & 3 \\
0 & -3 & 3 & 0 \\
0 & -3 & 3 & -1
\end{bmatrix*}\sim\begin{bmatrix*}[ccc|c]
1 & 2 & -1 & 3 \\
0 & -3 & 3 & 0 \\
0 & 0 & 0 & -1
\end{bmatrix*}
\end{align}
$$
nemá řešení

---
Určete znaménko permutace:

$$
\left(\begin{array}{lllllllll}
1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 \\
1 & 9 & 4 & 3 & 7 & 6 & 5 & 8 & 2
\end{array}\right)
$$

$$
\begin{align}
2\leftrightarrow 9 \\
3\leftrightarrow 4 \\
5\leftrightarrow 7
\end{align}
$$
${}\mathrm{zn}(\pi)=-1{}$

---
Vypočítejte:

$$
\begin{align}
\operatorname{det}\left[\begin{array}{lll}
4 & 1 & 2 \\
1 & 3 & 1 \\
2 & 1 & 5
\end{array}\right] =4\cdot 3\cdot 5+1\cdot 1\cdot 2+2\cdot 1\cdot 1-4\cdot 1\cdot 1-1\cdot 1\cdot 5-2\cdot 3\cdot 2= \\
=60+2+2-4-5-12=60+2+2-4-5-12=43
\end{align}
$$

$$
\begin{align}
\operatorname{det}\left[\begin{array}{cc}
3 & -1 \\
1 & 2
\end{array}\right] =3\cdot 2-(-1)\cdot 1=6+1=7
\end{align}
$$

$$
\begin{align}
\operatorname{det}[-2]=-2
\end{align}
$$

$$
\begin{align}
\operatorname{det}\begin{bmatrix}

\end{bmatrix}=1
\end{align}
$$

$$
\begin{align}
\operatorname{det}\left[\begin{array}{cccc}
2 & 3 & 4 & 6 \\
-1 & 5 & 1 & 3 \\
1 & 3 & 3 & 5 \\
5 & 3 & 4 & 9
\end{array}\right]=\operatorname{det}\left[\begin{array}{cccc}
0 & -3 & -2 & -4 \\
0 & 8 & 4 & 8 \\
1 & 3 & 3 & 5 \\
0 & -12 & -11 & -16
\end{array}\right]=1\cdot(-1)^{1+3}\cdot \det \begin{bmatrix}
-3 & -2 & -4 \\
8 & 4 & 8 \\
-12 & -11 & -16
\end{bmatrix}= \\
=1\cdot(192+192+352-264-256-192)=24
\end{align}
$$


$$
\begin{align}
\operatorname{det}\left[\begin{array}{ccccc}
\frac{5}{\log 2} & 0 & 1 & \sqrt[3]{7} & 0 \\
2 & 0 & 0 & 0 & 0 \\
-\frac{7}{16} & 0 & 0 & 1 & 0 \\
3 i & \cos \frac{\pi}{8} & 2^{-16} & \frac{\sqrt{3}}{2} i & \mathbf{1} \\
\pi^{5 e^2} & 1 & \log \frac{1}{23} & -6 & 0
\end{array}\right]=1\cdot(-1)^{5+4}\cdot \det \begin{bmatrix}
\frac{5}{\log 2} & 0 & 1 & \sqrt[3]{ 7 } \\
2 & 0 & 0 & 0 \\
-\frac{7}{16} & 0 & 0 & 1 \\
\pi^{5e^{2}} & 1 & \log \frac{1}{23} & -6 
\end{bmatrix}= \\
=-1\cdot 2\cdot(-1)^{1+2}\det \begin{bmatrix}
0 & 1 & \sqrt[3]{ 7 } \\
0 & 0 & 1 \\
1 & \log \frac{1}{23} & -6 
\end{bmatrix}=2\cdot 1\cdot(-1)^{1+3}\cdot \det \begin{bmatrix}
1 & \sqrt[3]{ 7 } \\
0 & 1
\end{bmatrix}=2\cdot(1)=2
\end{align}
$$



