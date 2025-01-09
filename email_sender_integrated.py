import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.utils import make_msgid

# Configuração do servidor de e-mail
SMTP_SERVER = "smtp.gmail.com"  # Servidor SMTP do Gmail
SMTP_PORT = 587  # Porta do servidor SMTP
EMAIL_ADDRESS = "sthefatefinha@gmail.com"  # Substitua pelo seu endereço de e-mail
EMAIL_PASSWORD = "zmsq ojuh tgzl dijz"  # Substitua pela sua senha ou app password

# Dados do administrador
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "123"  # Senha do administrador

# Lista para armazenar os cadastros
cadastros = []

# Mensagem padrão do e-mail para exclusão
DELETE_EMAIL_SUBJECT = "Notificação de Exclusão de Cadastro"
DELETE_EMAIL_BODY = """
Olá, {username}!

Seu cadastro foi removido do nosso sistema. Se isso foi um engano, entre em contato com nossa equipe.

Atenciosamente,
Equipe do Cainho e Teffinha
"""

# Definindo o assunto e corpo do e-mail
EMAIL_SUBJECT_SIMPLE = "Cadastro efetuado com sucesso!"
EMAIL_BODY_SIMPLE = """
Olá, {username}!

Seja bem-vindo(a) ao nosso sistema. Estamos felizes em tê-lo(a) conosco.

Seu login e senha para você não esquecer:

Usuário: {username}
Senha: {password}

Caso tenha dúvidas ou precise de ajuda, entre em contato com nossa equipe.

Atenciosamente,
Equipe do Cainho e Teffinha :)
"""

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

