import datetime
from . import base


class CRLBaseChecker(base.Checker):
    """
    Класс написан для CRL, в дальнейшем возможно масштабирование и деление на 3 модуля CRL, MUC, ФИР
    """
    def __init__(self):
        pass

    def get_data(self, url=None):
        """
        Получает на вход url по которому статическим методом _downloand_crl_from_url
        извлекает cryptography.x509.Certificate Объект
        :param url:
        :return: возвращает 3 значения с инфой о Crl файле
        """
        crl = base.Checker._downloand_crl_from_url(url)
        # Рассчет дельты текущего времени и след обновления
        timedelta = crl.next_update - datetime.datetime.now()
        return crl.last_update, crl.next_update, timedelta

    def start(self):
        """
        Отправная точка работы логики бота
        :return: msg - строка содержащая сообщения для вывода в боте
        """
        msg = ''
        yam = base.Checker._config_from_yaml()  # собираем конфигурации
        checker1 = base.Checker()
        checker1.from_yaml_to_crl_memory(yam)  # передали словарь в чекер, чтоб он с ним уже работал
        for x in checker1.CRL_MEMORY:
            last_update, next_update, timedelta = self.get_data(x)
            msg += f"URL CRL {x} Последнее обновление {last_update.strftime('%d.%m.%y %H:%M:%S')} " \
                   f"\n Следующее обновление {next_update.strftime('%d.%m.%y %H:%M:%S')} " \
                   f"\n Оставшееся время действия {str(timedelta).split('.')[0]}" \
                   f"\n ---------------------------------------\n"
        checker1.CRL_MEMORY.clear()
        return msg
