# -*- coding: utf-8 -*-
"""
Created on Mon May 11 20:09:11 2020

@author: Marina Pacheco
"""

import pymysql.cursors
import sys

connection = pymysql.connect(host = 'localhost',
                            user = 'MarinaPacheco22',
                            password = 'XXXXXXX',
                            db = 'proyecto',
                            charset = 'utf8mb4',
                            cursorclass = pymysql.cursors.DictCursor)

consulta = "SELECT"

print('''¿En qué tabla quieres realizar la búsqueda?
      1. Enfermedad
      2. Genes
      3. Fenotipos
      4. Localizaciones
      5. Salir del programa''')
      
tabla = input("Escribe el número correspondiente: ");

#TABLA ENFERMEDAD

if tabla == "1":
    tabla = "enfermedad"
    print('''¿Qué quieres mostrar de la tabla de enfermedad?
          1. Nombre
          2. Orphanumber
          3. Edad de comienzo
          4. Edad de fallecimiento
          5. Herencia
          6. Localizacion
          7. Todo''')
    columna = input("Escribe el número correspondiente: ")      
    if columna == "7":
        consulta = consulta + " * FROM " + tabla
        try:
            with connection.cursor() as cursor:
                cursor.execute(consulta + ";")
                print()
                for row in cursor:
                    print(row)
                print()
        finally:
            # Close connection.
            connection.close()
    else:
        if columna == "1":
            consulta = consulta + " nombre "
        elif columna == "2":
            consulta = consulta + " orphanumber "
        elif columna == "3":
            consulta = consulta + " edad_comienzo " 
        elif columna == "4":
            consulta = consulta + " edad_fallecimiento "
        elif columna == "5":
            consulta = consulta + " herencia "
        elif columna == "6":
            consulta = consulta + " id_localizacion "
        elif columna == "":
            connection.close()
            try:
                with connection.cursor() as cursor:
                    cursor.execute(consulta + ";")
                    print()
                    for row in cursor:
                        print(row)
                    print()
            finally:
                # Close connection.
                connection.close()
        
        print('''¿Quiere mostrar los resultados o seleccionar más información?
              1. Mostrar los resultados
              2. Seleccionar más información
              ''')
        paso2 = input("Escribe el número correspondiente: ")
        
        
        while paso2 == "2":
            print('''¿Qué quieres mostrar de la tabla de enfermedades?
              1. Nombre
              2. Orphanumber
              3. Edad de comienzo
              4. Edad de fallecimiento
              5. Herencia
              6. Localizacion''')
              
            columna = input("Escribe el número correspondiente: ")
            if columna == "1":
                consulta = consulta + ", nombre "
            elif columna == "2":
                consulta = consulta + ", orphanumber "
            elif columna == "3":
                consulta = consulta + ", edad_comienzo " 
            elif columna == "4":
                consulta = consulta + ", edad_fallecimiento "
            elif columna == "5":
                consulta = consulta + ", herencia "
            elif columna == "6":
                consulta = consulta + ", id_localizacion "
            print('''¿Quiere mostrar los resultados o seleccionar más información?
              1. Mostrar los resultados
              2. Seleccionar más información''')
            paso2 = input("Escribe el número correspondiente: ")
            
        if(paso2 == "1"):
            consulta = consulta + "FROM " + tabla + ";";
            try:
                with connection.cursor() as cursor:
                    cursor.execute(consulta)
                    print()
                    for row in cursor:
                        print(row)
                    print()
            finally:
                # Close connection.
                connection.close()
            sys.exit()



#TABLA GEN
    
