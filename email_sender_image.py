import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# Banco de dados simples (em memória)
users_db = {}

# Configuração do servidor de e-mail (atualize com seus dados)
SMTP_SERVER = "smtp.gmail.com"  # Servidor SMTP do Gmail
SMTP_PORT = 587  # Porta do servidor SMTP
EMAIL_ADDRESS = "usuario@gmail.com"  # Substitua pelo seu endereço de e-mail
EMAIL_PASSWORD = "apppassword"  # Substitua pela sua senha ou app password

#o app password você pode acessar seu google e gerar uma senha

# Mensagens e assuntos do e-mail
EMAIL_SUBJECT_HTML = "Cadastro efetuado com sucesso!"
EMAIL_BODY_HTML = """
<html>
  <body>
    <h1 style="font-size: 40px; color: #0000FF;">BEM VINDO A NOSSA EMPRESA</h1>
    <p>Aqui estão seus dados para acesso a conta:</p>
    <ul>
      <li><strong>Usuário:</strong> {username}</li>
      <li><strong>Senha:</strong> {password}</li>
    </ul>
    <p>No final do email temos um anexo de Boas-Vindas!!!!!</p>
    <p>Que comece sua jornada de ganhar dinheiro e tempo.</p>
    <br>
    <p>Atenciosamente,</p>
    <p>Sthefane e Cainho</p>
  </body>
</html>
"""

def send_email(to_email, subject, message, image_path=None):
    """Envia um e-mail de confirmação para o usuário com ou sem imagem anexada."""
    try:
        msg = MIMEMultipart("related")
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to_email
        msg["Subject"] = subject

        # Adicionar corpo do e-mail
        msg.attach(MIMEText(message, "html"))

        # Adicionar imagem se o caminho for fornecido
        if image_path and os.path.exists(image_path):
            with open(image_path, "rb") as img_file:
                img = MIMEImage(img_file.read())
                img.add_header("Content-ID", "<image1>")
                img.add_header("Content-Disposition", "inline", filename="imagem.png")
                msg.attach(img)

        # Enviar o e-mail
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

        print(f"E-mail enviado para {to_email} com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

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

    # Caminho para a imagem (ajuste com o caminho correto da sua imagem)
    image_path = r"C:\Users\Sthefane\Desktop\Projeto\Email\image.png"

    # Enviar e-mail HTML com imagem
    send_email(email, EMAIL_SUBJECT_HTML, EMAIL_BODY_HTML.format(username=username, password=password), image_path)

def login():
    username = input("Digite o nome de usuário: ")
    password = input("Digite a senha: ")

    if username in users_db and users_db[username]["password"] == password:
        print("Login bem-sucedido!")
    else:
        print("Usuário ou senha incorretos!")

def format_phone(phone):
    """Formata o número de telefone no estilo (XX) XXXXX-XXXX."""
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
