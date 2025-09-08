-- Sacar del esqueleto final!
module Interp where
import Graphics.Gloss
import Graphics.Gloss.Data.Vector
import qualified Graphics.Gloss.Data.Point.Arithmetic as V
import Dibujo
import Graphics.Gloss (pictures)


-- Gloss provee el tipo Vector y Picture.
type ImagenFlotante = Vector -> Vector -> Vector -> Picture
type Interpretacion a = a -> ImagenFlotante

mitad :: Vector -> Vector
mitad = (0.5 V.*)



-- Interpretaciones de los constructores de Dibujo

--interpreta el operador rotar
interp_rotar :: ImagenFlotante -> ImagenFlotante
interp_rotar im d w h = im (d V.+ w) h (V.negate w)

--interpreta el operador de espejar
interp_espejar :: ImagenFlotante -> ImagenFlotante
interp_espejar im d w h = im (d V.+ w) (V.negate w) h 
--interpreta el operador de rotacion 45
interp_rotar45 :: ImagenFlotante -> ImagenFlotante
interp_rotar45 im d w h = im  (d V.+ mitad (w V.+ h)) (mitad (w V.+ h)) (mitad (h  V.- w ))

-- --interpreta el operador de apilar
interp_apilar :: Float -> Float -> ImagenFlotante -> ImagenFlotante -> ImagenFlotante
interp_apilar n m im1 im2 d w h =
  let total = n + m
      h1 = (m / total) V.* h
      h2 = (n / total) V.* h
      im1' = im1 (d V.+ h1) w h2
      im2' = im2 d w h1
  in pictures [im1', im2']
-- --interpreta el operador de juntar
interp_juntar :: Float -> Float -> ImagenFlotante -> ImagenFlotante -> ImagenFlotante
interp_juntar n m im1 im2 d w h =
  let total = n + m
      w1 = (n / total) V.* w
      w2 = (m / total) V.* w
      im1' = im1 d w1 h
      im2' = im2 (d V.+ w1) w2 h
  in pictures [im1', im2']

-- --interpreta el operador de encimar
interp_encimar :: ImagenFlotante -> ImagenFlotante -> ImagenFlotante
interp_encimar im1 im2 d w h = pictures [im1 d w h, im2 d w h]

-- --interpreta cualquier expresion del tipo Dibujo a
-- --utilizar foldDib
interp :: Interpretacion a -> Dibujo a -> ImagenFlotante
interp inter d1 = foldDib inter  (interp_rotar) (interp_rotar45) (interp_espejar) (interp_apilar) (interp_juntar) (interp_encimar) d1


