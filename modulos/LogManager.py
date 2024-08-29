import os
from datetime import datetime
import shutil

class LogManager:
    def __init__(self, log_name:str, log_directory:str='logs'):
        self.__log_name_info = f'{log_name}-info'
        self.__log_name_erro = f'{log_name}-error'
        self.log_directory = log_directory

    def copy_logs(self) -> None:
        # Obter a data atual formatada
        current_date = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')

        # Definir os caminhos dos arquivos de log originais
        error_log_original = os.path.join(self.log_directory, f'{self.__log_name_erro}.log')
        info_log_original = os.path.join(self.log_directory, f'{self.__log_name_info}.log')

        # Definir os caminhos dos arquivos de log copiados
        error_log_copy = os.path.join(self.log_directory, f'{self.__log_name_erro}_{current_date}.log')
        info_log_copy = os.path.join(self.log_directory, f'{self.__log_name_info}_{current_date}.log')

        # Copiar os arquivos de log
        if os.path.exists(error_log_original):
            shutil.copy2(error_log_original, error_log_copy)
            # Esvaziar o arquivo original
            open(error_log_original, 'w').close()

        if os.path.exists(info_log_original):
            shutil.copy2(info_log_original, info_log_copy)
            # Esvaziar o arquivo original
            open(info_log_original, 'w').close()
