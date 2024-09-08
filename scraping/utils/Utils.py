from socket import socket

class Utils:
    @classmethod
    def get_free_port(cls) -> int:
        """
        Retorna uma porta livre
        :return: Porta livre
        """
        with socket() as sock:
            sock.bind(('', 0))
            return sock.getsockname()[1]
