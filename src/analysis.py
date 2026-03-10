import pandas as pd


def churn_distribution(df):

    churn_counts = df["Churn"].value_counts()
    churn_percent = df["Churn"].value_counts(normalize=True) * 100

    return churn_counts, churn_percent


def churn_by_contract(df):

    return pd.crosstab(df["Contract"], df["Churn"], normalize="index") * 100


def churn_by_payment(df):

    return pd.crosstab(df["PaymentMethod"], df["Churn"], normalize="index") * 100


def churn_by_internet(df):

    return pd.crosstab(df["InternetService"], df["Churn"], normalize="index") * 100


def churn_by_tenure(df):

    return df.groupby("Churn")["tenure"].mean()


def charges_analysis(df):

    return df.groupby("Churn")[["Charges.Monthly", "Charges.Total"]].mean()