"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import datetime as dt
import pandas as pd
import re

def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    #
    # Inserte su código aquí
    #
    df = pd.read_csv('solicitudes_credito.csv', sep=';') # lectura del archivo

    df.drop(columns='Unnamed: 0', inplace=True) # eliminar la columna que lleva los mismos valores que el índice

     # convertir todos los valores de las columnas a minúsculas y corregir formato general
    for column in df.columns:
        if df[column].dtypes == object:
            df[column] = df[column].str.lower()
            df[column] = df[column].str.replace('-', ' ')
            df[column] = df[column].str.replace('_', ' ')

    # convertir los valores monetarios a un mismo formato
    df.monto_del_credito = df.monto_del_credito.str.replace(',', '')
    df.monto_del_credito = df.monto_del_credito.str.replace(r'\.00', '', regex=True)
    df.monto_del_credito = df.monto_del_credito.str.strip('$')
    df.monto_del_credito = df.monto_del_credito.str.strip()
    df.monto_del_credito = df.monto_del_credito.astype(int)

    # convertir la fecha al formato correcto
    df.fecha_de_beneficio = df.fecha_de_beneficio.apply(
        lambda x: dt.datetime.strptime(x, '%Y/%m/%d') 
        if re.match('^\d{4}\/', x) 
        else dt.datetime.strptime(x, '%d/%m/%Y')
    ) 

    df.drop_duplicates(inplace=True) # eliminar registros completamente duplicados
    df.dropna(inplace=True) # eliminar registros con valores NaN

    return df
