import customtkinter as ctk
import pyodbc as bd
import tkinter as tk
from tkinter import ttk

########################################################################
###########################    BACK   ##################################
########################################################################

class Back():

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

####### ESTUDANTE
    def Auth_ESTUDANTE(self, matricula, senha):
        retorno = self.cursor.execute(f"""EXECUTE Auth_ESTUDANTE {matricula}, {senha}""")
        for row in retorno:
            resultado = row[0]
        if resultado == 0:
            return False
        elif resultado == 1:
            return True
        else:
            return "Erro"

    def C_ESTUDANTE(self):
        matricula = self.createEstudante_matricula.get()
        senha = str(self.createEstudante_senha.get())
        nome = str(self.createEstudante_nome.get())
        email = str(self.createEstudante_email.get())
        
        self.cursor.execute(f"""EXECUTE C_ESTUDANTE {matricula}, '{senha}',  '{nome}',  '{email}'""")
        self.cursor.commit()
        self.createEstudante_aviso.configure(text="Cadastro Realizado")
    def R_ESTUDANTE(self):
        
        matricula = self.AuthEstudante_matricula.get()
        retorno = self.cursor.execute(f"""EXECUTE R_ESTUDANTE '{matricula}'""")
        estudante = {"matricula": "", "senha": "", "email": "", "nome": ""}
        for i in retorno:
            estudante["matricula"] = i[0]
            estudante["senha"] = i[1]
            estudante["nome"] = i[2]
            estudante["email"] = i[3]
        return estudante
    def U_ESTUDANTE(self):
        matricula = self.AuthEstudante_matricula.get() if self.AuthEstudante_matricula.get() != "" else self.readEstudante_matricula.cget('text')
        senha = self.updateEstudante_senha.get() if self.updateEstudante_senha.get() != "" else self.readEstudante_senha.cget('text')
        nome = self.updateEstudante_nome.get() if self.updateEstudante_nome.get() != "" else self.readEstudante_nome.cget('text')
        email = self.updateEstudante_email.get() if self.updateEstudante_email.get() != "" else self.readEstudante_email.cget('text')
        
        self.cursor.execute(f"""EXECUTE U_ESTUDANTE {matricula}, '{senha}', '{nome}', '{email}'""")
        self.cursor.commit()
    def D_ESTUDANTE(self):
        
        matricula = self.AuthEstudante_matricula.get()
        retorno = self.cursor.execute(f"""EXECUTE D_ESTUDANTE {matricula}""")
        try:
            for i in retorno:
                resultado = i[0]
            return False
        except:
            self.cursor.commit()
            return True
    
####### PROFESSOR
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
        
        matricula = self.AuthProfessor_matricula.get() if self.AuthProfessor_matricula.get() != "" else self.readProfessor_matricula.cget('text')
        senha = self.updateProfessor_senha.get() if self.updateProfessor_senha.get() != "" else self.readProfessor_senha.cget('text')
        departamento = self.updateProfessor_departamento.get() if self.updateProfessor_departamento.get() != "" else self.readProfessor_departamento.cget('text')
        nome = str(self.updateProfessor_nome.get()) if self.updateProfessor_nome.get() != "" else self.readProfessor_nome.cget('text')
        email = self.updateProfessor_email.get() if self.updateProfessor_email.get() != "" else self.readProfessor_email.cget('text')
        
        self.cursor.execute(f"""UPDATE PROFESSOR SET senha = '{senha}', departamento = {departamento}, nome = '{nome}', email = '{email}' WHERE matricula = {matricula}""")
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

####### DEPARTAMENTO

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
     
        
        
        
########################################################################
##########################    FRONT    #################################
########################################################################

class Front(ctk.CTk, Back):
    
    def __init__(self):
        super().__init__()
        self.config_Tela_Inicial()
        self.conecta_bd()
        self.Frame_ESCOLHA()

    #configurando a janela principal
    def config_Tela_Inicial(self):
        self.geometry("900x500")
        self.title("Sistema de Login")
        self.resizable(False, False)
    
    #########################   NAVEGAÇÃO   ################################

