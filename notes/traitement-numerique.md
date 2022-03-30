# Traitement numérique

En échantillonné, on utilise les formes normalisées de fréquence 1 :
$$x(n)$$

Mais si on a une période d'échantillonnage Te, elle se présente ainsi :

$$x(n T_e)$$

## Transformée en z

À la base, on utilise la transformée de Laplace pour "asséner un coup de massue mathématique" aux signaux dont la transformée de Fourier n'existe pas.

$$X(\sigma, \omega) = \int(x(t) e^{-\sigma t}) e^{-j\omega t} dt$$
$$X(s) = \int x(t) e^{-s t} \text{ avec } s = \sigma + j \omega$$

C'est une extension de la transformée de Fourier :
$$X(0, \omega) = X(0, 2\pi f) = X(f)$$