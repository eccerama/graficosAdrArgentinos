from pandas_datareader.data import DataReader
from datetime import datetime
import mplfinance as mpf

def graficadorCortoPlazo(ticker = 'GOLD', start = datetime(2021,1,1), end = datetime.now()):


    '''Definiendo medias moviles'''
    mm1 = 3 #21 un mes
    mm2 = 6 #42 dos meses
    mm3 = 9 #252 un año
    mm4 = 30

    '''Obteniendo datos de yahoo finance'''
    df = DataReader(ticker,'yahoo',start,end)

    '''Configurando el grafico'''
    mc = mpf.make_marketcolors( up = 'tab:green', down = 'tab:red', wick = { 'up':'green' , 'down':'red' })

    s = mpf.make_mpf_style(base_mpl_style = 'seaborn',mavcolors = ['orange', 'green','blue', 'brown'],marketcolors = mc)
    
    df.to_excel(f'{ticker}.xlsx')

    #Guardando la imagen del plot
    mpf.plot( df, 
             type = 'candle', 
             style = s, 
             mav = (mm1,mm2,mm3,mm4), 
             title = ticker, 
             volume=True,
             savefig=ticker[0:4]
             )
    
    return df

if __name__ == '__main__':    
    
    import pandas as pd
    
    #leer lista de especies
    df = pd.read_excel("ADR_Argentina.xlsx")
    tickers = df['Symbol'].values

    for ticker in tickers:
        print(f'{ticker} ok!')
        graficadorCortoPlazo(ticker)