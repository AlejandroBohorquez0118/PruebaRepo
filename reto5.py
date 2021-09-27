#Definir diccionario
tienda = {'codigo': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], 'nombre': ['Tangelos', 'Limones', 'Peras', 'Arandanos', 'Tomates', 'Fresas', 'Helado', 'Galletas', 'Chocolate', 'Jamon'], 'precio': [9000.0, 2500.0, 2700.0, 9300.0, 8100.0, 9100.0, 4500.0, 700.0, 4500.0, 11000.0], 'inventario': [67, 35, 65, 34, 42, 90, 41, 18, 80, 55]}

codigo2 = []
nombre2 = []
precio2 = []
inventario2 = []

#contadores


i = 0
poi = 0
poi2 = 0
poi6 = 9999999
poi8 = 0
poi11= 0



codigo = tienda.get('codigo')

#Definir entrada
sol = input()
op1 = 'ACTUALIZAR'
op2 = 'BORRAR'
op3 = 'AGREGAR'

#Codigo Actualizar

if sol == op1:
    codigo = tienda.get('codigo')
    compa = " ".join(codigo)
    dato1, dato2, dato3, dato4 = input().split()
    dato3 = float(dato3)
    dato4 = int(dato4)
    
    compa2 = compa.count(dato1)
    if compa2 == 1:
        dato1 = int(dato1)
        datof = dato1 - 1
        nombre = tienda.get('nombre')
        precio = tienda.get('precio')
        inventario = tienda.get('inventario')
        nombre[datof] = dato2
        precio[datof] = dato3
        inventario[datof] = dato4
        tienda.update({'nombre': nombre})
        tienda.update({'precio': precio})
        tienda.update({'inventario': inventario})
        
        poi3 = tienda.get('precio')
        poi4 = tienda.get('nombre')
        poi10 = tienda.get('inventario')


      #mayor precio
        for i in range(len(poi3)):
            if poi2 < poi3[i]:
                poi2 = poi3[i]
                poi5     = poi4[i]
        #menor precio
        for i in range(len(poi3)):
            if poi6 > poi3[i]:
                poi6 = poi3[i]
                poi7 = poi4[i]
        #promedio
        for i in range(len(poi3)):
            poi8 += poi3[i]
        
        poi9 = poi8 / len(poi3)

        #inventario
        for i in range(len(poi3)):
        
            poi11 += (poi3[i] * poi10[i])

        print(poi5, poi7, poi9, poi11)
        
    
    else:
        print('ERROR')

#Codigo Borrar

if sol == op2:
    dato1, dato2, dato3, dato4 = input().split()
    dato3 = float(dato3)
    dato4 = int(dato4)
    codigo = tienda.get('codigo')
    compa = " ".join(codigo)
    compa2 = compa.count(dato1)
    if compa2 == 1:
        dato1 = int(dato1)
        datof = dato1 - 1
        nombre = tienda.get('nombre')
        precio = tienda.get('precio')
        inventario = tienda.get('inventario')
        codigo2.extend(codigo)
        nombre2.extend(nombre)
        precio2.extend(precio)
        inventario2.extend(inventario)

        codigo2.remove(codigo2[datof])
        nombre2.remove(nombre2[datof])
        precio2.remove(precio2[datof])
        inventario2.remove(inventario2[datof])

        for i in range(len(codigo2)):
            codigo2[i] = int(codigo2[i])

        for i in range(1 , len(codigo2)):
            
            if  i == codigo2[i] - 1:
                pass
            else:
                codigo2[i]= codigo2[i] - 1
                pass
            
        tienda.update({'codigo': codigo2})
        tienda.update({'nombre': nombre2})
        tienda.update({'precio': precio2})
        tienda.update({'inventario': inventario2})

        poi3 = tienda.get('precio')
        poi4 = tienda.get('nombre')
        poi10 = tienda.get('inventario')


        #mayor precio
        for i in range(len(poi3)):
            if poi2 < poi3[i]:
                poi2 = poi3[i]
                poi5     = poi4[i]
        #menor precio
        for i in range(len(poi3)):
            if poi6 > poi3[i]:
                poi6 = poi3[i]
                poi7 = poi4[i]
        #promedio
        for i in range(len(poi3)):
            poi8 += poi3[i]
        
        poi9 = poi8 / len(poi3)

        #inventario
        for i in range(len(poi3)):
        
            poi11 += (poi3[i] * poi10[i])
        poi12 = round(poi9,1)
        print(poi5, poi7, poi12, poi11)
        

    else:
        print('ERROR')

#Codigo Agregar
codigo = []
nombre = []
precio = []
inventario = []


if sol == op3:
 dato1, dato2, dato3, dato4 = input().split()
 codigo = tienda.get('codigo')
 compa = " ".join(codigo)
 compa2 = compa.count(dato1)
 if compa2 == 0:
    
    nombre = tienda.get('nombre')
    
    precio = tienda.get('precio')
    
    inventario = tienda.get('inventario')
    
    
    codigo2.extend(codigo)
    nombre2.extend(nombre)
    precio2.extend(precio)
    inventario2.extend(inventario)

    codigo2.append(dato1)
    nombre2.append(dato2)
    precio2.append(dato3)
    inventario2.append(dato4) 

    tienda.update({"codigo": codigo2})
    tienda.update({"nombre": nombre2})
    tienda.update({"precio": precio2})
    tienda.update({"inventario": inventario2})

    poi3 = tienda.get('precio')
    poi4 = tienda.get('nombre')
    poi10 = tienda.get('inventario')

    for i in range(len(poi3)):
            poi3[i] = float(poi3[i])
    for i in range(len(poi10)):
            poi10[i] = int(poi10[i])

    #mayor precio
    for i in range(len(poi3)):
            
        if poi2 < poi3[i]:
            poi2 = poi3[i]
            poi5     = poi4[i]
    
    #menor precio
    for i in range(len(poi3)):
        if poi6 > poi3[i]:
            poi6 = poi3[i]
            poi7 = poi4[i]
    #promedio
    for i in range(len(poi3)):
        poi8 += poi3[i]
        
    poi9 = poi8 / len(poi3)

    #inventario
    for i in range(len(poi3)):
        
        poi11 += (poi3[i] * poi10[i])

    poi12 = round(poi9,1)
    print(poi5, poi7, poi12, poi11)
 else:
     print('ERROR')    

