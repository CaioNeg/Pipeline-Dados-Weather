import requests
import json
from pathlib import Path

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

api_key = '58724fa6bc7afe1296ce1056ebeb7929'  # Replace with your actual API key
url = f'https://api.openweathermap.org/data/2.5/weather?q=Sao Paulo,BR&units=metric&appid={api_key}'

def extract_weather_data(url: str):
    response = requests.get(url)
    data = response.json()

    output_path = 'data/weather_data.json'
    output_dir = Path(output_path).parent
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w') as f:
        json.dump(data, f, indent=4)

    logging.info("arquivo salvo com sucesso em: %s", output_path)
    return data

extract_weather_data(url)