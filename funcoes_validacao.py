import re

def valid_number(number):
    """
    Verifica se um número de celular brasileiro é válido.
    """
    # Remove quaisquer caracteres não numéricos do número
    number = re.sub(r'\D', '', number)

    # Verifica se o número tem 11 dígitos (incluindo o DDD)
    if len(number) != 11:
        return False

    # Verifica se o primeiro dígito é 9
    if number[2] != '9':
        return False

    # Verifica se o DDD é válido
    ddd = number[:2]
    if ddd not in ['11', '12', '13', '14', '15', '16', '17', '18', '19',
                   '21', '22', '24', '27', '28', '31', '32', '33', '34',
                   '35', '37', '38', '41', '42', '43', '44', '45', '46',
                   '47', '48', '49', '51', '53', '54', '55']:
        return False

    # O número é válido
    return True

def cpf_valido(cpf):
    """
    Verifica se um CPF é válido, independentemente de ter ou não pontuação.

    Args:
        cpf (str): CPF a ser verificado.

    Returns:
        bool: True se o CPF é válido, False caso contrário.
    """

    # Remove qualquer pontuação do CPF e verifica se o tamanho é válido
    cpf = cpf.replace(".", "").replace("-", "")
    if len(cpf) != 11:
        return False

    # Verifica se todos os dígitos são iguais
    if cpf == cpf[0] * 11:
        return False

    # Calcula o primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    digito_1 = 11 - (soma % 11)
    if digito_1 > 9:
        digito_1 = 0

    # Calcula o segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    digito_2 = 11 - (soma % 11)
    if digito_2 > 9:
        digito_2 = 0

    # Verifica se os dígitos verificadores são válidos
    if int(cpf[9]) != digito_1 or int(cpf[10]) != digito_2:
        return False

    # Se chegamos até aqui, o CPF é válido!
    return True

def email_valido(email):
    """
    Verifica se um endereço de email é válido.

    Args:
        email (str): Endereço de email a ser verificado.

    Returns:
        bool: True se o email é válido, False caso contrário.
    """

    # Verifica se o email tem o formato correto usando expressão regular
    padrao = r"[^@]+@[^@]+\.[^@]+"
    if not re.match(padrao, email):
        return False

    # Verifica se o email tem um nome de usuário válido (parte antes do @)
    usuario = email.split("@")[0]
    if not re.match(r"^[a-zA-Z0-9._%+-]+$", usuario):
        return False

    # Verifica se o email tem um domínio válido (parte depois do @)
    dominio = email.split("@")[1]
    if not re.match(r"^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", dominio):
        return False

    # Se chegamos aqui, o email é válido!
    return True

def validar_chave_pix(chave):
    """
    Verifica se uma chave PIX é válida.

    Args:
        chave (str): Chave PIX a ser verificada.

    Returns:
        bool: True se a chave é válida, False caso contrário.
    """

    # Verifica se a chave tem o tamanho correto (36 caracteres)
    if len(chave) != 36:
        return False

    # Verifica se a chave é composta apenas de caracteres hexadecimais minúsculos e traço
    if not all(c in "0123456789abcdef-" for c in chave):
        return False
    
    # Verifica o numero de traços na chave
    if chave.count('-') != 4:
        return False
    
    return True