#### Navegação de Login 
    def navega_ESCOLHA_LOGIN_E(self):
        self.escolha_frame.place_forget()
        self.Frame_Auth_ESTUDANTE()  
    def navega_ESCOLHA_LOGIN_P(self):
        self.escolha_frame.place_forget()
        self.Frame_Auth_PROFESSOR()

#### Navegação de cadastro

    def navega_ESTUDANTE_Auth_para_C_(self):
        self.AuthEstudante_frame.place_forget()
        self.Frame_C_ESTUDANTE()  
    def navega_ESTUDANTE_C_para_Auth(self):
        self.createEstudante_frame.place_forget()
        self.Frame_Auth_ESTUDANTE()

    def navega_PROFESSOR_Auth_para_C_(self):
        self.AuthProfessor_frame.place_forget()
        self.Frame_C_PROFESSOR()  
    def navega_PROFESSOR_C_para_Auth(self):
        self.createProfessor_frame.place_forget()
        self.Frame_Auth_PROFESSOR()

#### Navegação do usuario estudante

    def navega_ESTUDANTE_Auth_para_R_(self):
        
        matricula = self.AuthEstudante_matricula.get()
        senha = self.AuthEstudante_senha.get()
        if self.Auth_ESTUDANTE(matricula, senha) == True:
            self.AuthEstudante_frame.place_forget()
            self.Frame_R_ESTUDANTE(self.R_ESTUDANTE())
        elif self.Auth_ESTUDANTE(matricula, senha) == False:
            self.AuthEstudante_aviso.configure(text="Usuario/Senha inválidos")
        else:
            self.AuthEstudante_aviso.configure(text="erro de login")
            
        
    def navega_ESTUDANTE_R_para_Auth_(self):
        self.readEstudante_frame.place_forget()
        self.Frame_Auth_ESTUDANTE()
    def navega_ESTUDANTE_R_para_U_(self):
        self.readEstudante_frame.place_forget()
        self.Frame_U_D_ESTUDANTE(self.R_ESTUDANTE())
    def navega_ESTUDANTE_U_para_R_(self):
        self.updateEstudante_frame.place_forget()
        self.U_ESTUDANTE()
        self.Frame_R_ESTUDANTE(self.R_ESTUDANTE())
    def navega_ESTUDANTE_U_para_Auth_(self):
        if self.D_ESTUDANTE():
            self.updateEstudante_frame.place_forget()
            self.Frame_Auth_ESTUDANTE()
        else:
            self.updateEstudante_aviso.configure(text="Não foi possivel excluir")
    
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

