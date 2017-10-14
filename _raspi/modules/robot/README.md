#escritura de varias bobinas
En este caso el procedimiento es un tanto peculiar, pues se necesita mandar tantos bit's como bobinas queremos modificar, al trabajar sobre modbus las tramas van en bytes, lo que implica que al menos tendremos que mandar 1 byte aunque vayamos a modificar menos de 8 bobinas, ademas el manual del inversor nos dice que debemos mandar un numero de bytes par, por lo que tendremos que mandar, 2 bytes para escribir entre 1 y 16 bobinas y 4 bytes para escribir entre 17 y 32 bobinas. ademas la manera de mandar los valores de las bobinas es en el siguiente orden, el primer byte, las bobinas de la 1 a la 8, el segundo byte las bobinas de la 9 a la 16, el tercer byte las bobinas de la 17 a la 24 y en el cuarto byte las bobinas de la 25 a la 32. mandando en hexadecimal, el valor que representa en binario el estado que queremos fijar.
por tanto para finar el siguiente estado en las 8 primeras bobinas mandaremos

b10100010 b00000000
\x64      \x00

# La lectura y la escritura de numeros negativos
    Falta comprobar si es complemento a uno o complemento a dos...


# Lectura de un registo simple
tx ['\x01', '\x03', '\x16', '2', '\x00', '\x01', '!', '\x8d']

rx ['\x01', '\x03', '\x02', '\x00', '\x05', 'x', 'G']

# Lectura de dos registros simples

tx ['\x01', '\x03', '\x10', 'X', '\x00', '\x02', 'A', '\x18']

rx ['\x01', '\x03', '\x04', '\x00', '\x12', '\x00', '\x02', '\xdb', '\xf7']

# Escritura de un registro simple

tx ['\x01', '\x06', '\x16', '2', '\x00', '\x05', '\xec', 'N']
rx ['\x01', '\x06', '\x16', '2', '\x00', '\x05', '\xec', 'N']

# Escritura de 2 registros simples
 algo no funciona TO-DO



# Lectura de un registro Doble
tx ['\x01', '\x03', '\x12', 'N', '\x00', '\x02', '\xa1', 'd']

rx ['\x01', '\x03', '\x04', '\x00', '\x00', '\x08', '+', '\xbd', '\xec']

# Lectura de dos registros dobles
tx ['\x01', '\x03', '\x12', 'N', '\x00', '\x04', '!', 'f']

rx ['\x01', '\x03', '\x08', '\x00', '\x00', '\x08', '+', '\x00', '\x00', '\x00', '3', '\xf0', '\x8c']


# Escritura  de un registro doble
tx ['\x01', '\x10', '\x12', 'N', '\x00', '\x02', '\x04', '\x00', '\x00', '\x13', '$', '\xaf', '\x98']

rx ['\x01', '\x10', '\x12', 'N', '\x00', '\x02', '$', '\xa7']


# Escritura de 2 registros dobles

algo no funciona TO-DO

# Comando enter
- El comando enter (0x0009) actua sobre todo lo que se haya cambiado en el inversor desde que se inicio este, o desde la ultima vez que se ejecuto dicho comando.
- En el caso de 0x9020 solo actua sobre la siguiente intrucción con código de función 0x06.

# escalado
   """TO-DO"""