# Função para enviar o e-mail
def send_email(to_email, subject, message, image_path=None):
    """Envia um e-mail para o destinatário especificado, com a opção de anexar uma imagem."""
    try:
        msg = MIMEMultipart("related")  # Usando "related" para incluir conteúdo embutido
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to_email
        msg["Subject"] = subject

        # Adicionar o corpo do e-mail
        msg.attach(MIMEText(message, "html" if image_path else "plain"))

        if image_path:
            with open(image_path, "rb") as image_file:
                # Cria um Content-ID para a imagem
                image_cid = make_msgid(domain="example.com")
                image = MIMEImage(image_file.read())
                image.add_header('Content-ID', f"<{image_cid}>")
                image.add_header('Content-Disposition', 'inline', filename="image.png")  # Ajuste o nome do arquivo se necessário
                msg.attach(image)

        # Conectar ao servidor SMTP e enviar o e-mail
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Habilitar segurança
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Fazer login
            server.send_message(msg)  # Enviar mensagem

        print(f"E-mail enviado para {to_email} com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

# Função para criar uma conta (exemplo)
def create_account():
    username = input("Digite o nome de usuário: ")
    password = input("Digite a senha: ")
    email = input("Digite o e-mail: ")
    phone = input("Digite o número de telefone (somente números): ")

    # Verificar se o email ou telefone já estão cadastrados
    for cadastro in cadastros:
        if cadastro["email"] == email:
            print("Erro: E-mail já cadastrado.")
            return
    
    for cadastro in cadastros:
        if cadastro["phone"] == phone:
            print("Erro: Número de telefone já cadastrado.")
            return

    # Adicionar cadastro à lista
    cadastros.append({
        "username": username,
        "password": password,
        "email": email,
        "phone": phone
    })

    ## Enviar e-mail simples
    #send_email(email, EMAIL_SUBJECT_SIMPLE, EMAIL_BODY_SIMPLE.format(username=username, password=password))

    # Caminho relativo para a imagem
    image_path = os.path.join(os.path.dirname(__file__), "image.png")

    # Enviar e-mail HTML com imagem (caso a imagem exista)
    if os.path.exists(image_path):
        print("Imagem encontrada!")
        send_email(email, EMAIL_SUBJECT_HTML, EMAIL_BODY_HTML.format(username=username, password=password), image_path)
    else:
        print("Imagem não encontrada, verifique o caminho.")

# Função para fazer login de usuário
def user_login():
    email = input("Digite o e-mail: ")
    password = input("Digite a senha: ")

    # Verificar se o e-mail e senha correspondem a um cadastro
    for cadastro in cadastros:
        if cadastro["email"] == email and cadastro["password"] == password:
            print(f"Bem-vindo, {cadastro['username']}!")
            return True
    
    print("E-mail ou senha incorretos. Tente novamente.")
    return False

#Formata o número de telefone no estilo (XX) XXXXX-XXXX
def format_phone(phone):
    return f"({phone[:2]}) {phone[2:7]}-{phone[7:]}"

# Função para visualizar cadastros como administrador
def view_cadastros():
    print("\nLista de cadastros:")
    if cadastros:
        for idx, cadastro in enumerate(cadastros, 1):
            print(f"ID: {idx} - Usuário: {cadastro['username']} - Email: {cadastro['email']} - Número: {format_phone(cadastro['phone'])}")
    else:
        print("Nenhum cadastro encontrado.")

# Função para adicionar um cadastro como administrador
def add_cadastro():
    username = input("Digite o nome de usuário: ")
    password = input("Digite a senha: ")
    email = input("Digite o e-mail: ")
    phone = input("Digite o número de telefone (somente números): ")

    # Verificar se o e-mail ou telefone já estão cadastrados
    for cadastro in cadastros:
        if cadastro["email"] == email:
            print("Erro: E-mail já cadastrado.")
            return
    
    for cadastro in cadastros:
        if cadastro["phone"] == phone:
            print("Erro: Número de telefone já cadastrado.")
            return

    # Adicionar cadastro à lista
    cadastros.append({
        "username": username,
        "password": password,
        "email": email,
        "phone": phone
    })

    print(f"Cadastro de {username} adicionado com sucesso!")
    # Enviar e-mail simples
    send_email(email, EMAIL_SUBJECT_SIMPLE, EMAIL_BODY_SIMPLE.format(username=username, password=password))

# Função para excluir um cadastro como administrador
def delete_cadastro():
    view_cadastros()
    if cadastros:
        try:
            idx = int(input("Digite o número do cadastro que deseja excluir: ")) - 1
            if 0 <= idx < len(cadastros):
                removed = cadastros.pop(idx)
                print(f"Cadastro de {removed['username']} excluído com sucesso!")
                
                # Enviar e-mail de notificação
                send_email(
                    removed['email'], 
                    DELETE_EMAIL_SUBJECT, 
                    DELETE_EMAIL_BODY.format(username=removed['username'])
                )
                print(f"E-mail de notificação enviado para {removed['email']}!")
            else:
                print("Número de cadastro inválido!")
        except ValueError:
            print("Por favor, digite um número válido!")

# Função para login do administrador
def admin_login():
    username = input("Digite o nome de usuário do administrador: ")
    password = input("Digite a senha do administrador: ")
    
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("\nLogin de administrador bem-sucedido!")
        return True
    else:
        print("\nCredenciais inválidas. Tente novamente.")
        return False

# Função principal
def main():
    while True:
        print("\nEscolha uma opção:")
        print("1 - Criar conta")
        print("2 - Entrar como admin")
        print("3 - Entrar como usuário")
        print("4 - Sair")
        option = input("Digite o número da opção: ")

        if option == "1":
            create_account()
        elif option == "2":
            if admin_login():
                while True:
                    print("\nOpções de Administrador:")
                    print("1 - Ver cadastros")
                    print("2 - Adicionar cadastro")
                    print("3 - Excluir cadastro")
                    print("4 - Sair do painel de administração")
                    admin_option = input("Digite o número da opção: ")
                    
                    if admin_option == "1":
                        view_cadastros()
                    elif admin_option == "2":
                        add_cadastro()
                    elif admin_option == "3":
                        delete_cadastro()
                    elif admin_option == "4":
                        print("Saindo do painel de administração...")
                        break
                    else:
                        print("Opção inválida!")
        elif option == "3":
            if user_login():
                continue
        elif option == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()