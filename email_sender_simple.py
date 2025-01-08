import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Banco de dados simples (em memória)
users_db = {}

# Configuração do servidor de e-mail (atualize com seus dados)
SMTP_SERVER = "smtp.gmail.com"  # Servidor SMTP do Gmail
SMTP_PORT = 587  # Porta do servidor SMTP
EMAIL_ADDRESS = "sthefatefinha@gmail.com"  # Substitua pelo seu endereço de e-mail
EMAIL_PASSWORD = "zmsq ojuh tgzl dijz"  # Substitua pela sua senha ou app password

# Mensagem padrão do e-mail
EMAIL_SUBJECT = "Confirmação de Cadastro"
EMAIL_BODY = """
Olá, {username}!

Seja bem-vindo(a) ao nosso sistema. Estamos felizes em tê-lo(a) conosco.

Seu login e senha para você não esquecer:

Usuário: {username}
Senha: {password}

Caso tenha dúvidas ou precise de ajuda, entre em contato com nossa equipe.

Atenciosamente,
Equipe do Cainho e Teffinha :)
"""

def create_account():
    username = input("Digite o nome de usuário: ")
    if username in users_db:
        print("Usuário já existe!")
        return

    password = input("Digite a senha: ")
    email = input("Digite o e-mail: ")
    phone = input("Digite o número de telefone (somente números): ")

    # Verifica se o telefone contém apenas números e tem o tamanho esperado
    if not phone.isdigit() or len(phone) != 11:
        print("Número de telefone inválido! Insira 11 dígitos (código de área + número).")
        return

    # Armazenando os dados do usuário
    users_db[username] = {
        "password": password,
        "email": email,
        "phone": phone
    }
    print(f"Conta criada para {username}!")

    # Enviar e-mail de confirmação
    send_email(email, EMAIL_SUBJECT, EMAIL_BODY.format(username=username, password=password))

def send_email(to_email, subject, message):
    """Envia um e-mail de confirmação para o usuário."""
    try:
        # Configurar mensagem de e-mail
        msg = MIMEMultipart()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to_email
        msg["Subject"] = subject

        # Adicionar corpo do e-mail
        msg.attach(MIMEText(message, "plain"))

        # Conectar ao servidor SMTP e enviar o e-mail
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Habilitar segurança
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Fazer login
            server.send_message(msg)  # Enviar mensagem

        print(f"E-mail enviado para {to_email} com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

def login():
    username = input("Digite o nome de usuário: ")
    password = input("Digite a senha: ")

    if username in users_db and users_db[username]["password"] == password:
        print("Login bem-sucedido!")
    else:
        print("Usuário ou senha incorretos!")

def format_phone(phone):
    """Formata o número de telefone no estilo XX-XXXXX-XXXX."""
    return f"({phone[:2]}) {phone[2:7]}-{phone[7:]}"

def list_users():
    if not users_db:
        print("Nenhum usuário cadastrado!")
        return

    print("\nUsuários cadastrados:")
    for username, details in users_db.items():
        formatted_phone = format_phone(details["phone"])
        print(f"- {username} (E-mail: {details['email']}, Telefone: {formatted_phone})")

def main():
    while True:
        print("\nEscolha uma opção:")
        print("1 - Criar conta")
        print("2 - Fazer login")
        print("3 - Ver usuários cadastrados")
        print("4 - Sair")
        option = input("Digite o número da opção: ")

        if option == "1":
            create_account()
        elif option == "2":
            login()
        elif option == "3":
            list_users()
        elif option == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
