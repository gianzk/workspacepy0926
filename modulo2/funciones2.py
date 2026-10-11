def calculo_monto(monto,tasa=10):
    return monto*tasa/100
monto = float(input("ingrese el monto"))
score= float(input("ingrese su score financiero"))

if score >0:
    if score >1 and score <2:
        tasa_default= 5
        monto_impuesto = calculo_monto(monto,tasa_default)
    elif score <3:
        tasa_default=8
        monto_impuesto = calculo_monto(monto,tasa_default)
    else:
        monto_impuesto = calculo_monto(monto)

print(f"el monto es",monto_impuesto)

