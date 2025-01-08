# automatic_messenger
Sistema de Cadastro com Envio de E-mails Automáticos
Este projeto é um sistema básico de cadastro de usuários desenvolvido em Python. Ele permite que os usuários sejam cadastrados com dados como nome de usuário, senha, e-mail e número de telefone. Além disso, o sistema envia automaticamente um e-mail de boas-vindas, podendo incluir uma imagem de boas-vindas anexada.



🌟 Sistema de Cadastro e Envio de E-mails 📧
Este projeto é um sistema simples para cadastro de usuários com funcionalidades de envio de e-mails personalizados. Ele combina 📋 gestão de usuários e ✉️ envio de mensagens de boas-vindas em um só lugar, com suporte para e-mails em HTML e anexos.

🚀 Funcionalidades
📥 Cadastro de Usuários:

Crie contas com nome de usuário, senha, e-mail e telefone.
🚦 Validação do telefone (11 dígitos, apenas números).
🎉 Envio de e-mail automático após o cadastro com os dados de acesso.
🔑 Login de Usuários:

Faça login com nome de usuário e senha para autenticação simples.
📋 Listagem de Usuários:

Veja todos os usuários cadastrados.
Formata automaticamente o número de telefone para o padrão brasileiro.
📧 Envio de E-mails Personalizados:

Envie e-mails com mensagens em HTML para os usuários cadastrados.
📎 Suporte para anexos: envie uma imagem de boas-vindas junto ao e-mail (se a imagem for encontrada no caminho especificado).
🛠️ Estrutura do Código
O sistema é organizado em funções para facilitar o uso e manutenção:

create_account(): ✍️ Cria contas de usuários e valida os dados fornecidos.
send_email(to_email, subject, message, image_path=None): 💌 Gerencia o envio de e-mails em HTML e com anexos.
login(): 🔐 Realiza a autenticação dos usuários cadastrados.
list_users(): 👥 Lista todos os usuários cadastrados com detalhes (e-mail e telefone formatado).
main(): 🏗️ Menu principal para navegação e interação.
🔧 Requisitos
Antes de executar o projeto, certifique-se de que os seguintes pacotes e configurações estejam no ambiente Python:

Pacotes necessários:

📦 smtplib - Para envio de e-mails via protocolo SMTP.
📦 email.mime - Para criar mensagens de e-mail com texto e anexos.


Configuração do servidor SMTP:
Atualize o código com seu endereço de e-mail e senha no trecho abaixo:

python
Copiar código
EMAIL_ADDRESS = "seuemail@gmail.com"
EMAIL_PASSWORD = "suasenhaouapppassword"
🖼️ Demonstração do E-mail em HTML
Mensagem HTML:
🖼️ Imagem de boas-vindas personalizada (anexa).
📜 Texto chamativo com dados de acesso do usuário.
html
Copiar código
<h1 style="font-size: 40px; color: #0000FF;">BEM-VINDO À NOSSA EMPRESA</h1>
<p>Aqui estão seus dados para acesso à conta:</p>
<ul>
  <li><strong>Usuário:</strong> {username}</li>
  <li><strong>Senha:</strong> {password}</li>
</ul>
<p>Que comece sua jornada de ganhar dinheiro e tempo! 💸</p>
<p>Atenciosamente,</p>
<p>Sthefane e Cainho</p>
🏃‍♀️ Como Usar
Clone este repositório:

bash
Copiar código
git clone https://github.com/seuusuario/seuprojeto.git
cd seuprojeto
Execute o script:

bash
Copiar código
python nome_do_script.py
Siga o menu para:

Criar contas.
Fazer login.
Listar usuários cadastrados.
📩 Contribua!
Adoraríamos receber contribuições para melhorar este projeto! 🤝
Sinta-se à vontade para abrir issues ou enviar pull requests.

🌈 Divirta-se usando o sistema! 😊
