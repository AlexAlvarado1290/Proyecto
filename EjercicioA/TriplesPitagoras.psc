Proceso TriplesPitagoras
	
	//Este Algoritmo encuentra triples de pitagoras tanto el cateto 1 como el cateto 2 y la hipotenus sean menores a 500
	
	//i = el primer cateto
	//j = el segundo cateto
	//h = la hipotenusa
	
	Para i = 1 Hasta 500
		Para j = i Hasta 500
			Para h = j Hasta 500
				// Comprobar si se cumple el teorema de Pit�goras
				Si i^2 + j^2 = h^2 Entonces
				// Si la condici�n se cumple, imprimir el Triple de Pit�goras
                    Escribir "Triple de Pit�goras: (", i, ", ", j, ", ", h, ")"
                Fin Si
			FinPara
		FinPara
	FinPara
	
Fin Proceso


