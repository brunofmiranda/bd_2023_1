import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from back_end import Back
from interface import interface

########################################################################
##########################    FRONT    #################################
########################################################################

class Front(ctk.CTk, interface):
    
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
    
############# LOGIN
    
    def Frame_ESCOLHA(self):
        
        #frame
        self.escolha_frame = ctk.CTkFrame(self,width=650, height=500)
        self.escolha_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        #widgets
        self.escolha_btn_Professor = ctk.CTkButton(self.escolha_frame, text="Professor", 
                                                       command=self.navega_ESCOLHA_para_Auth_P_)
        self.escolha_btn_Professor.grid(row=1, column=1, pady=5, padx=10)
        
        self.escolha_btn_Estudante = ctk.CTkButton(self.escolha_frame, text="Estudante", 
                                                       command=self.navega_ESCOLHA_para_Auth_E_)
        self.escolha_btn_Estudante.grid(row=1, column=2, pady=5, padx=10)
        
    def Frame_Auth_ESTUDANTE(self):
        
        #criando frame
        self.AuthEstudante_frame = ctk.CTkFrame(self,width=650, height=500)
        self.AuthEstudante_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        #colocando os widgets
        self.AuthEstudante_title = ctk.CTkLabel(self.AuthEstudante_frame, text="Bem vindo")
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
        
        self.AuthEstudante_btn_return = ctk.CTkButton(self.AuthEstudante_frame, text="Retornar", 
                                                       command=self.navega_ESTUDANTE_Auth_para_ESCOLHA_)
        self.AuthEstudante_btn_return.grid(row=7, column=0, pady=5, padx=10)

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
        
        self.AuthProfessor_btn_return = ctk.CTkButton(self.AuthProfessor_frame, text="Retornar", 
                                                       command=self.navega_PROFESSOR_Auth_para_ESCOLHA_)
        self.AuthProfessor_btn_return.grid(row=7, column=0, pady=5, padx=10)
    
########################################################################
######################    ROTA PROFESSOR   #############################
########################################################################

############# CRUD PROFESSOR

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
        
    def Frame_U_D_PROFESSOR(self, professor):
        
        #criando frame
        self.updateProfessor_frame = ctk.CTkFrame(self, width=650, height=500)
        self.updateProfessor_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        #Inserindo widgets
        self.updateProfessor_title = ctk.CTkLabel(self.updateProfessor_frame, text="Atualize seus dados")
        self.updateProfessor_title.grid(row=1, column=1,columnspan=2, pady=10)
        
        self.updateProfessor_label_senha = ctk.CTkLabel(self.updateProfessor_frame, text="Senha: ")
        self.updateProfessor_label_senha.grid(row=2, column=1, pady=10)
        self.updateProfessor_senha = ctk.CTkEntry(self.updateProfessor_frame, width=300, placeholder_text= professor["senha"])
        self.updateProfessor_senha.grid(row=2, column=2, pady=10, padx=10)
        
        self.updateProfessor_label_departamento = ctk.CTkLabel(self.updateProfessor_frame, text="Departamento: ")
        self.updateProfessor_label_departamento.grid(row=3, column=1, pady=10)
        
        self.updateProfessor_departamento = ctk.CTkComboBox(self.updateProfessor_frame, values = self.V_DEPARTAMENTO_())
        self.updateProfessor_departamento.grid(row=3, column=2, pady=10, padx=10)
        
        self.updateProfessor_label_nome = ctk.CTkLabel(self.updateProfessor_frame, text="Nome: ")
        self.updateProfessor_label_nome.grid(row=4, column=1, pady=10)
        self.updateProfessor_nome = ctk.CTkEntry(self.updateProfessor_frame, width=300, placeholder_text= professor["nome"])
        self.updateProfessor_nome.grid(row=4, column=2, pady=10, padx=10)
        
        self.updateProfessor_label_email = ctk.CTkLabel(self.updateProfessor_frame, text="Email: ")
        self.updateProfessor_label_email.grid(row=5, column=1, pady=10)
        self.updateProfessor_email = ctk.CTkEntry(self.updateProfessor_frame, width=300, placeholder_text= professor["email"])
        self.updateProfessor_email.grid(row=5, column=2, pady=10, padx=10)
        
        self.updateProfessor_aviso = ctk.CTkLabel(self.updateProfessor_frame, text="")
        self.updateProfessor_aviso.grid(row=6, column=1, columnspan=2, pady=5, padx=10)
        
        self.updateProfessor_btn_save = ctk.CTkButton(self.updateProfessor_frame, text="Salvar", command=self.navega_PROFESSOR_U_para_R_)
        self.updateProfessor_btn_save.grid(row=7, column=1, pady=5, padx=10)
        
        self.updateProfessor_btn_Delete = ctk.CTkButton(self.updateProfessor_frame, text="Deletar conta", 
                                                                 command = self.navega_PROFESSOR_U_para_Auth_)
        self.updateProfessor_btn_Delete.grid(row=7, column=2, pady=5, padx=10)
        
        self.updateProfessor_btn_readProfessor = ctk.CTkButton(self.updateProfessor_frame, text="Retornar", 
                                                                 command = self.navega_PROFESSOR_U_para_R_)
        self.updateProfessor_btn_readProfessor.grid(row=8, column=1, columnspan=2, pady=5, padx=10)
        
   
