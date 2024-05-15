import imaplib

# Configurações da conta de e-mail
email_address = "nadjajanara@hotmail.com" # Seu email
password = "Companhia2565" # sua senha
imap_server = "outlook.office365.com" # caso outlook, nao mudar

# Conectar ao servidor IMAP
imap = imaplib.IMAP4_SSL(imap_server)
imap.login(email_address, password)

# Selecionar a caixa de entrada
status, messages = imap.select("INBOX")

# Critérios de busca (exemplo: busca por e-mails de "empresaX" ou com SUBJECT "anúncio")
search_criteria = '(FROM "aleatory store")'

# Buscar e-mails correspondentes aos critérios
status, message_ids = imap.search(None, search_criteria)

if status == "OK":
    for message_id in message_ids[0].split():
        # Excluir o e-mail
        imap.store(message_id, '+FLAGS', '\\Deleted')
        print(f"E-mail do remetente {search_criteria} excluído com SUCESSO!!.")
    print("Feito!")
else:
    print("Status nao OK")
    
# Fechar conexão com o servidor IMAP
imap.expunge()
imap.close()
imap.logout()
