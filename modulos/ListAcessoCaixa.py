import re
from selenium.webdriver.common.by import By
from selenium.common import TimeoutException, StaleElementReferenceException
from selenium.webdriver import Chrome as WebDriver

from scraping.utils.ElementsLocation import ElementsLocation
from modulos.Logs import MyLogger

class ListAcessoCaixa:
    """Classe que obtem a lista dos processo
    :array_text_processos: Lista com os processos da pagina
    :array_id_processos: Lista com os id para acesso a timeline dos processos
    """
    def __init__(self, browser:WebDriver, log_name:str, id_processo:str):
        self.div_location = ElementsLocation.elements(browser, By.ID, id_processo)
        self.logger = MyLogger(log_name)

    @classmethod
    def regex_processo(self, string:str) -> str:
        return re.sub('[^0-9]', '', string)

    def list_text_processos(self, class_name:str) -> list[str]:
        """Função que Obtem o text dos processos ja formatando os numeros"""
        array_processos:list[str] = []
        self.logger.log_info('Obtendo lista dos id dos processo!!')
        try:
            atributo_location = ElementsLocation.find_elements(self.div_location, By.CLASS_NAME, class_name)

            for i in range(len(atributo_location)):
                try:
                    processo = self.regex_processo(atributo_location[i].text)
                    array_processos.append(processo)
                except TimeoutException as erT:
                    self.logger.log_warning(f'ListAcessoProcesso.list_text_processos.for.TimeoutException\n{erT}')
                    pass
                except StaleElementReferenceException as erSER:
                    self.logger.log_warning(f'ListAcessoProcesso.list_text_processos.for.StaleElementReferenceException\n{erSER}')
                    pass

            return array_processos
        except TimeoutException as e:
            self.logger.log_warning(f'##ListAcessoProcesso.list_text_processos.TimeoutException###########\n{e}')
            return array_processos
        except Exception as er: ## Verifica outras excessoes e passa!!
            self.logger.log_error(f'##ListAcessoProcesso.list_text_processos.Exception>##\n{er}')
            return array_processos

    def list_text_aviso(self, xpath:str) -> list[str]:
        """Função que Obtem o text dos processos ja formatando os numeros"""
        array_avisos:list[str] = []
        self.logger.log_info('Obtendo lista dos id dos processo!!')
        try:
            atributo_location = ElementsLocation.find_elements(self.div_location, By.XPATH, xpath)

            for i in range(len(atributo_location)):
                try:
                    processo = self.regex_processo(atributo_location[i].text)
                    array_avisos.append(processo)
                except TimeoutException as erT:
                    self.logger.log_warning(f'ListAcessoProcesso.list_text_aviso.for.TimeoutException\n{erT}')
                    pass
                except StaleElementReferenceException as erSER:
                    self.logger.log_warning(f'ListAcessoProcesso.list_text_aviso.for.StaleElementReferenceException\n{erSER}')
                    pass

            return array_avisos
        except TimeoutException as e:
            self.logger.log_warning(f'##ListAcessoProcesso.list_text_aviso.TimeoutException###########\n{e}')
            return array_avisos
        except Exception as er: ## Verifica outras excessoes e passa!!
            self.logger.log_error(f'##ListAcessoProcesso.list_text_aviso.Exception>##\n{er}')
            return array_avisos
