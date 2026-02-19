import os
import zipfile
from dotenv import load_dotenv # Importa a biblioteca

# Carrega as variáveis do arquivo .env para o ambiente
load_dotenv()

def download_kaggle_dataset(dataset_name, path='./data'):
    if not os.path.exists(path):
        os.makedirs(path)
    
    # O Kaggle busca automaticamente por 'KAGGLE_USERNAME' e 'KAGGLE_KEY' no ambiente
    print(f"Iniciando download do dataset: {dataset_name}...")
    
    status = os.system(f'kaggle competitions download -c {dataset_name} -p {path}')
    
    if status == 0:
        zip_path = os.path.join(path, f'{dataset_name}.zip')
        if os.path.exists(zip_path):
            print("Descompactando arquivos...")
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(path)
            os.remove(zip_path)
            print("Download e extração concluídos!")
    else:
        print("Erro no download. Verifique se o .env está correto e se aceitou as regras no site.")

download_kaggle_dataset('ieee-fraud-detection')