### Navegação do crud de departamento

    def navega_PROFESSOR_R_para_Departamento_(self):
        self.readProfessor_frame.place_forget()
        self.Frame_R_DEPARTAMENTO()
    def navega_DEPARTAMENTO_R_para_U_(self):
        if self.readDepartamento_codigo.get() != "": 
            self.readDepartamento_frame.place_forget()
            self.Frame_U_D_DEPARTAMENTO()
    def navega_DEPARTAMENTO_U_para_R_(self):
        self.R_DEPARTAMENTO()
        self.updateDepartamento_frame.place_forget()
        self.Frame_R_DEPARTAMENTO()
    def navega_DEPARTAMENTO_R_para_C_(self):
        self.readDepartamento_frame.place_forget()
        self.Frame_C_DEPARTAMENTO()
    def navega_DEPARTAMENTO_C_para_R_(self):
        self.createDepartamento_frame.place_forget()
        self.Frame_R_DEPARTAMENTO()
        
    #########################   TELAS   ################################
    
    #Tela de Login
    
    def Frame_ESCOLHA(self):
        
        #frame
        self.escolha_frame = ctk.CTkFrame(self,width=650, height=500)
        self.escolha_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        #widgets
        self.escolha_btn_Professor = ctk.CTkButton(self.escolha_frame, text="Professor", 
                                                       command=self.navega_ESCOLHA_LOGIN_P)
        self.escolha_btn_Professor.grid(row=1, column=1, pady=5, padx=10)
        
        self.escolha_btn_Estudante = ctk.CTkButton(self.escolha_frame, text="Estudante", 
                                                       command=self.navega_ESCOLHA_LOGIN_E)
        self.escolha_btn_Estudante.grid(row=1, column=2, pady=5, padx=10)
        
    def Frame_Auth_ESTUDANTE(self):
        
        #criando frame
        self.AuthEstudante_frame = ctk.CTkFrame(self,width=650, height=500)
        self.AuthEstudante_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        #colocando os widgets
        self.AuthEstudante_title = ctk.CTkLabel(self.AuthEstudante_frame, text="Bem vindo estudante")
        self.AuthEstudante_title.grid(row=1, column=0, pady=10)
        
        self.AuthEstudante_matricula = ctk.CTkEntry(self.AuthEstudante_frame, width=300, placeholder_text= "Matricula")
        self.AuthEstudante_matricula.grid(row=2, column=0, pady=10, padx=10)
        
        self.AuthEstudante_senha = ctk.CTkEntry(self.AuthEstudante_frame, width=300, placeholder_text= "Senha", show="*")
        self.AuthEstudante_senha.grid(row=3, column=0, pady=10, padx=10)
        
        self.AuthEstudante_aviso = ctk.CTkLabel(self.AuthEstudante_frame, text="")
        self.AuthEstudante_aviso.grid(row=4, column=0, pady=5, padx=10)
        
        self.AuthEstudante_btn_login = ctk.CTkButton(self.AuthEstudante_frame, text="Login",
                                                   command=self.navega_ESTUDANTE_Auth_para_R_)
        self.AuthEstudante_btn_login.grid(row=5, column=0, pady=5, padx=10)
        
        self.AuthEstudante_btn_Cadastrar = ctk.CTkButton(self.AuthEstudante_frame, text="Cadastrar", 
                                                       command=self.navega_ESTUDANTE_Auth_para_C_)
        self.AuthEstudante_btn_Cadastrar.grid(row=6, column=0, pady=5, padx=10)

    def Frame_Auth_PROFESSOR(self):
        
        #criando frame
        self.AuthProfessor_frame = ctk.CTkFrame(self,width=650, height=500)
        self.AuthProfessor_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        #colocando os widgets
        self.AuthProfessor_title = ctk.CTkLabel(self.AuthProfessor_frame, text="Bem vindo Professor")
        self.AuthProfessor_title.grid(row=1, column=0, pady=10)
        
        self.AuthProfessor_matricula = ctk.CTkEntry(self.AuthProfessor_frame, width=300, placeholder_text= "Matricula")
        self.AuthProfessor_matricula.grid(row=2, column=0, pady=10, padx=10)
        
        self.AuthProfessor_senha = ctk.CTkEntry(self.AuthProfessor_frame, width=300, placeholder_text= "Senha", show="*")
        self.AuthProfessor_senha.grid(row=3, column=0, pady=10, padx=10)
        
        self.AuthProfessor_aviso = ctk.CTkLabel(self.AuthProfessor_frame, text="")
        self.AuthProfessor_aviso.grid(row=4, column=0, pady=5, padx=10)
        
        self.AuthProfessor_btn_login = ctk.CTkButton(self.AuthProfessor_frame, text="Login",
                                                   command=self.navega_PROFESSOR_Auth_para_R_)
        self.AuthProfessor_btn_login.grid(row=5, column=0, pady=5, padx=10)
        
        self.AuthProfessor_btn_Cadastrar = ctk.CTkButton(self.AuthProfessor_frame, text="Cadastrar", 
                                                       command=self.navega_PROFESSOR_Auth_para_C_)
        self.AuthProfessor_btn_Cadastrar.grid(row=6, column=0, pady=5, padx=10)
        
