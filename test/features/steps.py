# -*- coding: utf-8 -*-
from lettuce import step, world
from app.calculadora import Calculadora

@step(u'Dado que tengo los numeros "([^"]*)" y "([^"]*)"')
def dado_que_tengo_los_numeros_group1_y_group2(step, num1, num2):
    world.num1 = int(num1)
    world.num2 = int(num2)
	
@step(u'Cuando realizo la sumatoria')
def cuando_realizo_la_sumatoria(step):
    cal = Calculadora()
    world.resultado = cal.suma(world.num1, world.num2)
	
@step(u'Entonces el resultado debe ser "([^"]*)"')
def entonces_el_resultado_debe_ser_group1(step, esperado):
    assert world.resultado == int(esperado), 'Los valores no coinciden'
	
@step(u'Cuando realizo la resta')
def cuando_realizo_la_resta(step):
    cal = Calculadora()
    world.resultado = cal.resta(world.num1, world.num2)
	
@step(u'Cuando realizo la multiplicacion')
def cuando_realizo_la_multiplicacion(step):
    cal = Calculadora()
    world.resultado = cal.multiplicacion(world.num1, world.num2)