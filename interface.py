from back_end import Back

########################################################################
########################    NAVEGAÇÃO   ################################
########################################################################


class interface(Back):
    

#### Navegação de Login 
    def navega_ESCOLHA_para_Auth_E_(self):
        self.escolha_frame.place_forget()
        self.Frame_Auth_ESTUDANTE()  
    def navega_ESCOLHA_para_Auth_P_(self):
        self.escolha_frame.place_forget()
        self.Frame_Auth_PROFESSOR()
        
    def navega_PROFESSOR_Auth_para_ESCOLHA_(self):
        self.AuthProfessor_frame.place_forget()
        self.Frame_ESCOLHA()

    def navega_ESTUDANTE_Auth_para_ESCOLHA_(self):
        self.AuthEstudante_frame.place_forget()
        self.Frame_ESCOLHA()
        
#### Navegação de cadastro

      
    def navega_PROFESSOR_Auth_para_C_(self):
        self.AuthProfessor_frame.place_forget()
        self.Frame_C_PROFESSOR()  
    def navega_PROFESSOR_C_para_Auth(self):
        self.createProfessor_frame.place_forget()
        self.Frame_Auth_PROFESSOR()

########################################################################
########################    ESTUDANTE   ################################
########################################################################

############# Autenticação

    def navega_ESTUDANTE_Auth_para_R_(self):
        
        matricula = self.AuthEstudante_matricula.get()
        senha = self.AuthEstudante_senha.get()
        resultado = self.Auth_ESTUDANTE(matricula, senha)
        
        if resultado == 1:
            
            self.AuthEstudante_frame.place_forget()
            estudante = self.R_ESTUDANTE(matricula)
            self.Frame_R_ESTUDANTE(estudante)
            
        elif resultado == 2:
            
            self.AuthEstudante_frame.place_forget()
            estudanteADM = self.R_ESTUDANTE(matricula)
            self.Frame_R_ESTUDANTEADM(estudanteADM)
            
        elif resultado == 0:
            self.AuthEstudante_aviso.configure(text="Usuario não existe no banco de dados")
        
        else:
            self.AuthEstudante_aviso.configure(text="Erro na comunicação com o banco de dados")
    def navega_ESTUDANTE_R_para_Auth_(self):
        self.readEstudante_frame.place_forget()
        self.Frame_Auth_ESTUDANTE()

############# CRUD

    def navega_ESTUDANTE_Auth_para_C_(self):
        self.AuthEstudante_frame.place_forget()
        self.Frame_C_ESTUDANTE()  

    def navega_ESTUDANTE_CA_para_Auth_(self):
        
        matricula = self.createEstudante_matricula.get()
        senha = str(self.createEstudante_senha.get())
        nome = str(self.createEstudante_nome.get())
        email = str(self.createEstudante_email.get())
        
        estudante = {
                    "matricula": matricula ,
                    "senha": senha ,
                    "email": email ,
                    "nome": nome }
        
        resultado = self.C_ESTUDANTE(estudante)
        if resultado == 1:
            self.createEstudante_frame.place_forget()
            self.Frame_Auth_ESTUDANTE()
        elif resultado == 0:
            self.createEstudante_aviso.configure(text = "Matricula ja existe")

    def navega_ESTUDANTE_C_para_Auth_(self):
        self.createEstudante_frame.place_forget()
        self.Frame_Auth_ESTUDANTE()

    def navega_ESTUDANTE_R_para_U_(self):
        self.readEstudante_frame.place_forget()
        estudante = self.R_ESTUDANTE(self.readEstudante_matricula.cget('text'))
        self.Frame_U_D_ESTUDANTE(estudante)
        
    def navega_ESTUDANTE_U_para_R_(self):
        
        estudante_temp = self.R_ESTUDANTE(self.updateEstudante_matricula.cget("text"))
    
        senha_new = self.updateEstudante_senha.get()
        email_new = self.updateEstudante_email.get()
        nome_new = self.updateEstudante_nome.get()
        estudante = {
                        "matricula": self.updateEstudante_matricula.cget("text"),
                        "senha":senha_new if senha_new != "" else estudante_temp["senha"] ,
                        "email":email_new if email_new != "" else estudante_temp["email"] ,
                        "nome":nome_new if nome_new != "" else estudante_temp["nome"]}
            
        self.U_ESTUDANTE(estudante)
        self.updateEstudante_frame.place_forget()
        estudante = self.R_ESTUDANTE(estudante["matricula"])
        self.Frame_R_ESTUDANTE(estudante)
           
    def navega_ESTUDANTE_U_para_Auth_(self):
        
        matricula = self.updateEstudante_matricula.cget("text")
        if self.D_ESTUDANTE(matricula):
            self.updateEstudante_frame.place_forget()
            self.Frame_Auth_ESTUDANTE()
        else:
            self.updateEstudante_aviso.configure(text="Não foi possivel excluir a conta")

