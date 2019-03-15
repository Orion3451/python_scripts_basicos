'''def halve_evens_only(nums):
    return [i/2 for i in nums if not i % 2]
numeros = [1,2,3,4,5,6,7,8,9,0,67,34,234,34,2,2,2]
resultado = halve_evens_only(numeros)'''
def animal(nombre):
    if nombre == 'Rigoberto':
        print ('Se llama --> {}'.format(nombre))
        mensaje = 'Tiene hambre'
        return mensaje
    elif nombre == 'Pupi':
        print ('Se llama -->{}'.format(nombre))
        mensaje = 'Esta dormido'
        return mensaje
    else:
        mensaje = 'No se encuentra el nombre'
        return mensaje

nombre = 'Pupi'
mostrar_animal = animal(nombre)
print (mostrar_animal)
