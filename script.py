import warnings
from pprint import pprint

import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

XLSX_ENGINE = 'openpyxl'
XLSX_FILE_INPUT = 'Dados.xlsx'
DATE_COLUMN = 'Data'
SALES_COLUMN = 'Vendas'
STEPS = 5

warnings.filterwarnings('ignore')


def get_input_data_frame():
    data_frame = pd.read_excel(XLSX_FILE_INPUT, engine=XLSX_ENGINE)
    data_frame.set_index(DATE_COLUMN, inplace=True)
    return data_frame


def get_forecast(data_frame):
    model = ARIMA(data_frame[SALES_COLUMN], order=(6,1,1))
    model_fit = model.fit()
    return model_fit.forecast(steps=STEPS)


def run():
    df = get_input_data_frame()
    forecast = get_forecast(df)
    df_forecast = pd.DataFrame(forecast).reset_index()
    df_forecast.columns = [DATE_COLUMN, SALES_COLUMN]
    df_forecast = pd.DataFrame(
        {
            DATE_COLUMN: forecast.index,
            SALES_COLUMN: forecast.values
        }
    )
    df_forecast.set_index(DATE_COLUMN, inplace=True)
    results = pd.concat([df, df_forecast])
    results[SALES_COLUMN] = results[SALES_COLUMN].astype(int)
    pprint(results)  


if __name__ == '__main__':
    run()
