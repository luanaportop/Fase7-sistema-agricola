def enviar_alerta(mensagem):
    try:
        # Aqui você colocará o código de envio via AWS SNS ou SES
        print("ALERTA:", mensagem)
        return True
    except Exception as e:
        print("Erro ao enviar alerta:", e)
        return False
