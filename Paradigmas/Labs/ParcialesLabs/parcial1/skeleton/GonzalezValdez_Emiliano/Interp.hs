module Interp where
import Dibujo
import Graphics.Gloss
import Graphics.Gloss.Data.Vector
import qualified Graphics.Gloss.Data.Point.Arithmetic as V

type ImagenFlotante = Vector -> Vector -> Vector -> Picture

formaF :: Color -> ImagenFlotante
formaF col d w h = color col (line . map (d V.+) $
    [ vCero, uX, p13, p33, p33 V.+ uY , p13 V.+ uY
    , uX V.+ 4 V.* uY ,uX V.+ 5 V.* uY, x4 V.+ y5
    , x4 V.+ 6 V.* uY, 6 V.* uY, vCero])
  where p33 = 3 V.* (uX V.+ uY)
        p13 = uX V.+ 3 V.* uY
        x4 = 4 V.* uX
        y5 = 5 V.* uY
        uX = (1/6) V.* w
        uY = (1/6) V.* h
        vCero = (0,0)


interp_rotar :: ImagenFlotante -> ImagenFlotante
interp_rotar imagen d w h = imagen (d V.+ w) h (V.negate w)


interp_apilar :: Int -> Int -> ImagenFlotante -> ImagenFlotante -> ImagenFlotante
interp_apilar n m imagen1 imagen2 x w h =
    let r' = fromIntegral n / fromIntegral (n + m)
        r = fromIntegral m / fromIntegral (n + m)
        h' = r' V.* h
    in pictures [imagen1 (x V.+ h') w (r V.* h), imagen2 x w h']


interp_encimar :: ImagenFlotante -> ImagenFlotante -> ImagenFlotante
interp_encimar imagen1 imagen2 x w h = pictures [imagen1 x w h, imagen2 x w h]


--COMPLETAR (EJERCICIO 2-a)
interp_basica :: Bool -> ImagenFlotante
interp_basica b | b ==True = formaF blue
		| b == False = formaF red

--COMPLETAR (EJERCICIO 2-b)
interp :: Dibujo Bool -> ImagenFlotante
interp d1 = case d1 of
	  Basica a -> interp_basica a
	  Rotar d2 -> interp_rotar(interp d2)
	  Apilar f1 f2 d2 d3 -> interp_apilar f1 f2 (interp d2)(interp d3)
	  Encimar d2 d3 -> interp_encimar (interp d2)(interp d3)
	  Resize f1 d2 -> interp_resize (fromIntegral f1) (interp d2)

interp_resize :: Int -> ImagenFlotante -> ImagenFlotante
interp_resize f1 imagen d w h = imagen d (fromIntegral f1 V.* w) (fromIntegral f1 V.*h)
