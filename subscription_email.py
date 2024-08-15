import imaplib

# Configurações da conta de e-mail
email_address = "seu email"
password = "sua senha"
imap_server = "outlook.office365.com"

# Conectar ao servidor IMAP
imap = imaplib.IMAP4_SSL(imap_server)
imap.login(email_address, password)

# Cancelar inscrição de uma caixa de correio específica
mailbox = "INBOX"
response = imap.unsubscribe(mailbox)

# Verificar se a operação foi bem-sucedida
if response[0] == "OK":
    print("Operação concluída com sucesso: Cancelada inscrição na caixa de correio", mailbox)
else:
    print("Erro ao cancelar inscrição na caixa de correio", mailbox)

# Fechar conexão com o servidor IMAP
imap.logout()
