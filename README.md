# Graficos de ADRs Argentinos
Graficador de contizaciones de de ADRs de Argentina funciona obteniendo datos desde yahoo finance. 
Las especies a trabajar se encuentran listadas en el archivo "ADR_Argentina.xlsx", y las fechas definidas inician en enero del 2021 hasta la fecha del día en que se ejecuta el script.

## Dependencias
Para evitar errores se recomienda tener instaladas las siguientes librerias
- pandas_datareader
- mplfinance

## Gráficos 
Los datos obtenidos son de frecuencia diaria, con un grafico de ventas y volumen de monto operado. 

Las medias moviles usadas en los gráficos son la de 3, 6, 9 y 30 días. Las primeras tres para seguir movimiento de corto plazo, mientras que la media movil de 30 días se toma como parametro limite de posición en el instrumento, como regla no se tiene posición si las cotizaciones se encuentran por debajo de dicho indicador.

## Datos
Se guardan los datos de las especies en un archivo individual


