#los string son las comillas que se ponen entre oraciones para que la consola lea palabras, estos pueden utilizar otros comandos para modificar el texto que tienen dentro
print("Academia jirafil")
#para separar en parrafos se usa \n
print("Academia\njirafil")
#para poner comillas se pone \"
print("Academia \"jirafil\"")
#tambien puedes no poner el texto si lo pones como una variable y continuarlo con un +, esto ultimo se llama concatenacion
Phrase = " Academia jirafil "
print("La" + Phrase + "esta lejos")
#este texto puede estar puramente en minuscula o mayuscula si añades la opcion a la variable
print("La" + Phrase.lower() + "esta lejos")
print("La" + Phrase.upper() + "esta lejos")
#tambien se pueden dar resultados verdadero o falso si se añade un "is" antes del upper o lower, si la frase esta completamente en mayuscula o minuscula dara verdadero, y si no entonces falso
print(Phrase.islower())
#estas funciones tambien se pueden combinar, por ejemplo, si tomamos la frase, la volvemos mayuscula y entonces preguntamos si es mayuscula dara verdadero
print(Phrase.upper().isupper())
#si quiero saber cuantas letras tiene una variable se usa "len"
print(len(Phrase))
print(len("La" + Phrase + "esta lejos"))
#si quieres saber cual letra es cierto numero puedes hacerlo usando "[]", la primera letra es el cero y los espacios tambien cuentan como letras
print(Phrase[2])
print("La" [0] + Phrase [5] + "esta lejos" [3])
#tambien se pueden saber donde estan letras o palabras con index, tambien puedes poner un conjunto de letras para saber donde empieza
print(Phrase.index("m"))
print(Phrase.index("jiraf"))
#se pueden sustituir partes del texto con .replace
print(Phrase.replace("Academia","Escuela"))
