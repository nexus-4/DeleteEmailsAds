# Script Python para Excluir E-mails Automatizados

Este é um script Python simples para excluir automaticamente e-mails da caixa de entrada que correspondam a determinados critérios de busca. É útil para situações em que você deseja filtrar e excluir automaticamente e-mails específicos, como e-mails de propaganda ou de uma loja específica.

## Como Usar

1. Clone este repositório:
no seu terminal digite: 
git clone https://github.com/seu-usuario/nome-do-repositorio.git

2. Instale as dependências necessárias:
   pip install imaplib o modulo usado para fazer tudo isso acontecer

3. Edite o script `delete_emails.py` com suas informações de conta de e-mail e critérios de busca:

```
# Configurações da conta de e-mail
email_address = ""  # Seu e-mail
password = ""  # Sua senha
imap_server = "outlook.office365.com"  # Servidor IMAP (para Outlook, não alterar)

# Critérios de busca (exemplo: busca por e-mails de "empresaX" ou com SUBJECT "anúncio")
search_criteria = '(FROM "aleatory store") #coloque o nome do autor do email

```
4. execute o script.







