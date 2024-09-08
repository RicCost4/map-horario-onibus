import logging
import os

class MyLogger:
    logger_initialized = False

    @classmethod
    def initialize_logger(cls, log_level:int, folder:str):
        if not cls.logger_initialized:
            cls.logger_initialized = True
            cls.logger = logging.getLogger()
            cls.logger.setLevel(log_level)
            console_handler = logging.StreamHandler()
            console_handler.setLevel(log_level)
            console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
            console_handler.setFormatter(console_formatter)
            cls.logger.addHandler(console_handler)

            cls.file_handlers = {}
            cls.log_folder = folder if folder != None else 'logs'

    def __init__(self, log_name: str, folder:str = None, initialized:bool = False, log_level=logging.INFO):
        # Configurar nova instancia de log se necessario.
        if initialized:
            self.logger_initialized = False

        self.log_name = log_name
        self.initialize_logger(log_level, folder)

        # Configuração do arquivo de log para cada nível, se ainda não existir.
        for level in [logging.INFO]:
            if level not in self.__class__.file_handlers:
                self._setup_file_handler(level)

    def _setup_file_handler(self, log_level):
        log_file = os.path.join(self.__class__.log_folder, f"{self.log_name}.log")
        handler = logging.FileHandler(log_file, mode='a', encoding='utf-8')
        handler.setLevel(log_level)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.__class__.file_handlers[log_level] = handler

    def log_debug(self, message):
        """Função que instancia o log_level a nível debug"""
        self.logger.debug(f'{self.log_name}: {message}\n==========')

    def log_info(self, message):
        """Função que instancia o log_level a nível info"""
        self.logger.info(f'{self.log_name}: {message}\n==========')

    def log_warning(self, message):
        """Função que instancia o log_level a nível warning"""
        self.logger.warning(f'{self.log_name}: {message}\n==========')

    def log_error(self, message):
        """Função que instancia o log_level a nível error"""
        self.logger.error(f'{self.log_name}: {message}\n==========')

    def log_critical(self, message):
        """Função que instancia o log_level a nível critical"""
        self.logger.critical(f'{self.log_name}: {message}\n==========')