######## CRUD ESTUDANTE ##########


    def Frame_C_ESTUDANTE(self):
        
        #criando frame
        self.createEstudante_frame = ctk.CTkFrame(self, width=650, height=500)
        self.createEstudante_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        #Inserindo widgets
        self.createEstudante_title = ctk.CTkLabel(self.createEstudante_frame, text="Cadastre-se")
        self.createEstudante_title.grid(row=1, column=0, pady=10)
        
        self.createEstudante_matricula = ctk.CTkEntry(self.createEstudante_frame, width=300, placeholder_text= "Matricula")
        self.createEstudante_matricula.grid(row=2, column=0, pady=10, padx=10)
        
        self.createEstudante_senha = ctk.CTkEntry(self.createEstudante_frame, width=300, placeholder_text= "Senha", show="*")
        self.createEstudante_senha.grid(row=3, column=0, pady=10, padx=10)
        
        self.createEstudante_email = ctk.CTkEntry(self.createEstudante_frame, width=300, placeholder_text= "email")
        self.createEstudante_email.grid(row=4, column=0, pady=10, padx=10)
        
        self.createEstudante_nome = ctk.CTkEntry(self.createEstudante_frame, width=300, placeholder_text= "nome")
        self.createEstudante_nome.grid(row=5, column=0, pady=10, padx=10)
        
        self.createEstudante_aviso = ctk.CTkLabel(self.createEstudante_frame, text="")
        self.createEstudante_aviso.grid(row=6, column=0, pady=5, padx=10)
        
        self.createEstudante_btn_cadastrar = ctk.CTkButton(self.createEstudante_frame, text="Cadastrar", command = self.C_ESTUDANTE)
        self.createEstudante_btn_cadastrar.grid(row=7, column=0, pady=5, padx=10)
        
        self.createEstudante_btn_voltaLoginEstudante = ctk.CTkButton(self.createEstudante_frame, text="Voltar para tela de login",
                                                                     command=self.navega_ESTUDANTE_C_para_Auth)
        self.createEstudante_btn_voltaLoginEstudante.grid(row=8, column=0, pady=5, padx=10)
     
    def Frame_R_ESTUDANTE(self, estudante):
        
        #criando frame
        self.readEstudante_frame = ctk.CTkFrame(self, width=650, height=500)
        self.readEstudante_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        #Inserindo widgets
        self.readEstudante_title = ctk.CTkLabel(self.readEstudante_frame, text="Bem vindo")
        self.readEstudante_title.grid(row=1, column=1, columnspan=2, pady=10)
        
        self.readEstudante_label_matricula = ctk.CTkLabel(self.readEstudante_frame, text="Matricula: ")
        self.readEstudante_label_matricula.grid(row=2, column=1, pady=10)
        self.readEstudante_matricula = ctk.CTkLabel(self.readEstudante_frame, width=300, text = estudante["matricula"])
        self.readEstudante_matricula.grid(row=2, column=2, pady=10, padx=10)
        
        self.readEstudante_label_senha = ctk.CTkLabel(self.readEstudante_frame, text="Senha: ")
        self.readEstudante_label_senha.grid(row=3, column=1, pady=10)
        self.readEstudante_senha = ctk.CTkLabel(self.readEstudante_frame, width=300, text = estudante["senha"])
        self.readEstudante_senha.grid(row=3, column=2, pady=10, padx=10)
        
        self.readEstudante_label_email = ctk.CTkLabel(self.readEstudante_frame, text="Email: ")
        self.readEstudante_label_email.grid(row=4, column=1, pady=10)
        self.readEstudante_email = ctk.CTkLabel(self.readEstudante_frame, width=300, text = estudante["email"])
        self.readEstudante_email.grid(row=4, column=2, pady=10, padx=10)
        
        self.readEstudante_label_nome = ctk.CTkLabel(self.readEstudante_frame, text="Nome: ")
        self.readEstudante_label_nome.grid(row=5, column=1, pady=10)
        self.readEstudante_nome = ctk.CTkLabel(self.readEstudante_frame, width=300, text = estudante["nome"])
        self.readEstudante_nome.grid(row=5, column=2, pady=10, padx=10)
        
        self.readEstudante_aviso = ctk.CTkLabel(self.readEstudante_frame, text="")
        self.readEstudante_aviso.grid(row=6, column=1, columnspan=2, pady=5, padx=10)
        
        self.readEstudante_btn_UpdateEstudante = ctk.CTkButton(self.readEstudante_frame, text="Editar Dados", 
                                                               command = self.navega_ESTUDANTE_R_para_U_)
        self.readEstudante_btn_UpdateEstudante.grid(row=7, column=1,columnspan=2, pady=5, padx=10)

    def Frame_U_D_ESTUDANTE(self, estudante):
        
        #criando frame
        self.updateEstudante_frame = ctk.CTkFrame(self, width=650, height=500)
        self.updateEstudante_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        #Inserindo widgets
        self.updateEstudante_title = ctk.CTkLabel(self.updateEstudante_frame, text="Atualize seus dados")
        self.updateEstudante_title.grid(row=1, column=0, pady=10)
        
        matricula_var = tk.StringVar()
        matricula_var = estudante["matricula"]
        self.updateEstudante_matricula = ctk.CTkEntry(self.updateEstudante_frame, width=300, placeholder_text= estudante["matricula"])
        self.updateEstudante_matricula.grid(row=2, column=0, pady=10, padx=10)
        
        self.updateEstudante_senha = ctk.CTkEntry(self.updateEstudante_frame, width=300, placeholder_text= estudante["senha"])
        self.updateEstudante_senha.grid(row=3, column=0, pady=10, padx=10)
        
        self.updateEstudante_email = ctk.CTkEntry(self.updateEstudante_frame, width=300, placeholder_text= estudante["email"])
        self.updateEstudante_email.grid(row=4, column=0, pady=10, padx=10)
        
        self.updateEstudante_nome = ctk.CTkEntry(self.updateEstudante_frame, width=300, placeholder_text= estudante["nome"])
        self.updateEstudante_nome.grid(row=5, column=0, pady=10, padx=10)
        
        self.updateEstudante_aviso = ctk.CTkLabel(self.updateEstudante_frame, text="")
        self.updateEstudante_aviso.grid(row=6, column=0, pady=5, padx=10)
        
        self.updateEstudante_btn_save = ctk.CTkButton(self.updateEstudante_frame, text="Salvar", command=self.navega_ESTUDANTE_U_para_R_)
        self.updateEstudante_btn_save.grid(row=7, column=0, pady=5, padx=10)
        
        self.updateEstudante_btn_Delete = ctk.CTkButton(self.updateEstudante_frame, text="Deletar conta", 
                                                                 command = self.navega_ESTUDANTE_U_para_Auth_)
        self.updateEstudante_btn_Delete.grid(row=8, column=0, pady=5, padx=10)
        
        self.updateEstudante_btn_readEstudante = ctk.CTkButton(self.updateEstudante_frame, text="Retornar", 
                                                                 command = self.navega_ESTUDANTE_U_para_R_)
        self.updateEstudante_btn_readEstudante.grid(row=9, column=0, pady=5, padx=10)
    
    
