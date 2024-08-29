from dotenv import load_dotenv
import os
import time
from typing import Tuple
from selenium.webdriver import Chrome as WebDriver
from selenium.webdriver.common.by import By

from scraping.utils.Drive import CreateDrive
from scraping.utils.ElementsLocation import ElementsLocation
from modulos.Logs import MyLogger

from scraping.utils.Utils import Utils

class StartPanel:
    def __init__(self, log_name:str, folder:str, rodar_background:bool) -> None:
        """Classe principal que ira iniciar o scrapping."""
        load_dotenv()
        self.logger = MyLogger(log_name=log_name, folder=folder)
        self.debug_port:int = Utils.get_free_port()
        self.url = os.environ.get("URL")
        self.__background = rodar_background

    def __refresh_browser(self, drive:WebDriver, seconds:int = 3) -> None:
        """Função que da refresh no browser"""
        self.logger.log_info('Refresh Navegador...')
        drive.refresh()
        time.sleep(seconds)

    def __quit(self, drive:WebDriver, mensage:str) -> None:
        """Função que Encerra o Driver"""
        self.logger.log_info(mensage)
        drive.quit()

    def __get_list_lines(self) -> list[str]:
        lists = []
        self.logger.log_info('Obtendo Lista das linhas...')
        self.logger.log_info('Criando o DRIVE')
        driver = CreateDrive(headless=self.__background, debug_port=self.debug_port).create_drive()
        self.logger.log_info('Entrando no site do DER!!')
        driver.get(self.url)

        time.sleep(5)
        self.logger.log_info('Localizando as linhas...')
        ElementsLocation.send_click(driver, By.XPATH, '//*[@id="form:tabview:campoBusca"]/button')
        div_pesquisar = ElementsLocation.elements(driver, By.XPATH, '//*[@id="form:tabview:campoBusca_panel"]/table/tbody')
        location_lines = ElementsLocation.find_elements(div_pesquisar, By.TAG_NAME, 'tr')
        if len(location_lines) > 0:
            for line in location_lines:
                text = line.text
                lists.append(text)

        self.__quit(drive=driver, mensage='Fim do processo atual, Encerrando o Driver.')
        return lists

    def __get_process_schedules(self, list_lines:list[str], counter:int) -> Tuple[bool, int]:
        """Função que entra e faz o login no pje"""
        self.logger.log_info(f'Obtendo acesso as linhas...')
        self.logger.log_info('Criando o DRIVE novamente')
        driver = CreateDrive(headless=self.__background, debug_port=self.debug_port).create_drive()
        self.logger.log_info('Entrando novamente no site do DER!!')
        driver.get(self.url)
        time.sleep(5)

        while True:
            text_line = list_lines[counter]
            self.logger.log_info(f'Obtendo dados da linha: {text_line}')
            time.sleep(2)
            # Inserir a linha na busca
            ElementsLocation.clear_and_send_keys(driver, By.ID, "form:tabview:campoBusca_input", text_line)
            time.sleep(2)
            # Selecionar a busca
            ElementsLocation.send_click(driver, By.ID, "form:tabview:campoBusca_panel")
            time.sleep(2)
            # btn_localizar
            ElementsLocation.send_click(driver, By.NAME, "form:tabview:j_idt20")

            time.sleep(5)
            driver.get(self.url)
            self.__refresh_browser(drive=driver)

            if counter == len(list_lines):
                self.__quit(drive=driver, mensage='Fim do processo atual, Encerrando a coleta.')
                return [False, counter]
            if counter % 4 == 0 and counter != 0:
                self.__quit(drive=driver, mensage='Fim do processo atual, Reiniciando o Driver.')
                return [True, counter]
            counter += 1

    def start_project(self) -> None:
        self.logger.log_info(f'Iniciando processo...')
        counter = 0
        restart = True
        list_lines = self.__get_list_lines()

        while restart:
            if len(list_lines) > 0:
                restart, counter = self.__get_process_schedules(list_lines, counter)
                counter += 1
        
        self.logger.log_info(f'Fim do processo, finalizando...')
