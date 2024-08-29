from dotenv import load_dotenv
import os
import time
from selenium.webdriver import Chrome as WebDriver
from selenium.webdriver.common.by import By
from selenium.common import TimeoutException

from scraping.utils.Drive import CreateDrive
from scraping.utils.ElementsLocation import ElementsLocation
from modulos.Logs import MyLogger

from scraping.utils.Utils import Utils

class StartPanel:
    def __init__(self, log_name:str, folder:str, rodar_background:bool) -> None:
        """Classe principal que ira iniciar o scrapping.
        :params painel_url: Variavel que passa a url do acervo ao acessar PJE.
        :params log_name: Variavel que ira determina o nome do arquivo que ira receber o log do processo.
        :params rodar_background: Variavel Booleana que determina o tipo de scrapping, `False` para Tela e True para rodar em backgroud.
        """
        load_dotenv()
        self.logger = MyLogger(log_name=log_name, folder=folder)
        self.debug_port:int = Utils.get_free_port()
        self.url = os.environ.get("URL")

        self.logger.log_info('Construindo driver...')
        self.__drive:WebDriver = CreateDrive(headless=rodar_background, debug_port=self.debug_port).create_drive() # Chama a classe ira criar o drive de conexão

    def __refresh_browser(self) -> None:
        """Função que da refresh no browser"""
        self.logger.log_info('Refresh Navegador...')
        self.__drive.refresh()
        time.sleep(3)

    def current_url(self) -> str:
        """Função exporta a url atual"""
        return self.__drive.current_url

    def get_browser(self) -> WebDriver:
        """Função que exporta o drive do browser"""
        return self.__drive

    def quit(self) -> None:
        """Função que Encerra o Driver"""
        self.logger.log_info('Encerrando Navegador')
        self.__drive.quit()

    def start_project(self) -> None:
        """Função que entra e faz o login no pje"""
        self.logger.log_info('Entrando no site do DER!!')
        self.__drive.get(self.url)

        list_lines:list[str] = []
        time.sleep(10)
        self.logger.log_info('Localizando as linhas...')
        # //*[@id="form:tabview:campoBusca"]/button
        ElementsLocation.send_click(self.__drive, By.XPATH, '//*[@id="form:tabview:campoBusca"]/button')
        div_pesquisar = ElementsLocation.elements(self.__drive, By.XPATH, '//*[@id="form:tabview:campoBusca_panel"]/table/tbody')
        location_lines = ElementsLocation.find_elements(div_pesquisar, By.TAG_NAME, 'tr')
        if len(location_lines) > 0:
            for line in location_lines:
                text = line.text
                print(text)
                list_lines.append(text)

        input('Enter p/continuar...')
        self.quit()