######## CRUD PROFESSOR ############

    def Frame_C_PROFESSOR(self):

        #criando frame
        self.createProfessor_frame = ctk.CTkFrame(self, width=650, height=500)
        self.createProfessor_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        #Inserindo widgets
        self.createProfessor_title = ctk.CTkLabel(self.createProfessor_frame, text="Cadastre-se")
        self.createProfessor_title.grid(row=1, column=0, pady=10)
        
        self.createProfessor_matricula = ctk.CTkEntry(self.createProfessor_frame, width=300, placeholder_text= "Matricula")
        self.createProfessor_matricula.grid(row=2, column=0, pady=10, padx=10)
        
        self.createProfessor_senha = ctk.CTkEntry(self.createProfessor_frame, width=300, placeholder_text= "Senha", show="*")
        self.createProfessor_senha.grid(row=3, column=0, pady=10, padx=10)
        
        self.createProfessor_departamento = ctk.CTkEntry(self.createProfessor_frame, width=300, placeholder_text= "departamento")
        self.createProfessor_departamento.grid(row=4, column=0, pady=10, padx=10)
        
        self.createProfessor_nome = ctk.CTkEntry(self.createProfessor_frame, width=300, placeholder_text= "nome")
        self.createProfessor_nome.grid(row=5, column=0, pady=10, padx=10)
        
        self.createProfessor_email = ctk.CTkEntry(self.createProfessor_frame, width=300, placeholder_text= "email")
        self.createProfessor_email.grid(row=6, column=0, pady=10, padx=10)
        
        self.createProfessor_aviso = ctk.CTkLabel(self.createProfessor_frame, text="")
        self.createProfessor_aviso.grid(row=7, column=0, pady=5, padx=10)
        
        self.createProfessor_btn_CreateProfessor = ctk.CTkButton(self.createProfessor_frame, text="Cadastrar", command = self.C_PROFESSOR)
        self.createProfessor_btn_CreateProfessor.grid(row=8, column=0, pady=5, padx=10)
        
        self.createProfessor_btn_voltaLoginProfessor = ctk.CTkButton(self.createProfessor_frame, text="Voltar para tela de login", 
                                                                     command=self.navega_PROFESSOR_C_para_Auth)
        self.createProfessor_btn_voltaLoginProfessor.grid(row=9, column=0, pady=5, padx=10)  
    
    def Frame_R_PROFESSOR(self, professor):  
        #criando frame
        self.readProfessor_frame = ctk.CTkFrame(self, width=650, height=500)
        self.readProfessor_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        #Inserindo widgets
        self.readProfessor_title = ctk.CTkLabel(self.readProfessor_frame, text="Bem vindo")
        self.readProfessor_title.grid(row=1, column=1, columnspan=2, pady=10)
        
        self.readProfessor_label_matricula = ctk.CTkLabel(self.readProfessor_frame, text="Matricula: ")
        self.readProfessor_label_matricula.grid(row=2, column=1, pady=10)
        self.readProfessor_matricula = ctk.CTkLabel(self.readProfessor_frame, width=300, text = professor["matricula"])
        self.readProfessor_matricula.grid(row=2, column=2, pady=10, padx=10)
        
        self.readProfessor_label_senha = ctk.CTkLabel(self.readProfessor_frame, text="Senha: ")
        self.readProfessor_label_senha.grid(row=3, column=1, pady=10)
        self.readProfessor_senha = ctk.CTkLabel(self.readProfessor_frame, width=300, text = professor["senha"])
        self.readProfessor_senha.grid(row=3, column=2, pady=10, padx=10)
        
        self.readProfessor_label_departamento = ctk.CTkLabel(self.readProfessor_frame, text="Departamento: ")
        self.readProfessor_label_departamento.grid(row=4, column=1, pady=10)
        self.readProfessor_departamento = ctk.CTkLabel(self.readProfessor_frame, width=300, text = professor["departamento"])
        self.readProfessor_departamento.grid(row=4, column=2, pady=10, padx=10)
        
        self.readProfessor_label_nome = ctk.CTkLabel(self.readProfessor_frame, text="Nome: ")
        self.readProfessor_label_nome.grid(row=5, column=1, pady=10)
        self.readProfessor_nome = ctk.CTkLabel(self.readProfessor_frame, width=300, text = professor["nome"])
        self.readProfessor_nome.grid(row=5, column=2, pady=10, padx=10)
        
        self.readProfessor_label_email = ctk.CTkLabel(self.readProfessor_frame, text="Email: ")
        self.readProfessor_label_email.grid(row=6, column=1, pady=10)
        self.readProfessor_email = ctk.CTkLabel(self.readProfessor_frame, width=300, text = professor["email"])
        self.readProfessor_email.grid(row=6, column=2, pady=10, padx=10)
        
        self.readProfessor_aviso = ctk.CTkLabel(self.readProfessor_frame, text="")
        self.readProfessor_aviso.grid(row=6, column=1, columnspan=2, pady=5, padx=10)
        
        self.readProfessor_btn_UpdateProfessor = ctk.CTkButton(self.readProfessor_frame, text="Editar Dados", 
                                                               command = self.navega_PROFESSOR_R_para_U_)
        self.readProfessor_btn_UpdateProfessor.grid(row=7, column=1, columnspan=2, pady=5, padx=10)
        
        self.readProfessor_btn_ReadTurma = ctk.CTkButton(self.readProfessor_frame, text="Gerenciar Departamentos",
                                                         command=self.navega_PROFESSOR_R_para_Departamento_)
        self.readProfessor_btn_ReadTurma.grid(row=8, column=1, columnspan=2, pady=5, padx=10)
        
    def Frame_U_D_PROFESSOR(self, professor):
        
        #criando frame
        self.updateProfessor_frame = ctk.CTkFrame(self, width=650, height=500)
        self.updateProfessor_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        #Inserindo widgets
        self.updateProfessor_title = ctk.CTkLabel(self.updateProfessor_frame, text="Atualize seus dados")
        self.updateProfessor_title.grid(row=1, column=0, pady=10)
        
        self.updateProfessor_matricula = ctk.CTkEntry(self.updateProfessor_frame, width=300, placeholder_text= professor["matricula"])
        self.updateProfessor_matricula.grid(row=2, column=0, pady=10, padx=10)
        
        self.updateProfessor_senha = ctk.CTkEntry(self.updateProfessor_frame, width=300, placeholder_text= professor["senha"])
        self.updateProfessor_senha.grid(row=3, column=0, pady=10, padx=10)
        
        self.updateProfessor_departamento = ctk.CTkEntry(self.updateProfessor_frame, width=300, placeholder_text= professor["departamento"])
        self.updateProfessor_departamento.grid(row=4, column=0, pady=10, padx=10)
        
        self.updateProfessor_nome = ctk.CTkEntry(self.updateProfessor_frame, width=300, placeholder_text= professor["nome"])
        self.updateProfessor_nome.grid(row=5, column=0, pady=10, padx=10)
        
        self.updateProfessor_email = ctk.CTkEntry(self.updateProfessor_frame, width=300, placeholder_text= professor["email"])
        self.updateProfessor_email.grid(row=6, column=0, pady=10, padx=10)
        
        self.updateProfessor_aviso = ctk.CTkLabel(self.updateProfessor_frame, text="")
        self.updateProfessor_aviso.grid(row=6, column=0, pady=5, padx=10)
        
        self.updateProfessor_btn_save = ctk.CTkButton(self.updateProfessor_frame, text="Salvar", command=self.navega_PROFESSOR_U_para_R_)
        self.updateProfessor_btn_save.grid(row=7, column=0, pady=5, padx=10)
        
        self.updateProfessor_btn_Delete = ctk.CTkButton(self.updateProfessor_frame, text="Deletar conta", 
                                                                 command = self.navega_PROFESSOR_U_para_Auth_)
        self.updateProfessor_btn_Delete.grid(row=8, column=0, pady=5, padx=10)
        
        self.updateProfessor_btn_readProfessor = ctk.CTkButton(self.updateProfessor_frame, text="Retornar", 
                                                                 command = self.navega_PROFESSOR_U_para_R_)
        self.updateProfessor_btn_readProfessor.grid(row=9, column=0, pady=5, padx=10)
        