############# R TURMA
  
    def Frame_R_TURMA(self, turma):
        
        #criando frame
        self.readTurma_frame = ctk.CTkFrame(self, width=650, height=500)
        self.readTurma_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        #Inserindo widgets
        
        self.readTurma_label_turma = ctk.CTkLabel(self.readTurma_frame, text="Selecione uma Turma: ")
        self.readTurma_label_turma.grid(row=1, column=1, pady=10)
        self.readTurma_cb_turma = ctk.CTkComboBox(self.readTurma_frame, values = turma)
        self.readTurma_cb_turma.grid(row=1, column=2, pady=10, padx=10)
        
        self.readTurma_btn_adm = ctk.CTkButton(self.readTurma_frame, text="Visualizar Avaliações", command = self.navega_R_TURMA_para_R_AVALIACAO_)
        self.readTurma_btn_adm.grid(row=2, column=1, columnspan = 2, pady=5, padx=10)
        
        self.readTurma_btn_adm = ctk.CTkButton(self.readTurma_frame, text="Retornar", command = self.navega_R_AVALIACAO_para_R_TURMA_)
        self.readTurma_btn_adm.grid(row=3, column=1, columnspan = 2, pady=5, padx=10)

     
########################################################################
######################    ROTA ESTUDANTE   #############################
########################################################################

############# CRUD ESTUDANTE

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
        
        self.createEstudante_btn_cadastrar = ctk.CTkButton(self.createEstudante_frame, text="Cadastrar", command = self.navega_ESTUDANTE_CA_para_Auth_)
        self.createEstudante_btn_cadastrar.grid(row=7, column=0, pady=5, padx=10)
        
        self.createEstudante_btn_return = ctk.CTkButton(self.createEstudante_frame, text="Voltar para tela de login",
                                                                     command=self.navega_ESTUDANTE_C_para_Auth_)
        self.createEstudante_btn_return.grid(row=8, column=0, pady=5, padx=10)
     
    def Frame_R_ESTUDANTE(self, estudante):
        
        #criando frame
        self.readEstudante_frame = ctk.CTkFrame(self, width=650, height=500)
        self.readEstudante_frame.place(relx=0.5, rely=0.5, anchor='center')
        

        #Inserindo widgets
        self.readEstudante_title = ctk.CTkLabel(self.readEstudante_frame, text="Bem vindo, Estudante")
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
        
        self.readEstudante_btn_readTurma = ctk.CTkButton(self.readEstudante_frame, text="Visualizar Turmas", 
                                                               command = self.navega_ESTUDANTE_R_para_R_TURMA_)
        self.readEstudante_btn_readTurma.grid(row=8, column=1,columnspan=2, pady=5, padx=10)
        
        self.readEstudante_btn_UpdateEstudante = ctk.CTkButton(self.readEstudante_frame, text="Sair", 
                                                               command = self.navega_ESTUDANTE_R_para_Auth_)
        self.readEstudante_btn_UpdateEstudante.grid(row=9, column=1,columnspan=2, pady=5, padx=10)

    def Frame_U_D_ESTUDANTE(self, estudante):
        
        #criando frame
        self.updateEstudante_frame = ctk.CTkFrame(self, width=650, height=500)
        self.updateEstudante_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        #Inserindo widgets
        self.updateEstudante_title = ctk.CTkLabel(self.updateEstudante_frame, text="Atualize seus dados")
        self.updateEstudante_title.grid(row=1, column=1,columnspan=2, pady=10)
        
        self.updateEstudante_matricula = ctk.CTkLabel(self.updateEstudante_frame, text="Matricula: ")
        self.updateEstudante_matricula.grid(row=2, column=1,columnspan=2, pady=10)
        self.updateEstudante_matricula = ctk.CTkLabel(self.updateEstudante_frame, text=estudante["matricula"])
        self.updateEstudante_matricula.grid(row=2, column=2,columnspan=2, pady=10)
        
        self.updateEstudante_label_senha = ctk.CTkLabel(self.updateEstudante_frame, text="Senha: ")
        self.updateEstudante_label_senha.grid(row=3, column=1, pady=10)
        self.updateEstudante_senha = ctk.CTkEntry(self.updateEstudante_frame, width=300, placeholder_text= estudante["senha"])
        self.updateEstudante_senha.grid(row=3, column=2, pady=10, padx=10)
        
        self.updateEstudante_label_email = ctk.CTkLabel(self.updateEstudante_frame, text="Email: ")
        self.updateEstudante_label_email.grid(row=4, column=1, pady=10)
        self.updateEstudante_email = ctk.CTkEntry(self.updateEstudante_frame, width=300, placeholder_text= estudante["email"])
        self.updateEstudante_email.grid(row=4, column=2, pady=10, padx=10)
        
        self.updateEstudante_label_nome = ctk.CTkLabel(self.updateEstudante_frame, text="Nome: ")
        self.updateEstudante_label_nome.grid(row=5, column=1, pady=10)
        self.updateEstudante_nome = ctk.CTkEntry(self.updateEstudante_frame, width=300, placeholder_text= estudante["nome"])
        self.updateEstudante_nome.grid(row=5, column=2, pady=10, padx=10)
        
        
        self.updateEstudante_aviso = ctk.CTkLabel(self.updateEstudante_frame, text="")
        self.updateEstudante_aviso.grid(row=6, column=1,columnspan=2, pady=5, padx=10)
        
        self.updateEstudante_btn_save = ctk.CTkButton(self.updateEstudante_frame, text="Salvar", command=self.navega_ESTUDANTE_U_para_R_)
        self.updateEstudante_btn_save.grid(row=7, column=1, pady=5, padx=10)
        
        self.updateEstudante_btn_Delete = ctk.CTkButton(self.updateEstudante_frame, text="Deletar conta", 
                                                                 command = self.navega_ESTUDANTE_U_para_Auth_)
        self.updateEstudante_btn_Delete.grid(row=7, column=2, pady=5, padx=10)
        
        self.updateEstudante_btn_readEstudante = ctk.CTkButton(self.updateEstudante_frame, text="Retornar", 
                                                                 command = self.navega_ESTUDANTE_U_para_R_)
        self.updateEstudante_btn_readEstudante.grid(row=8, column=1, columnspan=2, pady=5, padx=10)
    
