from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome as WebDriver
from selenium.webdriver.remote.webelement import WebElement

class ElementsLocation:
    """Classe que será chamada para fazer a manipulaçao dos elementos das div's"""
    @classmethod
    def __wait_until(cls, drive:WebDriver, condition:EC, elements:By, tag:str) -> WebElement:
        """Retorna o elemento do Drive do HTML"""
        elemento = WebDriverWait(drive, 20).until(condition((elements, tag)))
        return elemento

    @classmethod
    def send_keys(cls, drive:WebDriver, elements:By, tag:str, value:str) -> None:
        """Função que busca a chave do elemento html"""
        elemento = cls.__wait_until(drive, EC.presence_of_element_located, elements, tag)
        elemento.send_keys(value)

    @classmethod
    def clear_and_send_keys(cls, drive:WebDriver, elements:By, tag:str, value:str) -> None:
        """Função que limpa o campo do elemento html e envia um novo valor"""
        elemento = cls.__wait_until(drive, EC.presence_of_element_located, elements, tag)
        elemento.clear()
        elemento.send_keys(value)

    # Função de Click's
    @classmethod
    def send_click(cls, drive:WebDriver, elements:By, tag:str) -> None:
        """Função que faz o click no elemento"""
        elemento = cls.__wait_until(drive, EC.presence_of_element_located, elements, tag)
        elemento.click()

    @classmethod
    def action_click(cls, drive:WebDriver, elements:By, tag:str) -> None:
        """Função que faz o click no elemento, aguardando o elemento esta presente"""
        elemento = cls.__wait_until(drive, EC.presence_of_element_located, elements, tag)
        ActionChains(drive).move_to_element(elemento).click().perform()

    @classmethod
    def visibility_click(cls, drive:WebDriver, elements:By, tag:str) -> None:
        """Função que faz o click no elemento, aguardando o elemento esta presente"""
        elemento = cls.__wait_until(drive, EC.visibility_of_element_located, elements, tag)
        elemento.click()

    @classmethod
    def to_be_click(cls, drive:WebDriver, elements:By, tag:str) -> None:
        """Função que faz o click no elemento, na garantia de que o elemento esteja clicável antes de realizar a ação de clique"""
        elemento = cls.__wait_until(drive, EC.element_to_be_clickable, elements, tag)
        elemento.click()

######################################################################################################################################
    @classmethod
    def elements(cls, drive:WebDriver, elements:By, tag:str) -> WebElement:
        elemento = cls.__wait_until(drive, EC.presence_of_element_located, elements, tag)
        return elemento

    @classmethod
    def elements_not(cls, drive:WebDriver, elements:By, tag:str, visibility:bool=True) -> WebElement:
        condition = EC.visibility_of_element_located if visibility else EC.presence_of_element_located
        elemento = WebDriverWait(drive, 20).until_not(condition((elements, tag)))
        return elemento

    @classmethod
    def location_iframe(cls, drive:WebDriver, elements:By, tag:str) -> WebElement:
        """Função que localiza iframes"""
        elemento = cls.__wait_until(drive, EC.frame_to_be_available_and_switch_to_it, elements, tag)
        return elemento

    @classmethod
    def find_elements(cls, requisicao:WebDriver, by:By, tag_name:str) -> list[WebElement]:
        return requisicao.find_elements(by, tag_name)

    @classmethod
    def find_element(cls, requisicao:WebDriver, by:By, tag_name:str) -> WebElement:
        return requisicao.find_element(by, tag_name)

    @classmethod
    def get_attribute(cls, requisicao:WebElement, atributo_html:str) -> str:
        return requisicao.get_attribute(atributo_html)
