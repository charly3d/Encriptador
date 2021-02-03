###########  Version #############
#Creador: Rodrigo Ferrer         #
#Versión: V3.0                   #
#Fecha:10-11-2020                #
#                                #
##################################

###############  MODULOS  #####################################################################################################
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import ttk
import tkinter as tk
import math
import time
import random

##############  FUNCIONES ###################################################################################################### 
              
#funcion que ordena una lista segun un valor                    #La funcion recibe una lista de longitud n y la ordena de una forma extraña segun un valor del 0 al 9          
def orden(lista,orden):
    cant=math.factorial(len(lista))                             #factorial de la cantidad de valores en la lista para conocer todas las posibilidades
    nvalista=[0]*len(lista)                                     #crea una del mismoo tamaño que la original con todo lista con todo 0
    largo=len(lista)
    if largo>10:
        aleato=[0,-4,1,3,2,4,-1,-5,-2,-3]*(int(round(largo/10,1))+1)
    else:
        aleato=[0,-4,1,3,2,4,-1,-5,-2,-3]
    for i in range(len(nvalista)):                              #va recorrindo la lista nueva
        indice=int((len(lista)-1)*(math.cos((aleato[i]+orden)/5*math.pi)))
        nvalista[i]=lista[indice]                               #le da un valor a la lista nueva y lo borra d ela lista original para no volver a darselo a la nueva
        del (lista[indice])
    return nvalista