if tabla == "2":
    tabla = "gen"
    print('''¿Qué quieres mostrar de la tabla de genes?
          1. Nombre
          2. Simbolo
          3. Localizacion
          4. Tipo
          5. Todo''')
    columna = input("Escribe el número correspondiente: ")
    
    if columna == "5":
        consulta = consulta + " * FROM " + tabla
        try:
            with connection.cursor() as cursor:
                cursor.execute(consulta + ";")
                print()
                for row in cursor:
                    print(row)
                print()
        finally:
            # Close connection.
            connection.close()
    else:    
        if columna == "1":
            consulta = consulta + " nombre "
        elif columna == "2":
            consulta = consulta + " simbolo "
        elif columna == "3":
            consulta = consulta + " localizacion "
        elif columna == "4":
            consulta = consulta + " tipo "
            try:
                with connection.cursor() as cursor:
                    cursor.execute(consulta)
                    print()
                    for row in cursor:
                        print(row)
                    print()
            finally:
                # Close connection.
                connection.close()
        
        print('''¿Quiere mostrar los resultados o seleccionar más información?
              1. Mostrar los resultados
              2. Seleccionar más información''')
        paso2 = input("Escribe el número correspondiente: ")
        
        while paso2 == "2":
            print('''¿Qué quieres mostrar de la tabla de genes?
              1. Nombre
              2. Simbolo
              3. Localizacion
              4. Tipo''')
            columna = input("Escribe el número correspondiente: ")
            if columna == "1":
                consulta = consulta + ", nombre "
            elif columna == "2":
                consulta = consulta + ", simbolo "
            elif columna == "3":
                consulta = consulta + ", localizacion "
            elif columna == "4":
                consulta = consulta + ", tipo "
            print('''¿Quiere mostrar los resultados o seleccionar más información?
              1. Mostrar los resultados
              2. Seleccionar más información''')
            paso2 = input("Escribe el número correspondiente: ")
            
        if(paso2 == "1"):
            consulta = consulta + "FROM " + tabla + ";";
            try:
                with connection.cursor() as cursor:
                    cursor.execute(consulta)
                    print()
                    for row in cursor:
                        print(row)
                    print()
            finally:
                # Close connection.
                connection.close()
        sys.exit()



#TABLA FENOTIPO

if tabla == "3":
    tabla = "fenotipo"
    print('''¿Qué quieres mostrar de la tabla de fenotipos?
          1. Id del fenotipo
          2. Frecuencia
          3. Nombre
          4. Criterio diagnóstico
          5. Todo
          ''')
    columna = input("Escribe el número correspondiente: ")
    if columna == "5":
        consulta = consulta + " * FROM " + tabla
        try:
            with connection.cursor() as cursor:
                cursor.execute(consulta + ";")
                print()
                for row in cursor:
                    print(row)
                print()
        finally:
            # Close connection.
            connection.close()
    else:
        if columna == "1":
            consulta = consulta + " fenotipo_id"
        elif columna == "2":
            consulta = consulta + " frecuencia"
        elif columna == "3":
            consulta = consulta + " nombre_fenotipo" 
        elif columna == "4":
            consulta = consulta + " criterio_diagnostico"
            try:
                with connection.cursor() as cursor:
                    cursor.execute(consulta+";")
                    print()
                    for row in cursor:
                        print(row)
                    print()
            finally:
                # Close connection.
                connection.close()
            
                
        print('''¿Quiere mostrar los resultados o seleccionar más información?
              1. Mostrar los resultados
              2. Seleccionar más información''')
        paso2 = input("Escribe el número correspondiente: ")
        
        while paso2 == "2":
            print('''¿Qué quieres mostrar de la tabla de fenotipos?
              1. Id del fenotipo
              2. Frecuencia
              3. Nombre
              4. Criterio diagnóstico
              ''')
            columna = input("Escribe el número correspondiente: ")
            if columna == "1":
                consulta = consulta + ", fenotipo_id"
            elif columna == "2":
                consulta = consulta + ", frecuencia"
            elif columna == "3":
                consulta = consulta + ", nombre_fenotipo" 
            elif columna == "4":
                 consulta = consulta + ", criterio_diagnostico"
            print('''¿Quiere mostrar los resultados o seleccionar más información?
              1. Mostrar los resultados
              2. Seleccionar más información''')
            paso2 = input("Escribe el número correspondiente: ")
            
        if(paso2 == "1"):
            consulta = consulta + " FROM " + tabla + ";";
            try:
                with connection.cursor() as cursor:
                    cursor.execute(consulta)
                    print()
                    for row in cursor:
                        print(row)
                    print()
            finally:
                # Close connection.
                connection.close()
        sys.exit()
            
if tabla == "4":
    consulta = consulta + " localizacion FROM localizacion;";
    try:
            with connection.cursor() as cursor:
                cursor.execute(consulta)
                print()
                for row in cursor:
                    print(row)
                print()
    finally:
            # Close connection.
            connection.close()
    sys.exit()
            
if tabla == "5":
    sys.exit()