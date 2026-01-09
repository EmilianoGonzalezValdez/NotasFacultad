module Dibujo where


-- Definir el lenguaje via constructores de tipo
data Dibujo a =
                Basica a 
              | Rotar (Dibujo a) 
              | Rotar45 (Dibujo a)  
              | Espejar (Dibujo a) 
              | Apilar Float Float (Dibujo a) (Dibujo a) 
              | Juntar Float Float (Dibujo a) (Dibujo a)
              | Encimar (Dibujo a) (Dibujo a)
              deriving (Eq, Show)

data Cosas = Trianguloo| Rectangulo | Circulo deriving(Eq,Show) 

type Masterpiece = Dibujo Cosas

-- Composición n-veces de una función con sí misma.
comp :: (a -> a) -> Int -> a -> a
comp f 0 z = z
comp f x z = comp f (x-1) (f z)

-- Rotaciones de múltiplos de 90.
r180 :: Dibujo a -> Dibujo a
r180 d1 = Rotar(Rotar d1) 

r270 :: Dibujo a -> Dibujo a
r270 d1 = Rotar(Rotar(Rotar d1))



-- -- Pone una figura sobre la otra, ambas ocupan el mismo espacio.
(.-.) :: Dibujo a -> Dibujo a -> Dibujo a
(.-.) d1 d2 = (Apilar 1 1 d1 d2)

-- Pone una figura al lado de la otra, ambas ocupan el mismo espacio.
(///) :: Dibujo a -> Dibujo a -> Dibujo a
(///) d1 d2 = (Juntar 1 1 d1 d2)


-- Superpone una figura con otra.
(^^^) :: Dibujo a -> Dibujo a -> Dibujo a
(^^^) d1 d2 = (Encimar d1 d2)



-- -- Dadas cuatro dibujos las ubica en los cuatro cuadrantes.
cuarteto :: Dibujo a -> Dibujo a -> Dibujo a -> Dibujo a -> Dibujo a
cuarteto d1 d2 d3 d4 = (.-.)((///)d1 d2) ((///)d3 d4)

-- -- Una dibujo repetido con las cuatro rotaciones, superpuestas.
encimar4 :: Dibujo a -> Dibujo a
encimar4 d1 = (Encimar (Rotar(d1)) (Encimar(Rotar(d1)) (Encimar(Rotar(d1)) (Encimar (Rotar(d1)) d1))))


-- -- -- Cuadrado con la misma figura rotada i * 90, para i ∈ {0, ..., 3}.
-- -- -- No confundir con encimar4!
ciclar :: Dibujo a -> Dibujo a
ciclar d1 = (cuarteto d1 (Rotar(d1)) (r180(d1)) (r270(d1)))


-- Transfomar un valor de tipo a como una Basica.
pureDib :: a -> Dibujo a
pureDib = Basica

-- map para nuestro lenguaje.
mapDib :: forall a b. (a -> b) -> Dibujo a -> Dibujo b
mapDib op (Basica a) = pureDib(op a)
mapDib op (dibu) = case dibu of
                 Rotar (d1) -> Rotar (mapDib op d1)
                 Rotar45 (d1) -> Rotar45 (mapDib op d1)
                 Espejar (d1) -> Espejar (mapDib op d1)
                 Apilar f1 f2 (d1) (d2) -> Apilar f1 f2 (mapDib op d1) (mapDib op d2)
                 Juntar f1 f2 (d1) (d2) -> Juntar f1 f2 (mapDib op d1) (mapDib op d2)
                 Encimar (d1) (d2) -> Encimar (mapDib op d1) (mapDib op d2)


-- Funcion de fold para Dibujos a
foldDib :: (a -> b) -> (b -> b) -> (b -> b) -> (b -> b) ->
       (Float -> Float -> b -> b -> b) -> 
       (Float -> Float -> b -> b -> b) -> 
       (b -> b -> b) ->
       Dibujo a -> b
foldDib basic rot rot45 espejo apila junta encima dibujo = case dibujo of 
                                                         Basica a -> basic a
                                                         Rotar d -> rot (foldDib basic rot rot45 espejo apila junta encima d)
                                                         Rotar45 d -> rot45 (foldDib basic rot rot45 espejo apila junta encima d)
                                                         Espejar d -> espejo (foldDib basic rot rot45 espejo apila junta encima d)
                                                         Apilar f1 f2 b1 b2 -> apila f1 f2 (foldDib basic rot rot45 espejo apila junta encima b1) (foldDib basic rot rot45 espejo apila junta encima b2)
                                                         Juntar f1 f2 b1 b2 -> junta f1 f2 (foldDib basic rot rot45 espejo apila junta encima b1) (foldDib basic rot rot45 espejo apila junta encima b2)
                                                         Encimar b1 b2 -> encima (foldDib basic rot rot45 espejo apila junta encima b1) (foldDib basic rot rot45 espejo apila junta encima b2)
                      







