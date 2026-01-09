module Dibujo where

-- Definicion  del lenguaje
data Dibujo a = Basica a 
              | Rotar (Dibujo a)
              | Apilar Int Int (Dibujo a) (Dibujo a)
              | Encimar (Dibujo a) (Dibujo a) 
	      | Resize Int (Dibujo a)
              deriving(Show, Eq)


-- Funcion Map (de Basicas) para nuestro sub-lenguaje.
mapDib :: (a -> b) -> Dibujo a -> Dibujo b
mapDib f (Basica x) = Basica (f x) 
mapDib f (Rotar d1) = Rotar (mapDib f d1)
mapDib f (Apilar n m d1 d2) = Apilar n m (mapDib f d1) (mapDib f d2)
mapDib f (Encimar d1 d2) = Encimar (mapDib f d1) (mapDib f d2)
mapDib f (Resize f1 d2) = Resize f1 (mapDib f d2)

-- Funcion Fold para nuestro sub-lenguaje.
foldDib :: (a -> b) -> (b -> b) ->
       (Int -> Int -> b -> b -> b) -> 
       (b -> b -> b) ->
       (Int ->b ->b) ->
       Dibujo a -> b

foldDib sB sR sA sEn sRe d =
    let foldDibRecursiva = foldDib sB sR sA sEn sRe 
    in case d of
        Basica x -> sB x
        Rotar d -> sR $ foldDibRecursiva d
        Apilar m n d1 d2 -> sA m n (foldDibRecursiva d1) (foldDibRecursiva d2)
        Encimar d1 d2 -> sEn (foldDibRecursiva d1) (foldDibRecursiva d2)
	Resize f1 d1 -> sRe f1 (foldDibRecursiva d1)


--COMPLETAR (EJERCICIO 1-a)
toBool:: Dibujo (Int,Int) -> Dibujo Bool
toBool d1  = case d1 of
	   Basica(x,y) -> if ( mod x y == 0 || mod y x ==0 ) then Basica(True) else Basica(False)
	   Rotar(d2) -> Rotar(toBool d2)
           Apilar f1 f2 (d2) (d3) -> Apilar f1 f2 (toBool d2) (toBool d3)
	   Encimar(d2)(d3) -> Encimar(toBool d2)(toBool d3)
           Resize f1 d2 -> Resize f1 (toBool d2) 
--COMPLETAR (EJERCICIO 1-b)
toBool2:: Dibujo (Int,Int) -> Dibujo Bool
toBool2 d1 = mapDib (\(x,y) -> if (( mod x y ==0) || ( mod y x == 0)) then True else False) d1


--COMPLETAR (EJERCICIO 1-c)
profundidad:: Dibujo a -> Int
profundidad d1 = case d1 of
               Basica(a) -> 1
               Rotar(d2) -> 1+profundidad(d2)
               Apilar f1 f2 (d2)(d3) -> 1+(max (profundidad d2) (profundidad d3))
               Encimar(d2)(d3) -> 1+(max (profundidad d2) (profundidad d3))
	       Resize f1 d2 -> 1+ (profundidad d2)

--COMPLETAR (EJERCICIO 1-d)
profundidad2:: Dibujo a -> Int
profundidad2 d1 = foldDib basica rotar apilar encimar resize d1
		where
		basica a = 1
		rotar a = 1+a
		apilar f1 f2 a b = 1+ (max a b)
		encimar a b = 1+(max a  b)
 	        resize f1 a = 1+ a
