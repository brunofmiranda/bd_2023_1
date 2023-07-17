import pyodbc as bd


########################################################################
###########################    BACK   ##################################
########################################################################

class Back():


######################## CONEXÃO COM O BD ##############################

    def conecta_bd(self):
        
        ############ ALTERAR CONFORME O BANCO DE DADOS UTILIZADO ##################
        server = 'bruno'
        database = 'avaliaE'
        user = 'sa'
        psswrd = '123'
        
        try:
            self.conn = bd.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={user};PWD={psswrd}')
            self.cursor = self.conn.cursor()
            print("conexão concluída")
        except:
            print("conexão erro")
    
    def desconecta_bd(self):
        self.conn.close()

########################## ESTUDANTE ###################################

    def Auth_ESTUDANTE(self, matricula, senha):
        retorno = self.cursor.execute(f"""EXECUTE Auth_ESTUDANTE {matricula}, '{senha}'""")
        for row in retorno:
            resultado = row[0]
        return resultado

    def C_ESTUDANTE(self, estudante):
        
        try:
            self.cursor.execute(f"""EXECUTE C_ESTUDANTE 
                                                        {estudante["matricula"]},
                                                        '{estudante["senha"]}',
                                                        '{estudante["nome"]}',
                                                        '{estudante["email"]}'
                                                                                    """)
            self.cursor.commit()
            return 1
        except:
            return 0
                  
    def R_ESTUDANTE(self, matricula):
        
        retorno = self.cursor.execute(f"""EXECUTE R_ESTUDANTE '{matricula}'""")
        estudante = {"matricula": "", "senha": "", "email": "", "nome": ""}
        for i in retorno:
            estudante["matricula"] = i[0]
            estudante["senha"] = i[1]
            estudante["nome"] = i[2]
            estudante["email"] = i[3]
        return estudante
    
    def U_ESTUDANTE(self, estudante):
         
        self.cursor.execute(f"""EXECUTE U_ESTUDANTE {estudante["matricula"]}, 
                                                    '{estudante["senha"]}', 
                                                    '{estudante["nome"]}', 
                                                    '{estudante["email"]}'""")
        self.cursor.commit()
        
    def D_ESTUDANTE(self, matricula):
        
        retorno = self.cursor.execute(f"""EXECUTE D_ESTUDANTE {matricula}""")
        try:
            for i in retorno:
                resultado = i[0]
            return False
        except:
            self.cursor.commit()
            return True

########################## TURMA #######################################

    def V_TURMA(self):
        retorno = self.cursor.execute(f"""SELECT * FROM lista_TURMA""")
        resultado = []
        resultado.append(" - ")
        for row in retorno:
            resultado.append(row[0])
        return resultado

########################## AVALIACAO ###################################
    def V_AVALIACAO(self, turma):
        retorno = self.cursor.execute(f"""EXECUTE lista_AVALIACAO {turma}""")
        resultado = []
        for row in retorno:
            tupla = (row[0], row[1])
            resultado.append(tupla)

        return resultado
    
    def C_AVALIACAO(self, avaliacao):
        try:
            self.cursor.execute(f"""EXECUTE C_AVALIACAO 
                                                        {avaliacao["estudante"]},
                                                        {avaliacao["turma"]},
                                                        '{avaliacao["avaliacao"]}',
                                                        {avaliacao["denuncia"]}
                                                                                """)
            self.cursor.commit()
            return 1
        except:
            return 0

    def U_AVALIACAO(self, avaliacao):
        
        self.cursor.execute(f"""EXECUTE U_AVALIACAO 
                                                    {avaliacao["codigo"]}, 
                                                    '{avaliacao["avaliacao"]}', 
                                                    {avaliacao["denuncia"]}""")
        self.cursor.commit()
        
    def D_AVALIACAO(self, codigo):
        self.cursor.execute(f"""EXECUTE D_AVALIACAO {codigo}""")
        
    def V_estudante_AVALIACAO(self, turma, estudante):
        retorno = self.cursor.execute(f"""EXECUTE lista_estudante_AVALIACAO {turma}, {estudante}""")
        resultado = []
        for row in retorno:
            opcao = f"{row[0]} - {row[1]}"
            resultado.append(opcao)
        return resultado
    
