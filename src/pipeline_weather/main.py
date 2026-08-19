from dotenv import load_dotenv
from pathlib import Path
env_path = Path(__file__).resolve().parent.parent / 'config' / '.env'
load_dotenv(env_path)


from pipeline_weather.extract_data import extract_weather_data
from pipeline_weather.transform_data import data_transformations
from pipeline_weather.load_data import load_weather_data

import os

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

env_path = Path(__file__).resolve().parent.parent.parent / 'config' / '.env'
load_dotenv(env_path)

API_KEY = os.getenv('API_KEY')

url = f'https://api.openweathermap.org/data/2.5/weather?q=Sao Paulo,BR&units=metric&appid={API_KEY}'
table_name = 'sp_weather'

def pipeline():
    try:
        logging.info("ETAPA 1: Extração de dados")
        data = extract_weather_data(url)

        logging.info("ETAPA 2: Transformação de dados")
        df = data_transformations(data)

        logging.info("ETAPA 3: Carregamento de dados")
        load_weather_data(table_name, df)

        logging.info("Pipeline concluído com sucesso!")

        print("\n" + "="*60)
        print("Pipeline concluído com sucesso!")
        print("="*60)

    except Exception as e:
        logging.error(f"Erro na execução do pipeline: {e}")
        import traceback
        traceback.print_exc()

pipeline()