############# Turmas

    def navega_ESTUDANTE_R_para_R_TURMA_(self):
        self.readEstudante_frame.place_forget()
        turma = self.V_TURMA()
        self.Frame_R_TURMA(turma) 

    def navega_R_TURMA_para_R_ESTUDANTE_(self):
        self.readTurma_frame.place_forget()
        estudante = self.R_ESTUDANTE(self.readEstudante_matricula.get())
        self.Frame_R_ESTUDANTE(estudante)

    def navega_R_TURMA_para_R_AVALIACAO_(self):
        self.readTurma_frame.place_forget()
        
        turma = self.readTurma_cb_turma.get()
        turma = int((turma.split(" - "))[0])
        avaliacoes = self.V_AVALIACAO(turma)
        
        self.Frame_R_AVALIACAO(turma, avaliacoes)
    
############# Avaliações

    def navega_CAv_AVALIACAO_para_R_AVALIACAO_(self):
        
        turma = self.readTurma_cb_turma.get()
        turma = int((turma.split(" - "))[0])
        avaliacao = {     "estudante": self.readEstudante_matricula.cget('text'),
                          "turma": turma,
                          "avaliacao": self.createAvaliacao_avaliacao.get(),
                          "denuncia": 0}
        print(avaliacao)
        resultado = self.C_AVALIACAO(avaliacao)
        if resultado == 1:
            self.createAvaliacao_frame.place_forget()
            avaliacoes = self.V_AVALIACAO(turma)
            self.Frame_R_AVALIACAO(turma, avaliacoes)
        else:
            self.createAvaliacao_aviso.configure("Erro ao criar")
    
    def navega_CDen_AVALIACAO_para_R_AVALIACAO_(self):
        
        turma = self.readTurma_cb_turma.get()
        turma = int((turma.split(" - "))[0])
        avaliacao = {     "estudante": self.readEstudante_matricula.cget('text'),
                          "turma": turma,
                          "avaliacao": self.createAvaliacao_avaliacao.get(),
                          "denuncia": 1}
        resultado = self.C_AVALIACAO(avaliacao)
        if resultado == 1:
            self.createAvaliacao_frame.place_forget()
            avaliacoes = self.V_AVALIACAO(turma)
            self.Frame_R_AVALIACAO(turma, avaliacoes)
        else:
            self.createAvaliacao_aviso.configure("Erro ao criar")
     
    def navega_C_AVALIACAO_para_R_AVALIACAO_(self):
        
        self.createAvaliacao_frame.place_forget()
         
        turma = self.readTurma_cb_turma.get()
        turma = int((turma.split(" - "))[0])
        avaliacoes = self.V_AVALIACAO(turma)
        
        self.Frame_R_AVALIACAO(turma, avaliacoes)
          
    def navega_R_AVALIACAO_para_C_AVALIACAO_(self):
        
        self.readAvaliacao_frame.place_forget()
        turma = self.readTurma_cb_turma.get()
        self.Frame_C_AVALIACAO(turma)
    
    def navega_R_AVALIACAO_para_U_D_AVALIACAO_(self):
        
        self.readAvaliacao_frame.place_forget()
        turma = self.readTurma_cb_turma.get()
        turma = int((turma.split(" - "))[0])
        estudante = self.readEstudante_matricula.cget('text')
        
        avaliacoes = self.V_estudante_AVALIACAO(turma, estudante)
        self.Frame_U_D_AVALIACAO(avaliacoes)
    
    def navega_Uav_AVALIACAO_para_R_AVALIACAO_(self):
        
        self.updateDeleteAvaliacao_frame.place_forget()
        
        codigo = self.updateDeleteAvaliacao_cb_id.get()
        codigo = int((codigo.split(" - "))[0])
        estudante = self.readEstudante_matricula.cget('text')
        
        avaliacao = {"codigo": codigo,
                     "avaliacao": self.updateDeleteAvaliacao_avaliacao.get(),
                     "denuncia": 0}
        self.U_AVALIACAO(avaliacao)
        
        turma = self.readTurma_cb_turma.get()
        turma = int((turma.split(" - "))[0])
        avaliacoes = self.V_AVALIACAO(turma)
        
        self.Frame_R_AVALIACAO(turma, avaliacoes)
        
    def navega_Uden_AVALIACAO_para_R_AVALIACAO_(self):
        
        self.updateDeleteAvaliacao_frame.place_forget()
        
        codigo = self.updateDeleteAvaliacao_cb_id.get()
        codigo = int((codigo.split(" - "))[0])
        estudante = self.readEstudante_matricula.cget('text')
        
        avaliacao = {"codigo": codigo,
                     "avaliacao": self.updateDeleteAvaliacao_avaliacao.get(),
                     "denuncia": 1}
        self.U_AVALIACAO(avaliacao)
        
        turma = self.readTurma_cb_turma.get()
        turma = int((turma.split(" - "))[0])
        avaliacoes = self.V_AVALIACAO(turma)
        
        self.Frame_R_AVALIACAO(turma, avaliacoes)
    
    def navega_D_AVALIACAO_para_R_AVALIACAO_(self):
        
        self.updateDeleteAvaliacao_frame.place_forget()
        codigo = self.updateDeleteAvaliacao_cb_id.get()
        codigo = int((codigo.split(" - "))[0])
        estudante = self.readEstudante_matricula.cget('text')
        
        self.D_AVALIACAO(codigo)
        
        turma = self.readTurma_cb_turma.get()
        turma = int((turma.split(" - "))[0])
        avaliacoes = self.V_AVALIACAO(turma)
        
        self.Frame_R_AVALIACAO(turma, avaliacoes)
    
    def navega_U_D_AVALIACAO_para_R_AVALIACAO_(self):
        
        self.updateDeleteAvaliacao_frame.place_forget()
        turma = self.readTurma_cb_turma.get()
        turma = int((turma.split(" - "))[0])
        avaliacoes = self.V_AVALIACAO(turma)
        
        self.Frame_R_AVALIACAO(turma, avaliacoes)
    
    def navega_R_AVALIACAO_para_R_TURMA_(self):
        
        self.readTurma_frame.place_forget()
        turma = self.V_TURMA()
        self.Frame_R_TURMA(turma)
        
        
