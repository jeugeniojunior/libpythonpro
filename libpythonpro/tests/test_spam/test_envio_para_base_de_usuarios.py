import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Renzo', email='renzo@pythonpro.com.br'),
            Usuario(nome='Junior', email='renzo@pythonpro.com.br')
        ],
        [
            Usuario(nome='Renzo', email='renzo@pythonpro.com.br'),
        ]

    ]

)

def test_qde_de_span(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_email(
        'jeugenio.junior@gmail.com',
        'Curso de culinaria Merendinha-JF',
        'Primeira turma do curso de culinária do Merendinha-JF'
    )
    assert len(usuarios) == enviador.qtd_email_enviados


class EnviadorMock(Enviador):

    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


def test_parametros_de_span(sessao):
    usuario = Usuario(nome='Renzo', email='renzo@pythonpro.com.br')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_email(
        'jeugenio.junior@gmail.com',
        'Curso de culinaria Merendinha-JF',
        'Primeira turma do curso de culinária do Merendinha-JF'
    )
    assert enviador.parametros_de_envio == (
        'jeugenio.junior@gmail.com',
        'renzo@pythonpro.com.br',
        'Curso de culinaria Merendinha-JF',
        'Primeira turma do curso de culinária do Merendinha-JF'

    )