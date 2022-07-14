from datetime import date
from glob import glob
from sqlite3 import Date
import tkinter
from tkinter import*
from tkinter import messagebox
from turtle import left
import pymysql
from setuptools import Command


def pantallainicio():
    global pantalla
    pantalla=Tk()
    pantalla.geometry("400x500")
    pantalla.title("BBVA - AppConsultas")
    pantalla.iconbitmap("BBVAlogo.ico")

    image=PhotoImage(file="BBVAlogo.gif")
    image=image.subsample(2,4)
    label=Label(image=image)
    label.pack()

    Label(text="Acceso al Sistema", bg="DodgerBlue4", fg="white", width="500",height="3", font=("Calibrí",15)).pack()
    Label(text="Ingrese su Usuario y Contraseña", width="500",height="3", font=("Calibrí",10)).pack()

    global nombreusuario_verify
    global contrasenausuario_verify

    nombreusuario_verify=StringVar()
    contrasenausuario_verify=StringVar()

    Label(text="Usuario", width="500",height="3",font=("Calibrí",10)).pack()
    nombre_usuario_entry=Entry(pantalla, textvariable=nombreusuario_verify)
    nombre_usuario_entry.pack()

    Label(text="Contraseña", width="500",height="3", font=("Calibrí",10)).pack()
    contrasena_usuario_entry=Entry(pantalla,show="*", textvariable=contrasenausuario_verify)
    contrasena_usuario_entry.pack()

    Button(text="Continuar", command=validacion_datos).pack()

    pantalla.mainloop()

def validacion_datos():
    bd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="proyectobbva"
    )

    fcursor=bd.cursor()

    fcursor.execute("SELECT perfil FROM asesores WHERE usuario='"+nombreusuario_verify.get()+"' AND auth='"+contrasenausuario_verify.get()+"'")
    if fcursor.fetchall():
        messagebox.showinfo(title="inicio correcto", message="Credenciales correctas")
        pantallamenu()    
    else:
        messagebox.showwarning(title="Cuidado", message="Credenciales incorrectas")

    bd.close()


def pantallamenu():
    global pantalla1
    pantalla1= Toplevel(pantalla)
    pantalla1.geometry("400x550")
    pantalla1.title("BBVA - Menu Principal")
    pantalla1.iconbitmap("BBVAlogo.ico")

    Label(pantalla1, text="Bienvenido Asesor BBVA", bg="DodgerBlue4", fg="white", width="500",height="3", font=("Calibrí",15)).pack()
    Label(pantalla1,text="Ventana de Consultas", width="500",height="3", font=("Calibrí",10)).pack()
    
    global idcliente_verify
    global nombrecliente_verify
    global appaternocliente_verify
    global apmaternocliente_verify
    global FechaNaccliente_verify

    idcliente_verify=StringVar()
    nombrecliente_verify=StringVar()
    appaternocliente_verify=StringVar()
    apmaternocliente_verify=StringVar()

    global id_cliente_entry
    global nombre_cliente_entry
    global appaterno_cliente_entry
    global apmaterno_cliente_entry

    Label(pantalla1,text="ID Cliente", width="500",height="3",font=("Calibrí",10)).pack()
    id_cliente_entry=Entry(pantalla1, textvariable=idcliente_verify)
    id_cliente_entry.pack()
    Label(pantalla1).pack()

    Label(pantalla1,text="Nombre", width="500",height="3", font=("Calibrí",10)).pack()
    nombre_cliente_entry=Entry(pantalla1, textvariable=nombrecliente_verify)
    nombre_cliente_entry.pack()
    Label(pantalla1).pack()

    Label(pantalla1,text="Apellido Paterno", width="500",height="3", font=("Calibrí",10)).pack()
    appaterno_cliente_entry=Entry(pantalla1, textvariable=appaternocliente_verify)
    appaterno_cliente_entry.pack()
    Label(pantalla1).pack()

    Label(pantalla1,text="Apellido Materno", width="500",height="3", font=("Calibrí",10)).pack()
    apmaterno_cliente_entry=Entry(pantalla1, textvariable=apmaternocliente_verify)
    apmaterno_cliente_entry.pack()
    Label(pantalla1).pack()

    Button(pantalla1, text="Buscar", command=validacion_datos2).pack()


def validacion_datos2():
    bd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="proyectobbva"
    )

    fcursor=bd.cursor()

    fcursor.execute("SELECT * FROM clientes WHERE idCliente='"+idcliente_verify.get()+"' OR ( nombre='"+nombrecliente_verify.get()+"' AND apellidoPaterno='"+appaternocliente_verify.get()+"' AND apellidoMaterno='"+apmaternocliente_verify.get()+"') ")
    if fcursor.fetchall():
        messagebox.showinfo(title="Cliente Encontrado", message="Credenciales correctas")
        resultcliente=fcursor.fetchall()
        print(resultcliente)
    else:
        messagebox.showwarning(title="No hay Coincidencias", message="Credenciales incorrectas")

    bd.close()


pantallainicio()