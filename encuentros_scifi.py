import random
from random import shuffle

lista = ["Tu nave espacial se encuentra con un enorme buque de investigación que parece haber sido abandonado. La tripulación de este buque abandonado ha sido consumida por criaturas con una habilidad de camuflaje natural, haciéndolas casi invisibles.", "Una estación espacial minera en el cinturón de un asteroide planetario está teniendo dificultades con pequeños asteroides que parecen atacar a la estación. Después se descubre que el cinturón en su conjunto es una criatura serpiente que intenta defenderse desesperadamente", "Ves un asteroide acercándose a ti. Tras una estrecha inspección, parece estar hecha de carne viva.", "Detectas un buque dañado con la baliza de salto. Parece que la nave está absorviendo metal de la baliza, arriesgándose a destruirla y a quedarse varada.", "Encuentras el origen de una llamada de socorro en una pequeña estación de investigación. Parece que un pequeño fuego se salió de control y amenaza con destruir la estación. Su sistema de supresión de incendios no respondes.", "Un gran convoy de naves civiles parece estar pasando por la región. No muestra intenciones hostiles, pero no se arriesgan, enviando inmediatamente a su escolta al ataque.", "Una nave enemiga ha redirigido sus generadores de gravedad para lanzaros asteroides desde un campo de asteroides cercano", "Una estación científica implosionó durante la prueba de una nueva arma, pero juzgó mal el tamaño del agujero negro resultante. Ahora, están cayendo hacia el horizonte de sucesos, enviando avisos de mayday y evacuación completa", "Inmediantamente te llama una nave de aspecto peligroso. Hoy me siento generoso. Te dejaré elegir tu propia muerte. ¿Cual te gusta menos? Escudos, oxígeno o armas. El que eligen será deshabilitado por las naves enemigas durante la batalla."]

#encuentro_random = ""
random.seed()
cuantos_encuentros = len (lista)
cuantos_encuentros = int (cuantos_encuentros)
encuentro_random = random.choice(lista)
#shuffle(lista)
#encuentro_random = lista[2]
