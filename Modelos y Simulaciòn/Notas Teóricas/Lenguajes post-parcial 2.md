
**Lema 23** (Lema de la sumatoria): Sea $\sum$ un alfabeto finito:
- Si $f:w \times S_1 \times ... \times S_n \times L1 \times ... \times L_m \rightarrow w$ es $\sum$-pr con $S_1,...,S_n \subseteq w$ y $L_1,...,Lm \subseteq \sum^*$ no vacíos, entonces las funciones $\lambda xy\overrightarrow{x\alpha}[\sum^{t=y}_{t=x} f(t,\overrightarrow{x},\overrightarrow{\alpha})]$      y $\lambda xy\overrightarrow{x\alpha}[\prod^{t=y}_{t=x} f(t,\overrightarrow{x},\overrightarrow{\alpha})]$ son $\sum$-pr
- Si $f:w \times S_1 \times ... \times S_n \times L1 \times ... \times L_m \rightarrow \sum^*$ es $\sum$-pr con $S_1,...,S_n \subseteq w$ y $L_1,...,Lm \subseteq \sum^*$ no vacíos, entonces las funciones $\lambda xy\overrightarrow{x\alpha}[\subset^{t=y}_{t=x} f(t,\overrightarrow{x},\overrightarrow{\alpha})]$ es $\sum$-pr

**Cuantificación acotada de predicados $\sum$-pr con dominio rectangular:** Sea $P : S\times S_1 \times ... \times S_n \times L_1 \times...\times L_m \rightarrow w$ un predicado con $n,m \in w$. Supongamos ademas que $S,S_1,...,S_n \subseteq w$ y $L_1,...,L_m \subseteq \sum^*$ son no vacíos. Sea $\bar{S} \subseteq S$. Entonces la expresión booleana $(\forall t \in \bar{S})_{t <= x} P(t,\overrightarrow{x},\overrightarrow{\alpha})$ depende de las variables $x. \overrightarrow{x},\overrightarrow{\alpha}$ y valdrá 1 en una $(1+n+m)$-upla cuando $P(x,\overrightarrow{x},\overrightarrow{\alpha})$  sea igual a 1 cada $t \in \{ u\in \bar{S} : u<=x \}$ y 0 en caso contrario.   También podemos cuantificar sobre variables alfabéticas de modo que $(\forall t \in \bar{L})_{|\alpha| <= x} P(\overrightarrow{x},\overrightarrow{\alpha},\alpha)$ depende de las variables $x. \overrightarrow{x},\overrightarrow{\alpha}$ y está definida cuando $(x. \overrightarrow{x},\overrightarrow{\alpha})$ pertenece a $S \times S_1 \times...\times S_n \times L_1 \times...\times L_m$ 

**Lema 24** (Lema de cuantificación acotada): Sea $\sum$ un alfabeto finito:
- Sea $P : S \times ... \times S_n \times L \times ... \times L_m \rightarrow w$ un predicado $\sum$-pr con $S,...,S_n \subseteq w$ y $L,...,L_m \subseteq \sum^*$ no vacíos. Supongamos $\bar{S} \subseteq S$ es $\sum^*$-pr. Entonces $\lambda x \overrightarrow{x} \overrightarrow{\alpha}[(\forall t \in \bar{S})_{t <=x} P(t, \overrightarrow{x},\overrightarrow{\alpha})]$ y $\lambda x \overrightarrow{x} \overrightarrow{\alpha}[(\exists t \in \bar{S})_{t <=x} P(t, \overrightarrow{x},\overrightarrow{\alpha})]$ son $\sum$-pr  
- Sea $P : S \times ... \times S_n \times L \times ... \times L_m \rightarrow w$ un predicado $\sum$-pr con $S,...,S_n \subseteq w$ y $L,...,L_m \subseteq \sum^*$ no vacíos. Supongamos $\bar{S} \subseteq S$ es $\sum^*$-pr. Entonces $\lambda x \overrightarrow{x} \overrightarrow{\alpha}[(\forall \alpha \in \bar{S})_{|\alpha| <=x} P(\overrightarrow{x},\overrightarrow{\alpha,\alpha})]$ y $\lambda x \overrightarrow{x} \overrightarrow{\alpha}[(\exists \alpha \in \bar{S})_{|\alpha| <=x} P( \overrightarrow{x},\overrightarrow{\alpha},\alpha)]$ son $\sum$-pr 

>[!WARNING]-  OBSERVACIÓN:
>La cuantificación no acotada no preserva la propiedad de ser $\sum$-pr. Hay un predicado $P:w\times L1 \rightarrow w$ tal que $\lambda \alpha[(\exists t \in w) P(t,\alpha)]$ no es $\sum$-efectivamente computable, por lo cual tampoco es $\sum$-pr 


**Regla de caracterizar pertenencia:** Si Us esta intentando probar que cierto conjunto $S \subseteq w^n \times \sum^{*m}$ es $\sum$-pr, entonces puede ser util primero caracterizar la pertenencia a $S$, es decir, escribir algo del tipo:
- Para cada $(\overrightarrow{x},\overrightarrow{\alpha}) \in w^n \times \sum^{*m}$ se tiene que $(\overrightarrow{x},\overrightarrow{\alpha}) \in S$ si y solo si...   




