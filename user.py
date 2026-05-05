def criar_conta(usuario, senha):
        if not isinstance(usuario, str) or not isinstance(senha, str):
            return "Campos_Invalidos"
    
        if len(usuario) > 100 or len(senha) > 100:
             return "Campo_vazio"
    
        if usuario in usuario:
            return "usuario existe"
    
        usuario[usuario] = senha
        return "Sucesso"
