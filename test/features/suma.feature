Feature: Suma de dos numeros
    Con el fin de poder realizar calculos matematicos
    Como novel en matematicas
    Realizaremos la funcion suma

    Scenario: Suma de los numeros 2 y 4
        Dado que tengo los numeros "2" y "4"
        Cuando realizo la sumatoria
        Entonces el resultado debe ser "6"

    Scenario: Suma de los numeros 7 y -4
        Dado que tengo los numeros "7" y "-4"
        Cuando realizo la sumatoria
        Entonces el resultado debe ser "3"

    Scenario: Suma de los nuemeros 8 y 100
        Dado que tengo los numeros "8" y "100"
        Cuando realizo la sumatoria 
        Entonces el resultado debe ser "108"