#funcion que ordenla lista en funcion del codigo
def ordenarlista(lista,codigo):                                 #lista que se va a ordenar y codigo de digitos que indican el orden
    listaenc=[]
    
    if not(codigo.isdigit()):
        codigo='9999999'
    codigo=list(codigo)
    n=math.ceil(len(lista)/(len(codigo)))
    for i in range(0,len(lista),n):
        if (i+n)<len(lista):
            listaenc=listaenc+orden (lista[i:i+n],int(codigo[i//n]))
        else:
            listaenc=listaenc+orden (lista[i:len(lista)],int(codigo[i//n-1]))
    return listaenc

#funcion que encripta clave
def encriptar(clave,lista1,lista2):
    claveencr=[]
    for i in clave:
        indice=lista1.index(i)        
        claveencr=claveencr+[lista2[indice]]
    return claveencr

#funcion para actualizar texto del boton
def bot(event):
        if opcion.get()=='Encriptar Clave':
                textob.set('Encriptar')
        if opcion.get()=='Desencriptar Clave':
                textob.set('Desencriptar')
        if opcion.get()=='Buscar Clave':
                textob.set('Buscar')   
def progress(currentValue):
    barra["value"]=currentValue
def Progresar():
    barra["value"]=0
    barra["maximum"]=100
    divisiones=10
    currentValue=0
    while currentValue<100:
        currentValue=currentValue+random.randint(1, 10)

        if currentValue>=100:
            currentValue=100
            
        barra.after(50, progress(currentValue))
        barra.update()
    
##    for i in range (divisiones):
##        currentValue=currentValue+10
##        barra.after(100, progress(currentValue))
##        barra.update() # Force an update of the GUI
        

############### PROGRAMA PRINCIPAL  ##################################################################################### 
def vamos():
##        barra.start(10)
        #abre archivo con letras y encriptación)
        aenc=open('Data\ENC.txt')
        laux=[]
        i=1
        le=[]
        #crear l lista con letras posibles de claves
        for linea in aenc:
            laux=laux+linea.split()
            i+=1
        l=list(laux[0])
        #crear le
        cont=0
        for i in l:
            le=le+[laux[1][cont]+laux[1][cont+1]]
            cont+=2
  
        #Encriptar Clave
        if opcion.get()=='Encriptar Clave':
                
                cod=codigo.get()
                #cod=list(cod)
                c=list(clave.get())
                le=ordenarlista(le,cod)
                ce=encriptar(c,l,le)
                Progresar()
                texto2.set(ce)
                if guardarclave.get()=='Si':
                    book=open('Data\claves.txt')
                    g=open('Data\backup.txt','w')
                    for line in book:
                        g.write(line)
                    book.close()
                    pagina=pag.get()
                    persona=per_usu.get()
                    delimitador=' '
                    linea=persona+' '+pagina+' '+delimitador.join(ce)+'\n'
                    g.write(linea)
                    book=open('Data\claves.txt','w')
                    g.close()
                    g=open('Data\backup.txt')
                    for line in g:
                        book.write(line)
                    book.close()
            
        #Desncriptar Clave
        if opcion.get()=='Desencriptar Clave':
                cod=codigo.get()
                #cod=list(cod)
                c=clave.get()
                c=c.split(' ')
                le=ordenarlista(le,cod)
                ce=encriptar(c,le,l)
                delimitador=""
                ce=delimitador.join(ce)
                Progresar()
                texto2.set(ce)
        #Buscar Clave
        if opcion.get()=='Buscar Clave':
                book=open('Data\claves.txt')
                cod=codigo.get()
                #cod=list(cod)
                persona=per_usu.get()
                pagina=pag.get()
                for line in book:
                    if line.startswith(persona):
                        lista=line.split(' ')
                    if lista[1]==pagina:
                        c=lista[2:]
                        c[-1]=c[-1][:-1]
                le=ordenarlista(le,cod)
                ce=encriptar(c,le,l)
                delimitador=""
                clave2=delimitador.join(ce)
                Progresar()
                texto2.set(clave2)
                book.close()
                    
        
###############  INTERFAZ GRAFICA  ##################################################################################### 
titulo="Encriptador de Claves by RFerrer"
tam=200
ancho=tam*3
alto=tam*3
fondo="light blue"
fuente='Arial'
alet=[int(tam/150*15),int(tam/150*12),int(tam/150*10),int(tam/150*8)]

tamaño=str(ancho)+'x'+str(alto)

xo=[tam/4,2/3*tam,1.5*tam,2.4*tam]
yo=[tam/5,2*tam/5,3*tam/5,4*tam/5,5*tam/5,6*tam/5,7*tam/5,8*tam/5,9*tam/5,10*tam/5]

### Ventana
ventana= Tk()
ventana.title(titulo)
ventana.iconbitmap("Data\icono.ico")
ventana.geometry(tamaño)
ventana.config(bg="white",
               width=ancho,
               height=alto)

### Frame/cont1 1
cont1=Frame(ventana)
cont1.pack()
cont1.config(bg=fondo,
                  width=ancho,
                  height=alto,
                  bd=10)

### Etiquetas
descr1=Label(cont1)
descr1.config(text='Elegí la opción deseada',
             bg="light blue",
             font=(fuente,alet[1]))
descr1.place(x=xo[0],y=yo[0])

descr2=Label(cont1)
descr2.config(text='Codigo único(solo números)',
             bg=fondo,
             font=(fuente,alet[1]))
descr2.place(x=xo[0],y=yo[2])

##resultado=Label(cont1)
##resultado.config(textvariable=texto2,
##                 bg='white',
##                 font=(fuente,alet[2]))
##resultado.place(x=xo[0],y=yo[-1])


### Opción Elegible
opcion=Combobox(cont1,values=['Encriptar Clave',
                              'Desencriptar Clave',
                              'Buscar Clave'],
                font=(fuente,alet[2]))
opcion.bind("<<ComboboxSelected>>",bot)
opcion.place(x=xo[0],y=yo[1])
opcion.current(0)

### Botones
textob=StringVar()
textob.set('Encriptar')
boton=Button(cont1,
             textvariable=textob,
             command=vamos,
             font=(fuente,alet[2]))
boton.place(x=int(0.7*ancho),y=int(0.8*alto))

### Entradas de Texto
codigo=Entry(cont1,show='*',
             width=20,
             font=(fuente,alet[2]))
codigo.insert(0,'Codigo')
codigo.place(x=xo[0],y=yo[3])

pag=Entry(cont1,
          font=(fuente,alet[2]))
pag.insert(0,'Pagina')
pag.place(x=xo[0],y=yo[5])

per_usu=Entry(cont1,
              font=(fuente,alet[2]))
per_usu.insert(0,'Persona/Usuario')
per_usu.place(x=xo[0],y=yo[6])

clave=Entry(cont1,
            font=(fuente,alet[2]))
clave.insert(0,'Clave')
clave.place(x=xo[0],y=yo[7])

texto2=StringVar()
texto2.set('Resultado')
resultado=Entry(cont1,
            font=(fuente,alet[2]),
               width=int(tam/10)
               )
resultado.config(textvariable=texto2,
                 bg='white',
##                 font=(fuente,alet[2])
                 )
resultado.configure(state="readonly")
resultado.place(x=xo[0],y=yo[-1])

### Opcion Button
guardarclave = StringVar()
check = Checkbutton(cont1, text='Guardar Clave para luego poder buscarla', 
            variable=guardarclave,
	    onvalue='Si',
            offvalue='No',
            bg=fondo,
            font=(fuente,alet[2]))
check.place(x=xo[0],y=yo[4])

###Barra de Progreso
progreso = StringVar()
largobarra=tam*2
barra=ttk.Progressbar(cont1,
                      mode='determinate',
                      orient="vertical",
                      maximum=100,
                      #variable=progreso,
                      )
barra.place(x=xo[3],y=yo[0],
            #width=tam,
            height=largobarra)




###########         FIN      ##################################################################################### 
ventana.mainloop()
