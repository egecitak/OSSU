;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname notebook-functions) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)

(define (bulb c)
  (circle 40 "solid" c))

(bulb "purple")

(above (bulb "red")
       (bulb "blue")
       (bulb "yellow"))

;Booleans

(define WIDTH 400)
(define HEIGHT 600)

(> WIDTH HEIGHT)
(>= WIDTH HEIGHT)
(< WIDTH HEIGHT)
(<= WIDTH HEIGHT)
(= WIDTH HEIGHT)

(string=? "foo" "bar")

(define I1 (rectangle 10 20 "solid" "red"))
(define I2 (rectangle 20 30 "solid" "blue"))

(if (< (image-width I1)
       (image-width I2))
    "tall"
    "wide")
