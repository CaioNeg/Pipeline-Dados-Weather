import os
import logging
from dotenv import load_dotenv

# Carrega o .env automaticamente da raiz do projeto
load_dotenv()


API_KEY = os.getenv('API_KEY')
print(f"--- TESTE: Minha API KEY é: {API_KEY} ---")

# Só DEPOIS de carregar o ambiente, importamos os módulos
from pipeline_weather.extract_data import extract_weather_data
from pipeline_weather.transform_data import data_transformations
from pipeline_weather.load_data import load_weather_data

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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

        print("\n" + "="*60)
        print("Pipeline concluído com sucesso!")
        print("="*60)

    except Exception as e:
        logging.error(f"Erro na execução do pipeline: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    pipeline()
    