import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")


def plot_churn_distribution(df):

    plt.figure(figsize=(6,4))
    sns.countplot(x="Churn", data=df)

    plt.title("Distribución de Churn")
    plt.xlabel("Churn")
    plt.ylabel("Número de clientes")

    plt.show()


def plot_contract_churn(df):

    plt.figure(figsize=(8,5))
    sns.countplot(x="Contract", hue="Churn", data=df)

    plt.title("Churn por tipo de contrato")

    plt.show()


def plot_tenure(df):

    plt.figure(figsize=(8,5))
    sns.histplot(data=df, x="tenure", hue="Churn", bins=30)

    plt.title("Antigüedad del cliente vs Churn")

    plt.show()


def plot_monthly_charges(df):

    plt.figure(figsize=(8,5))
    sns.boxplot(x="Churn", y="Charges.Monthly", data=df)

    plt.title("Cargos mensuales vs Churn")

    plt.show()