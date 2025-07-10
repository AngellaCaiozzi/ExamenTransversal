# modelo: marca / pantalla / RAM / disco / GB de DD / procesador / video
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'Integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'Integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
             'FS1230HD': ['Asus', 15.6, '8GB', 'SSD', '512GB', 'Intel Core i3', 'Integrada']
             }

# modelo: precio / stock
stock = {'8475HD': [387990, 10],
        '2175HD': [327990, 4],
        'JjfFHD': [424990, 1],
        'fgdxFHD': [664990, 21],
        'GF75HD': [749990, 2],
        '123FHD': [290890, 32],
        '342FHD': [444990, 7],
        'UWU131HD': [249990, 0],
        'FS1230HD': [249990, 0]
        }

def validarNum(tipo, txtIn, txtError, txtExep, vMin=None, vMax=None):
    while True:
        try:
            num = tipo(input(txtIn))
            if vMin != None and vMax != None:
                if num >= vMin and num <= vMax:
                    break
                else:
                    print(txtError)
            elif vMin != None:
                if vMin <= num:
                    break  
                else:
                    print(txtError)
            elif vMax != None:
                if vMax >= num:
                    break
                else:
                    print(txtError)
            else:
                break
        except:
            print(txtExep) 
    return num        

def stock_marca():
    contador = 0
    totalNote = 0
    marca = input('Ingrese la marca del Notebook que desea buscar: ').strip().lower()
    for clave, valor in productos.items():
        if marca == valor[0].lower():
            contador += 1
            totalNote += stock[clave][1]
    if contador != 0:
        print(f'Hay {contador} Notebooks de la marca {marca.upper()}') 
        for clave, valor in productos.items():
            if marca == valor[0].lower():
                print(f'Modelo: {clave} - {productos[clave]}')
    if totalNote != 0:
        print(f'Hay {totalNote} notebooks en stock de {marca.upper()}')
    else:
        print(f'No tenemos disponibles Notebooks de la marca {marca.upper()}')    

def busqueda_precio():
    encontrado = False
    p_min = validarNum(int,'Ingrese precio (mínimo): $','Precio debe ser mayor a CERO','Precio debe ser un número entero',0)
    p_max = validarNum(int,'Ingrese un precio (máximo): $','Precio debe ser mayor a' +str(p_min),'Precios debe ser un número entero',p_min)
    for clave, valor in stock.items():
        if valor[0] >= p_min and valor[0] <= p_max:
            print(f'Valor Notebook: {productos[clave][0]}--{clave}: ${valor[0]}')
            encontrado = True
    if not encontrado:
        print('No se encontraron Notebooks con ese rango de precio.')        

def actualizar_precio():                           
    while True:
        codigo = input('Ingrese código del producto: ').upper()
        if codigo in stock:
            break
        else:
            print('Código de producto NO Existe!!')
            return
    newPrecio = validarNum(int,'Ingrese Nuevo Precio: ','Precio debe ser mayor a CERO.','Precio debe ser un número entero',1)        
    stock[codigo][0] = newPrecio
    print('Precio Actualizado.')
    print('¿Desea continuar actualizando precios?')
    seguir = validarNum(int,'1.- Seguir actualizando precio.\n2.- Salir\n--> ','Opción NO existe.','Opción es un número',1,2)
    if seguir == 1:
        actualizar_precio()
    else:
        print('___Producto Actualizado___')
        print(f'PRECIO: ${stock[codigo][0]} - NOTEBOOK: {productos[codigo][0]}')
        return  
            
def menu():
    while True:
        print("""\n***** MENÚ PYBOOKS *****
            1. Stock de la Marca.
            2. Búsqueda por Precio.
            3. Actualizar Precio    
            4. Salir    
              """)
        op = input('Ingrese una opción: ')
        if op == '1': 
            print('__STOCK x Marca__') 
            stock_marca()
        elif op == '2':
            print('__BUSCAR x PRECIO__') 
            busqueda_precio()
        elif op == '3':
            print('__ACTUALIZAR PRECIO__') 
            actualizar_precio()  
        elif op == '4':
            print('Saliendo...')
            print('Programa Finalizado!!!')
            break
        else:
            print('OPCIÓN NO VÁLIDA')
            
menu()