module Pred where

import Dibujo
import Data.List

type Pred a = a -> Bool

--Para la definiciones de la funciones de este modulo, no pueden utilizar
--pattern-matching, sino alto orden a traves de la funcion foldDib, mapDib 

-- Dado un predicado sobre básicas, cambiar todas las que satisfacen
-- el predicado por el resultado de llamar a la función indicada por el
-- segundo argumento con dicha figura.
-- Por ejemplo, `cambiar (== Triangulo) (\x -> Rotar (Basica x))` rota
-- todos los triángulos.
cambiar :: Pred a -> a -> Dibujo a -> Dibujo a
cambiar pred hacer dibujo = mapDib (\x-> if (pred x) then hacer else x) dibujo


-- Alguna básica satisface el predicado.
anyDib :: Pred a -> Dibujo a -> Bool
anyDib pred d1 = foldDib (\x -> pred x) (\x->x) (\x->x) (\x->x) (\ i j k l ->  k || l) (\ i j k l -> k || l) (\i j-> i || j) d1


-- Todas las básicas satisfacen el predicado.
allDib :: Pred a -> Dibujo a -> Bool
allDib pred d1 = foldDib (\x-> pred x) (\x->x) (\x->x) (\x->x) (\ i j k l ->  k && l) (\ i j k l -> k && l) (\i j-> i && j)  d1


-- Hay 4 rotaciones seguidas.
esRot360 :: Pred (Dibujo a)
esRot360 a = snd (foldDib (const (0,False))
            (\t -> let n = fst t +1 
            in if n == 4 
             then (0, True)
             else (n, snd t))
            (\t -> (0,snd t))
            (\t -> (0,snd t))
            (\_ _  t1 t2 -> (0, snd t2 || snd t1))
            (\_ _  t1 t2 -> (0, snd t2 || snd t1))
            (\t1 t2 -> (0, snd t1 || snd t2))
            a)


-- Hay 2 espejados seguidos. 
esFlip2 :: Pred (Dibujo a)
esFlip2 dib = snd $ foldDib basic rot rot45 espejar apila junta encimar dib
            where
              -- (últimaOperación, encontrado)
              basic _ = (0, False)
              rot (op, f) = (0, f)
              rot45 (op, f) = (0, f)
              espejar (op, f) = (2, f || op == 2)
              apila _ _ (_, f1) (op2, f2) = (op2, f1 || f2)
              junta _ _ (_, f1) (op2, f2) = (op2, f1 || f2)
              encimar (_, f1) (op2, f2) = (op2, f1 || f2)


data Superfluo = RotacionSuperflua | FlipSuperfluo
  deriving (Show, Eq)

-- Chequea si el dibujo tiene una rotacion superflua
errorRotacion :: Dibujo a -> [Superfluo]
errorRotacion d1 = if esRot360 d1 then [RotacionSuperflua] else []


-- Chequea si el dibujo tiene un flip superfluo
errorFlip :: Dibujo a -> [Superfluo]
errorFlip d1 = if esFlip2 d1  then [FlipSuperfluo] else []


-- Aplica todos los chequeos y acumula todos los errores, y
-- sólo devuelve la figura si no hubo ningún error.
-- (se muestra Left y Right en el resultado, por el tipo Either)
-- (cambiar implementacion de necesitarlo en limpio)
checkSuperfluo :: Dibujo a -> Either [Superfluo] (Dibujo a)
checkSuperfluo dibu | (errorRotacion dibu) /= [] || (errorFlip dibu) /= [] = Left (errorRotacion dibu ++ errorFlip dibu)
                    | otherwise = Right dibu

