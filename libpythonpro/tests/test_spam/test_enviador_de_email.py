from libpythonpro.tests.spam.enviador_de_email import Enviador
import pytest


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'destinatario',
    ['jeugenio.junior@gmail.com', 'merendinhajf@gmail.com']
)
def test_remetente(destinatario):
    enviador = Enviador()
    destinatarios = ['jeugenio.junior@gmail.com', 'merendinhajf@gmail.com']
    destinatario
    resultado = enviador.enviar(
        destinatario,
        'anareis.34@gmail.com',
        'Curso de culinaria Merendinha-JF',
        'Primeira turma do curso de culinária do Merendinha-JF'
    )
    assert destinatario in resultado