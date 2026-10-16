---
type: concept
aliases:
status: draft
katedra: KMA
---
# **výrok** - oznamovací věta, o které má smysl přemýšlet, zda je pravdivá či ne
př.:
	A: venku prší.   nepravdivý výrok $p(A)=0$
	B: $1+1=2$            pravdivý výrok.    $p(A)=1$
	C: běž pryč.       není výrok
	D: kolik je hodin? není výrok
	E: $x+1=2$             není výrok, je to výroková forma

# Negace výroku
opačný výrok, výrok s opačnou pravdivostní hodnotou

značka: $\overline{A}, \neg{A}, \mathrm{non} A$
"není pravda, že $A$"

např.:
	Není pravda, že venku prší
	Není pravda, že $1+1=2$

# Složené výroky
výroky lze skládat pomocí logických spojek

- konjunkce - $A \land B$   "A a zároveň B"
- disjunkce - $A \lor B$     "A nebo B"
- implikace - $A \implies B$   "Pokud A, potom B"
- ekvivalence - $A \Longleftrightarrow B$ ($(A\implies B) \land (B \implies A)$) "A právě tehdy, když B"


| $A$ | $B$ | $A \land B$ | $A \lor B$ | $A \implies B$ | $A\Longleftrightarrow B$ |
| :-: | :-: | :---------: | :--------: | :------------: | :----------------------: |
|  1  |  1  |      1      |     1      |       1        |            1             |
|  1  |  0  |      0      |     1      |       0        |            0             |
|  0  |  1  |      0      |     1      |       1        |            0             |
|  0  |  0  |      0      |     0      |       1        |            1             |

## implikace
pozn.: implikace $A \implies B$
$A$ je postačující podmínka pro $B$
$B$ je nutné podmínka pro $A$
( $Zk \implies Zp$)

**obmíněná implikace X obrácená implikace**
${}\overline{B}\implies\overline{A}{}$                       X             ${}B\implies A{}$

| ${}A{}$ | ${}B{}$ | ${}\overline{A}{}$ | ${}\overline{B}{}$ | ${}A\implies B{}$ | ${}\overline{B}\implies\overline{A}{}$ | ${}B\implies A{}$ |
| :-----: | :-----: | :----------------: | :----------------: | :---------------: | :------------------------------------: | :---------------: |
|    1    |    1    |         0          |         0          |         1         |                   1                    |         1         |
|    1    |    0    |         0          |         1          |         0         |                   0                    |         1         |
|    0    |    1    |         1          |         0          |         1         |                   1                    |         0         |
|    0    |    0    |         1          |         1          |         1         |                   1                    |         1         |

**negace implikace**: ${}\overline{A\implies B}\Leftrightarrow A\land\overline{B}{}$

# Kvantifikované výroky
- výroková forma: ${}V(x), V(x,y),\dots{}$
	- ${}V(x){}$ je výrokem pro konkrétní hodnotou proměnné ${}x{}$
	- např.: ${}V(x):x+1=1{}$
- **kvantifikace**:
	- ${}\forall{}$ velký kvantifikátor
		- např.: ${}\forall x\in \mathbb{R}:x+1=1~(p=1){}$
	- ${}\exists{}$ malý/existenční kvantifikátor
		- např.: ${}\exists x\in \mathbb{R}:x+1=1~(p=1){}$
		- ${}\exists!{}$ "existuje právě jedno"
		- ${}\nexists{}$ "neexistuje"
	- pozn.:
		- ${}V(x,y){}$ je třeba kvantifikovat všechny proměné
			- ${}\forall x\in \mathbb{R}:x+y=1{}$ není výrok
		- !**záleží na pořadí**
			- ${}\forall x\in \mathbb{R}\exists y\in \mathbb{R}:x+y=1{}$ pravdivý výrok
			- ${}\exists y\in \mathbb{R}\forall x\in \mathbb{R}:x+y=1{}$ nepravdivý výrok

---

př.:
$\gamma=(A\implies B)\Longleftrightarrow(A\land \neg B)$

| $A$ | $B$ | $A\implies B$ | $A\land \neg B$ | $\gamma$ |
| :-: | :-: | :-----------: | :-------------: | :------: |
|  1  |  1  |       1       |        0        |    0     |
|  1  |  0  |       0       |        1        |    0     |
|  0  |  1  |       1       |        0        |    0     |
|  0  |  0  |       1       |        0        |    0     |
**Kondratikce**

${}\ell=((A\implies B)\land(B\implies C))\implies(A\implies C){}$

| $A$ | $B$ | $C$ | ${}A\implies B{}$ | ${}B\implies C{}$ | ${}(A\implies B)\land(B\implies C){}$ | ${}A\implies C{}$ | ${}\ell{}$ |
| :-: | :-: | :-: | :---------------: | :---------------: | :-----------------------------------: | :---------------: | :--------: |
|  1  |  1  |  1  |         1         |         1         |                   1                   |         1         |     1      |
|  1  |  1  |  0  |         1         |         0         |                   0                   |         0         |     1      |
|  1  |  0  |  1  |         0         |         1         |                   0                   |         1         |     1      |
|  1  |  0  |  0  |         0         |         1         |                   0                   |         0         |     1      |
|  0  |  1  |  1  |         1         |         1         |                   1                   |         1         |     1      |
|  0  |  1  |  0  |         1         |         0         |                   0                   |         1         |     1      |
|  0  |  0  |  1  |         1         |         1         |                   1                   |         1         |     1      |
|  0  |  0  |  0  |         1         |         1         |                   1                   |         1         |     1      |
**Tautologie**

