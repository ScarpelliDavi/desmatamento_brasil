from pathlib import Path

import pandas as pd


# Caminhos do projeto
ROOT_DIR = Path(__file__).resolve().parent.parent

RAW_FILE = ROOT_DIR / "data" / "raw" / "desmatamento_prodes.csv"
PROCESSED_FILE = ROOT_DIR / "data" / "processed" / "desmatamento_tratado.csv"

ESTADOS = [
    "acre",
    "amazonas",
    "amapa",
    "maranhao",
    "mato_grosso",
    "para",
    "rondonia",
    "roraima",
    "tocantins"
]


def extract():

    df = pd.read_csv(RAW_FILE)

    return df


def transform(df):

    # trocar os nomes das colunas

    df = df.rename(columns={
        "referencia": "ano",
        "area_total_desmatamento": "area_total_desmatada"
    })

    # verificar se existem valores ausentes

    if df.isnull().values.any():
        raise ValueError("O dataset possui valores ausentes.")

    # verificar linhas duplicadas

    if df.duplicated().any():
        raise ValueError("O dataset possui linhas duplicadas.")

    # verificar valores negativos

    if (df[ESTADOS + ["area_total_desmatada"]] < 0).any().any():
        raise ValueError("O dataset possui valores negativos.")

    # verificar se o valor da soma dos estados realmente esta correta

    soma_estados = df[ESTADOS].sum(axis=1)

    if not soma_estados.equals(df["area_total_desmatada"]):
        raise ValueError(
            "A soma dos estados não corresponde ao total de desmatamento."
        )

    return df


def load(df):

    PROCESSED_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(
        PROCESSED_FILE,
        index=False
    )

    print(f"Arquivo tratado salvo em: {PROCESSED_FILE}")


def run_etl():

    df = extract()

    df = transform(df)

    load(df)


if __name__ == "__main__":
    run_etl()
