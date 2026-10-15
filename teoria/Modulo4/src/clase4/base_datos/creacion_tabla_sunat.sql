
/*Creo tabla sunat si esta no existe*/
CREATE TABLE IF NOT EXISTS sunat(
    fecha varchar(20),
    origen varchar(20),
    moneda varchar(20),
    compra varchar(20),
    venta varchar(20)
);