######################### PROFESSOR ####################################
    def Auth_PROFESSOR(self, matricula, senha):
        retorno = self.cursor.execute(f"""EXECUTE Auth_PROFESSOR {matricula}, {senha}""")
        for row in retorno:
            resultado = row[0]
        if resultado == 0:
            return False
        elif resultado == 1:
            return True
        else:
            return "Erro"

    def C_PROFESSOR(self):
        matricula = self.createProfessor_matricula.get()
        senha = str(self.createProfessor_senha.get())
        departamento = self.createProfessor_departamento.get()
        nome = self.createProfessor_nome.get()
        email = self.createProfessor_email.get()
        
        try:
            self.cursor.execute(f"""EXECUTE C_PROFESSOR {matricula}, '{senha}', {departamento}, '{nome}',  '{email}'""")
            self.cursor.commit()
            self.createProfessor_aviso.configure(text="Cadastro Realizado")
        except:
            self.createProfessor_aviso.configure(text="Erro no cadastro")
    def R_PROFESSOR(self):
        
        matricula = self.AuthProfessor_matricula.get()
        retorno = self.cursor.execute(f"""EXECUTE R_PROFESSOR '{matricula}'""")
        professor = {"matricula": "", "senha": "", "email": "", "nome": ""}
        for i in retorno:
            professor["matricula"] = i[0]
            professor["senha"] = i[1]
            professor["departamento"] = i[2]
            professor["nome"] = i[3]
            professor["email"] = i[4]
        return professor
    def U_PROFESSOR(self):
        
        matricula = self.AuthProfessor_matricula.get()
        
        senha = self.updateProfessor_senha.get() if self.updateProfessor_senha.get() != "" else self.readProfessor_senha.cget('text')
    
        departamento_bruto = self.updateProfessor_departamento.get() if self.updateProfessor_departamento.get() != "" else self.readProfessor_departamento.cget('text')
        departamento_bruto = departamento_bruto.split(" - ")
        departamento = departamento_bruto[0] if departamento_bruto[0] != '' else self.readProfessor_departamento.cget('text')
        
        nome = str(self.updateProfessor_nome.get()) if self.updateProfessor_nome.get() != "" else self.readProfessor_nome.cget('text')
        
        email = self.updateProfessor_email.get() if self.updateProfessor_email.get() != "" else self.readProfessor_email.cget('text')
        
        self.cursor.execute(f"""U_PROFESSOR '{matricula}','{senha}', {departamento}, '{nome}', '{email}'""")
        self.cursor.commit()       
    def D_PROFESSOR(self):
        matricula = self.AuthProfessor_matricula.get()
        retorno = self.cursor.execute(f"""EXECUTE D_PROFESSOR {matricula}""")
        try:
            for i in retorno:
                resultado = i[0]
            return False
        except:
            self.cursor.commit()
            return True

######################## DEPARTAMENTO ####################################

    def C_DEPARTAMENTO(self):
        
        codigo = self.createDepartamento_codigo.get()
        nome = self.createDepartamento_nome.get()
        
        try:
            self.cursor.execute(f"""EXECUTE C_DEPARTAMENTO {codigo}, '{nome}'""")
            self.cursor.commit()
            self.createDepartamento_aviso.configure(text="Criado com sucesso")       

        except:
            self.createDepartamento_aviso.configure(text="Não foi possivel criar")       
    def R_DEPARTAMENTO(self):
        
        codigo = self.readDepartamento_codigo.get()
        retorno = self.cursor.execute(f"""EXECUTE R_DEPARTAMENTO {codigo}""")
        departamento = {"codigo": "", "nome": ""}
        try:
            for i in retorno:
                departamento["codigo"] = i[0]
                departamento["nome"] = i[1]
            self.readDepartamento_nome2.configure(text=departamento["nome"])
        except:
            self.readDepartamento_nome2.configure(text="departamento não encontrado")
    def U_DEPARTAMENTO(self):
        codigo = self.readDepartamento_codigo.get()
        nome = self.updateDepartamento_nome.get()
        
        self.cursor.execute(f"""EXECUTE U_DEPARTAMENTO {codigo}, '{nome}'""")
        self.cursor.commit()
        self.updateDepartamento_aviso.configure(text="Alterado com sucesso")
    def D_DEPARTAMENTO(self):
        codigo = self.updateDepartamento_codigo.get()
        retorno = self.cursor.execute(f"""EXECUTE D_DEPARTAMENTO {codigo}""")
        try:
            for i in retorno:
                resultado = i[0]
            self.updateDepartamento_aviso.configure(text="Não foi possivel excluir")
        except:
            self.cursor.commit()
            self.updateDepartamento_aviso.configure(text="Exclusão concluida")
     
    def V_DEPARTAMENTO_(self):
        retorno = self.cursor.execute(f"""SELECT * FROM lista_DEPARTAMENTO""").fetchall()
        resultado = []
        resultado.append(" - ")
        for row in retorno:
            resultado.append(row[0])
        return resultado
    