######## CRUD DEPARTAMENTO #########

    def Frame_C_DEPARTAMENTO(self):
        
        #criando frame
        self.createDepartamento_frame = ctk.CTkFrame(self, width=650, height=500)
        self.createDepartamento_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        #widgets
        self.createDepartamento_title = ctk.CTkLabel(self.createDepartamento_frame, text="Criar novo departamento")
        self.createDepartamento_title.grid(row=1, column=0,columnspan=2, pady=10)
        
        self.createDepartamento_codigo = ctk.CTkEntry(self.createDepartamento_frame, width=300, placeholder_text= "Codigo")
        self.createDepartamento_codigo.grid(row=2, column=0, columnspan=2,pady=10, padx=10)
        
        self.createDepartamento_nome = ctk.CTkEntry(self.createDepartamento_frame, width=300, placeholder_text= "Nome")
        self.createDepartamento_nome.grid(row=3, column=0,columnspan=2, pady=10, padx=10)
        
        self.createDepartamento_aviso = ctk.CTkLabel(self.createDepartamento_frame, text="")
        self.createDepartamento_aviso.grid(row=4, column=0,columnspan=2, pady=10)
        
        self.createDepartamento_btn_create = ctk.CTkButton(self.createDepartamento_frame, text="Salvar", command=self.C_DEPARTAMENTO)
        self.createDepartamento_btn_create.grid(row=5, column=0, pady=5, padx=10)
        
        self.createDepartamento_btn_return = ctk.CTkButton(self.createDepartamento_frame, text="Retornar", 
                                                                 command = self.navega_DEPARTAMENTO_C_para_R_)
        self.createDepartamento_btn_return.grid(row=5, column=1,  pady=5, padx=10)
    
    def Frame_R_DEPARTAMENTO(self):
        #criando frame
        self.readDepartamento_frame = ctk.CTkFrame(self, width=650, height=500)
        self.readDepartamento_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        #Inserindo widgets
        self.readDepartamento_title = ctk.CTkLabel(self.readDepartamento_frame, text="Selecione um departamento")
        self.readDepartamento_title.grid(row=1, column=1, pady=10)
        
        self.readDepartamento_codigo = ctk.CTkEntry(self.readDepartamento_frame, width=300, placeholder_text= "Departamento...")
        self.readDepartamento_codigo.grid(row=1, column=2, pady=10, padx=10)
        
        self.readDepartamento_btn_read = ctk.CTkButton(self.readDepartamento_frame, text="Selecionar", 
                                                                 command = self.R_DEPARTAMENTO)
        self.readDepartamento_btn_read.grid(row=2, column=1, pady=5, padx=10)
        
        self.readDepartamento_nome = ctk.CTkLabel(self.readDepartamento_frame, text="NOME DO DEPARTAMENTO: ")
        self.readDepartamento_nome.grid(row=3, column=1, pady=10)
        
        self.readDepartamento_nome2 = ctk.CTkLabel(self.readDepartamento_frame, text="")
        self.readDepartamento_nome2.grid(row=3, column=2, pady=10)
        
        self.readDepartamento_btn_update = ctk.CTkButton(self.readDepartamento_frame, text="Alterar", 
                                                                 command = self.navega_DEPARTAMENTO_R_para_U_)
        self.readDepartamento_btn_update.grid(row=4, column=1, pady=5, padx=10)
        
        self.readDepartamento_btn_create = ctk.CTkButton(self.readDepartamento_frame, text="Criar", 
                                                                 command = self.navega_DEPARTAMENTO_R_para_C_)
        self.readDepartamento_btn_create.grid(row=4,column=2, pady=5, padx=10)
        
        
        
        tabela = ttk.Treeview(self.readDepartamento_frame, selectmode="browse", column=("codigo", "nome"), show='headings')
        tabela.grid(row=6, column= 1, columnspan=2, pady=5, padx=10)
        
        tabela.heading("#1", text="codigo")
        tabela.heading("#2", text="nome")
        
        resultados = self.cursor.execute(f"""SELECT * FROM DEPARTAMENTO""")
        lista_resultados = [list(row) for row in resultados]
        
        for(codigo, nome) in lista_resultados:
            tabela.insert("","end",values=(codigo, nome))

            
    def Frame_U_D_DEPARTAMENTO(self):
        
        #criando frame
        self.updateDepartamento_frame = ctk.CTkFrame(self, width=650, height=500)
        self.updateDepartamento_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        #widgets
        self.updateDepartamento_title = ctk.CTkLabel(self.updateDepartamento_frame, text="Altere os dados do Departamento")
        self.updateDepartamento_title.grid(row=1, column=0, pady=10)
        
        self.updateDepartamento_codigo = ctk.CTkEntry(self.updateDepartamento_frame, width=300, placeholder_text= "Codigo")
        self.updateDepartamento_codigo.grid(row=2, column=0, pady=10, padx=10)
        
        self.updateDepartamento_nome = ctk.CTkEntry(self.updateDepartamento_frame, width=300, placeholder_text= "Nome")
        self.updateDepartamento_nome.grid(row=3, column=0, pady=10, padx=10)
        
        self.updateDepartamento_aviso = ctk.CTkLabel(self.updateDepartamento_frame, text="")
        self.updateDepartamento_aviso.grid(row=4, column=0, pady=10)
        
        self.updateDepartamento_btn_update = ctk.CTkButton(self.updateDepartamento_frame, text="Salvar", command=self.U_DEPARTAMENTO)
        self.updateDepartamento_btn_update.grid(row=5, column=0, pady=5, padx=10)
        
        self.updateDepartamento_btn_update = ctk.CTkButton(self.updateDepartamento_frame, text="Deletar Departamento", 
                                                                 command = self.D_DEPARTAMENTO)
        self.updateDepartamento_btn_update.grid(row=6, column=0, pady=5, padx=10)
        
        self.updateDepartamento_btn_update = ctk.CTkButton(self.updateDepartamento_frame, text="Retornar", 
                                                                 command = self.navega_DEPARTAMENTO_U_para_R_)
        self.updateDepartamento_btn_update.grid(row=7, column=0, pady=5, padx=10)
        

########################################################################
##########################    MAIN    ##################################
########################################################################

if __name__ == "__main__":
    
    app = Front()
    app.mainloop()