############# CRUD AVALIACAO     
 
    def Frame_C_AVALIACAO(self, turma):
        
        #criando frame
        self.createAvaliacao_frame = ctk.CTkFrame(self, width=650, height=500)
        self.createAvaliacao_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        #Inserindo widgets
        self.createAvaliacao_turma1 = ctk.CTkLabel(self.createAvaliacao_frame, text="TURMA: ")
        self.createAvaliacao_turma1.grid(row=1, column=1,  pady=10)
        
        self.createAvaliacao_turma2 = ctk.CTkLabel(self.createAvaliacao_frame, text= turma)
        self.createAvaliacao_turma2.grid(row=1, column=2, pady=10)
        
        self.createAvaliacao_avaliacao = ctk.CTkEntry(self.createAvaliacao_frame, placeholder_text="Novo comentario...")
        self.createAvaliacao_avaliacao.grid(row=2, column=1,columnspan = 2, pady=10)
        
        self.createAvaliacao_aviso = ctk.CTkLabel(self.createAvaliacao_frame, text="")
        self.createAvaliacao_aviso.grid(row=1, column=2, pady=10)
        
        self.createAvaliacao_btn_criar_av = ctk.CTkButton(self.createAvaliacao_frame, text="Cadastrar como avaliação", command = self.navega_CAv_AVALIACAO_para_R_AVALIACAO_)
        self.createAvaliacao_btn_criar_av.grid(row=3, column=1, pady=5, padx=10)
        
        self.createAvaliacao_btn_criar_denuncia = ctk.CTkButton(self.createAvaliacao_frame, text="Cadastrar como Denúncia", command = self.navega_CDen_AVALIACAO_para_R_AVALIACAO_)
        self.createAvaliacao_btn_criar_denuncia.grid(row=3, column=2, pady=5, padx=10)
        
        self.createAvaliacao_btn_return = ctk.CTkButton(self.createAvaliacao_frame, text="Retornar", command = self.navega_C_AVALIACAO_para_R_AVALIACAO_)
        self.createAvaliacao_btn_return.grid(row=4, column=1, columnspan = 2, pady=5, padx=10)

    def Frame_R_AVALIACAO(self, turma, avaliacoes):
        
        #criando frame
        self.readAvaliacao_frame = ctk.CTkFrame(self, width=650, height=500)
        self.readAvaliacao_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        #Inserindo widgets
        self.readAvaliacao_turma1 = ctk.CTkLabel(self.readAvaliacao_frame, text="TURMA: ")
        self.readAvaliacao_turma1.grid(row=1, column=1,  pady=10)
        
        self.readAvaliacao_turma2 = ctk.CTkLabel(self.readAvaliacao_frame, text= turma)
        self.readAvaliacao_turma2.grid(row=1, column=2, pady=10)
        
        self.readAvaliacao_btn_create = ctk.CTkButton(self.readAvaliacao_frame, text="Novo comentário", command = self.navega_R_AVALIACAO_para_C_AVALIACAO_)
        self.readAvaliacao_btn_create.grid(row=2, column=1, pady=5, padx=10)
        
        self.readAvaliacao_btn_updateDelete = ctk.CTkButton(self.readAvaliacao_frame, text="Editar ou excluir meus comentários", command = self.navega_R_AVALIACAO_para_U_D_AVALIACAO_)
        self.readAvaliacao_btn_updateDelete.grid(row=2, column=2, pady=5, padx=10)
        
        self.readAvaliacao_btn_updateDelete = ctk.CTkButton(self.readAvaliacao_frame, text="Retornar")
        self.readAvaliacao_btn_updateDelete.grid(row=3, column=2, columnspan = 2, pady=5, padx=10)
        
        
        
        tv = ttk.Treeview(self.readAvaliacao_frame, columns=("matricula", "avaliacao"), show = "headings")
        tv.grid(row = 4, column = 1, columnspan = 2)
        tv.heading('matricula', text = 'Matricula')
        tv.heading('avaliacao', text = 'Avaliação')
        
        for registro in avaliacoes:
            tv.insert("", "end", values = registro)

    def Frame_U_D_AVALIACAO(self, avaliacoes):
        #criando frame
        self.updateDeleteAvaliacao_frame = ctk.CTkFrame(self, width=650, height=500)
        self.updateDeleteAvaliacao_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        #Inserindo widgets
        self.updateDeleteAvaliacao_label_id = ctk.CTkLabel(self.updateDeleteAvaliacao_frame, text="Selecione o id da avaliacao a ser alterada: ")
        self.updateDeleteAvaliacao_label_id.grid(row=1, column=1, pady=10)
        self.updateDeleteAvaliacao_cb_id = ctk.CTkComboBox(self.updateDeleteAvaliacao_frame, values = avaliacoes)
        self.updateDeleteAvaliacao_cb_id.grid(row = 1, column=2, pady=10, padx=10)
        
        self.updateDeleteAvaliacao_avaliacao = ctk.CTkEntry(self.updateDeleteAvaliacao_frame, placeholder_text="")
        self.updateDeleteAvaliacao_avaliacao.grid(row=2, column=1,columnspan = 2, pady=10)
        
        self.updateDeleteAvaliacao_label_aviso = ctk.CTkLabel(self.updateDeleteAvaliacao_frame, text="")
        self.updateDeleteAvaliacao_label_aviso.grid(row=3, column=1, pady=10)
        
        self.updateDeleteAvaliacao_btn_update_av = ctk.CTkButton(self.updateDeleteAvaliacao_frame, text="Alterar como avaliação", command = self.navega_Uav_AVALIACAO_para_R_AVALIACAO_)
        self.updateDeleteAvaliacao_btn_update_av.grid(row=4, column=1, pady=5, padx=10)
        
        self.updateDeleteAvaliacao_btn_update_den = ctk.CTkButton(self.updateDeleteAvaliacao_frame, text="Alterar como denuncia", command = self.navega_Uden_AVALIACAO_para_R_AVALIACAO_)
        self.updateDeleteAvaliacao_btn_update_den.grid(row=4, column=2, pady=5, padx=10)
        
        self.updateDeleteAvaliacao_btn_delete = ctk.CTkButton(self.updateDeleteAvaliacao_frame, text="Deletar", command = self.navega_D_AVALIACAO_para_R_AVALIACAO_)
        self.updateDeleteAvaliacao_btn_delete.grid(row=5, column=1, columnspan = 2, pady=5, padx=10)
        
        self.updateDeleteAvaliacao_btn_return = ctk.CTkButton(self.updateDeleteAvaliacao_frame, text="Retornar", command = self.navega_U_D_AVALIACAO_para_R_AVALIACAO_)
        self.updateDeleteAvaliacao_btn_return.grid(row=6, column=1, columnspan = 2, pady=5, padx=10)
    