########################################################################
###########################    ADM   ###################################
########################################################################

    def navega_ESTUDANTEADM_R_para_Auth_(self):
        self.readEstudanteADM_frame.place_forget()
        self.Frame_Auth_ESTUDANTE()
        
### Navegação do usuario professor

    def navega_PROFESSOR_Auth_para_R_(self):
        
        matricula = self.AuthProfessor_matricula.get()
        senha = self.AuthProfessor_senha.get()
        if self.Auth_PROFESSOR(matricula, senha) == True:
            self.AuthProfessor_frame.place_forget()
            self.Frame_R_PROFESSOR(self.R_PROFESSOR())
        elif self.Auth_PROFESSOR(matricula, senha) == False:
            self.AuthProfessor_aviso.configure(text="Usuario/Senha inválidos")
        else:
            self.AuthProfessor_aviso.configure(text="erro de login")

    def navega_PROFESSOR_R_para_Auth_(self):
        self.readProfessor_frame.place_forget()
        self.Frame_Auth_PROFESSOR()
    def navega_PROFESSOR_R_para_U_(self):
        self.readProfessor_frame.place_forget()
        self.Frame_U_D_PROFESSOR(self.R_PROFESSOR())
    def navega_PROFESSOR_U_para_R_(self):
        self.updateProfessor_frame.place_forget()
        self.U_PROFESSOR()
        self.Frame_R_PROFESSOR(self.R_PROFESSOR())
    def navega_PROFESSOR_U_para_Auth_(self):
        if self.D_PROFESSOR():
            self.updateProfessor_frame.place_forget()
            self.Frame_Auth_PROFESSOR()
        else:
            self.updateProfessor_aviso.configure(text="Não foi possivel excluir")