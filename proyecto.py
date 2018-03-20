#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
import sys
import optparse

def printError(msg, exit = False):
        sys.stderr.write('Error:\t%s\n' % msg)
        if exit:
            sys.exit(1)

def addOptions():
	parser = optparse.OptionParser()
	parser.add_option('-m','--romperHash', dest='romperHash', default=None, help='Recibe un hash a romper')
	parser.add_option('-M', '--romperHashes', dest='romperHashes', defalult=None, help='Recibe una lista de hashes a romper')
	parser.add_option('-a', '--algoritmo', dest='algoritmo', default=None, help='Algoritmo con el que fue calculado el hash a romper/algoritmos para la rainbow table')
	parser.add_option('-d', '--diccionario', dest='diccionario', default=None, help='Diccionario de contraseñas para el cálculo de hashes')
	parser.add_option('-s', '--salt', dest='salt', default=None, help='Salt a usar para el cálculo del hash')
	parser.add_option('-f', '--formato', dest='formato', default=None, help='Formato de uso de la salt ($salt$pass o $pass$salt)')
	parser.add_option('-o', '--output', dest='output', default=None, help='Archivo dónde se guardará el reporte de los resultados')
	parser.add_option('-t', '--threads', dest='threads', default=None, help='Número de hilos a utilizar para el calculo de los hashes')
	parser.add_option('-c', '--config', dest='config', default=None, help='Archivo de configuración que puede ser usado para modificar la ejecución')
	parser.add_option('-i', '--identif', dest='identif', default=None, help='Identifica el tipo de hash introducido')
	parser.add_option('-g', '--genera', dest='genera', default=None, help='Genera una base de datos con los hashes de un diccionario de contraseñas')
	parser.add_option('-b', '--hashkiller', dest='hashkiller', default=None, help='Usar modo "hash killer" para romper contraseñas')
	parser.add_option('-k', '--hashcat', dest='hashcat', default=None, help='Usar modo "hashcat" para romper contraseñas')
	parser.add_option('-e', '--shadow', dest='shadow', default=None, help='Usar un archivo con el formato /etc/shadow')
	parser.add_option('-v', '--verbose', dest='verbose', default=None, help='Imprime la información detallada de la ejecucuión del programa')
	opts,args = parser.parse_args()
	return opts


##############################################################
# Método para leer configuraciones desde un archivo de texto #
# y pasarlas a un diccionario                                #
# Recibe:                                                    #
# Un archivo de texto                                        #
#############################################################
def lee_configuracion(archivo):
	res = {}
    with open(archivo,'r') as configuraciones:
		for linea in configuraciones.readlines():
			linea = linea.split('=')
			opcion = linea[0]
			valor = linea[1]
			res[opcion] = valor
	return res			

############################################################################################
#                                                                                          #
#Función para almacenar las opciones que nos pasen por línea de comandos en un diccionario #
#																						   #
############################################################################################			
def obten_valores(opts):
    valores = {} 
    valores['hash'] = opts.valores
    valores['hashes'] = opts.hash
    valores['algoritmo'] = opts.hashes
    valores['puerto'] = opts.puerto
    valores['diccionario'] = opts.diccionario
    valores['salt'] = opts.salt
    valores['formato'] = opts.formato
    valores['output'] = opts.output
    valores['threads'] = opts.threads
    valores['config'] = opts.config
    valores['identif'] = opts.identif
    valores['genera'] = opts.genera
    valores['hashkiller'] = opts.hashkiller
    valores['verboso'] = opst.verboso
    valores['hashcat'] = opts.hashcat
    valores['shadow'] = opts.shadow 
return valores

#####################################################################################################
#																									#
#Función para cambiar el diccionario original en caso de recibir un archivo de configuración        #
#																									#
#####################################################################################################

def cambia_parametros(original, modificado):
	for key in modificado.keys():
		original[key] = modificado[key]
	return original

