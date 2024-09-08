from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from selenium.webdriver import Chrome as WebDriver

from scraping.utils.LoadPG import LoadPG
from modulos.Logs import MyLogger
# formExpedientes:tbExpedientes:scPendentes_table
# formAcervo:tbProcessos:scPendentes_table
class Paginacao:
    """
    Classe que manipula o controle de paginação do scrapping
    :params log_name: Variavel String que recebe o nome do log a ser identificado no log em execução
    """
    def __init__(self, browser:WebDriver, log_name: str, id_paginacao:str):
        self.logger = self.logger = MyLogger(log_name)
        self.__log_name = log_name
        self.__browser = browser
        self.__tag_name = 'td'
        self.__id_paginacao = id_paginacao

    def label_paginacao(self, cont: int) -> bool:
        """
        Função que localiza os elementos da paginação de cada caixa e vai mudando de acordo com os eventos.
        :params browser: Variavel que recebe o drive
        :params cont: Variavel que recebe o contador das paginas em execução
        :return : Retorna valor booleano, se False= continua a paginação; se True= interrompa a paginação e volta para a primeira pagina
        """
        self.logger.log_info('Localizando paginação...')
        try:
            menu_paginacao = self.__browser.find_element(By.ID, self.__id_paginacao)
            botoes_paginacao = menu_paginacao.find_elements(By.TAG_NAME, self.__tag_name)
            botao_first_page = botoes_paginacao[0]  # O botão de primeira página é o primeiro
            botao_next = botoes_paginacao[-2]  # O botão da proxima página

            if 'dsbld' not in botao_next.get_attribute('class'):
                self.logger.log_info(f'Clicando na pagina {cont+1}...')
                botao_next.click()  # Clica no botão da proxima página
                load_pg = LoadPG(self.__log_name).load_pg(self.__browser)
                return True
            self.logger.log_info('Voltando para a primeira pagina!!')
            botao_first_page.click()  # Clica no botão de primeira página
            load_pg = LoadPG(self.__log_name).load_pg(self.__browser)
        except Exception:  # Se de erro, continua paginação
            self.logger.log_error('##Paginacao.label_paginacao.Exception>label_paginacao## - Não possui paginação, continuando...')
        return False

    def validar_first_page(self) -> bool:
        """
        Função que ao entrar na caixa de processos, localiza os elementos da paginação de cada caixa e validar inicia na primeira paginação, se não clica na primeira.
        :params browser: Variavel que recebe o drive
        """
        self.logger.log_info('Identificando paginação...')
        try:
            menu_paginacao = self.__browser.find_element(By.ID, self.__id_paginacao)
            botoes_paginacao = menu_paginacao.find_elements(By.TAG_NAME, self.__tag_name)
            botao_first_page = botoes_paginacao[0]  # O botão de primeira página é o primeiro

            if 'dsbld' not in botao_first_page.get_attribute('class'):
                self.logger.log_info('Voltando para a primeira pagina!!')
                botao_first_page.click()  # Clica no botão de primeira página
                load_pg = LoadPG(self.__log_name).load_pg(self.__browser)
        except Exception:  # Se de erro, continua paginação
            self.logger.log_error('##Paginacao.validar_first_page.Exception## - Não identificado a primeira paginação')
        return True
