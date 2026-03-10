import pandas as pd


def clean_data(df):

    # reemplazar espacios vacíos
    df["Charges.Total"] = df["Charges.Total"].replace(" ", None)

    # convertir a número
    df["Charges.Total"] = pd.to_numeric(df["Charges.Total"], errors="coerce")

    # rellenar nulos
    df["Charges.Total"] = df["Charges.Total"].fillna(df["Charges.Total"].median())

    # convertir SeniorCitizen a texto
    df["SeniorCitizen"] = df["SeniorCitizen"].replace({1: "Yes", 0: "No"})

    return df