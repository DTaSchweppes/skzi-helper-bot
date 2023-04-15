import OpenSSL
import requests
import yaml


class Checker:
    """
    Базовый класс, в котором прописана отсновная логика Чекера сертификатов
    """
    modulename = 'WEB CRL'
    CRL_MEMORY = []
    CONFIGURATIONS: dict

    @staticmethod
    def _config_from_yaml(path_yaml_file="C:\\Users\\david\\PycharmProjects\\skzi-helper-bot\\setup.yaml"):  #
        # Прогрузить из yaml конфиги и вернуть dict
        """
        :param url: путь до Yaml файла
        :return: dict Yaml файла
        """
        with open(path_yaml_file, encoding="utf-8") as setup_file:
            CONFIGURATIONS = yaml.safe_load(setup_file)['WEB CRL']
        return CONFIGURATIONS

    def from_yaml_to_crl_memory(self, configurations):  # из yaml в словарь с url без возврата
        """Кладет в атрибут CRL_MEMORY (list) объекта Chacker конфиги из Yaml, отбирая от туда Только URL

        :param CONFIGURATIONS: конфиг из Yaml
        """
        for dates in configurations:
            self.CRL_MEMORY.append(dates['path'])

    @staticmethod
    def _downloand_crl_from_url(url):
        responce = requests.get(url)
        if responce.status_code != 200:
            return None
        cert = OpenSSL.crypto.load_crl(OpenSSL.crypto.FILETYPE_ASN1, responce.content)
        return cert.to_cryptography()
