import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome as WebDriver

from scraping.utils.ElementsLocation import ElementsLocation
from modulos.Logs import MyLogger

class LoadPG:
    def __init__(self, log_file:str):
        load_dotenv()
        self.logger = MyLogger(log_file)
        self.base_url = os.environ.get("BASE_URL_PJE")

    def load_pg(self, browser:WebDriver) -> bool:
        """Função que ira fazer o tratamento da tela de carregamento"""
        self.logger.log_info('Tela de load...')
        # Espera a pesquisa carregar
        carregou_resultados: bool = False
        sucesso: bool = False
        while not carregou_resultados:
            # Verifica se o style do span que aparece o carregamento mudou, ele fica vazio quando carrega
            try:
                elements = ElementsLocation.elements(browser, By.XPATH, '//*[@id="_viewRoot:status.start"]')
                if elements.get_attribute('style') != '':
                    self.logger.log_info('saindo da Tela de load')
                    carregou_resultados = True
                    sucesso = True
            except Exception as e:  # Se não encontrou o elemento, da refresh na página
                self.logger.log_warning(f'##Exception>load_pg()##\n{e}')
                browser.refresh()
                if self.base_url in browser.current_url:  # Se ta na tela de login sair do loop (ela não tem o elemento)
                    carregou_resultados = True

        return sucesso
