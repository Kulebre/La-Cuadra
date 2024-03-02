from pydoc import pager
from tkinter import PAGES
import flet 
from flet import AppBar, ElevatedButton, Page, Text, View, colors
import flet as ft
import Imagenes
from Imagenes import galicia
from Imagenes import Aguila
from Imagenes import Gabriel
from Imagenes import Paula





    
    
       


def button_clicked(gali):
    precio = 0.90
    gd.data += 1
    gv.value = f"{gd.data} Estrellas"
    
   

gd = ft.ElevatedButton("Estrella Galicia 0,70€", on_click=button_clicked, data=0)
gv = ft.Text()

def main(page: Page):
    page.title = "La Cuadra"

#Metodo
 
#imagenes
  

#Pagina principal de rutas
    
    def route_change(e):
        page.views.clear()

        #Asociacion boton bebida y paso a personas
        def gali_click(e):
            precio_valor = 0.70
        
            page.views.append(
                 View(
                       "/Personas",
                       [
                          AppBar(title=Text("Personas"), bgcolor=colors.SURFACE_VARIANT),
                          
                         
                          ft.SafeArea(Gabriel), 
                          ElevatedButton("Gabriel", on_click=lambda _: page.go("/Pago")), 
                          ft.SafeArea(Paula), 
                          ElevatedButton("Paula", on_click=lambda _: page.go("/")), 
                          ft.Text(precio_valor),
                          ElevatedButton("Inicio", on_click=lambda _: page.go("/")),
                       ],
                  )
                 )
            page.update()
        
        def agui_click(e):
            precio_valor = 0.90
        
            page.views.append(
                 View(
                       "/Personas",
                       [
                          AppBar(title=Text("Personas"), bgcolor=colors.SURFACE_VARIANT),
                          ElevatedButton("Gabriel", on_click=lambda _: page.go("/Pago")), 
                          ft.SafeArea(Paula), 
                          ElevatedButton("Paula", on_click=lambda _: page.go("/")), 
                          ft.Text(precio_valor),
                          ElevatedButton("Inicio", on_click=lambda _: page.go("/")),
                          
                       ],
                  )
                 )
            page.update()

          
        #Pagina principal bebidas
        page.views.append(
            
            View(
                "/",
                [
                    AppBar(title=Text("Bebidas"), bgcolor=colors.SURFACE_VARIANT),
                   
                    ft.SafeArea(galicia), 
                    ElevatedButton("Estrella Galicia", on_click=gali_click),
                    ft.SafeArea(Aguila), 
                    ElevatedButton("Águila", on_click=agui_click),
                     
                    
                    

                ],
            )
           
        )
        page.update()
        #Pagina personas
        if page.route == "/Personas":
            page.views.append(
                View(
                    "/Personas",
                    [
                        AppBar(title=Text("Personas"), bgcolor=colors.SURFACE_VARIANT),
                        ElevatedButton("Inicio", on_click=lambda _: page.go("/")),
                    ],
                )
            )
        page.update()
        #Pagina pago
        if page.route == "/Pago":
            page.views.append(
                View(
                    "/Pago",
                    [
                        AppBar(title=Text("Pagar"), bgcolor=colors.SURFACE_VARIANT),
                        ElevatedButton("Pagar", on_click=lambda _: page.go("/")),
                        
                    ],
                )
            )
        page.update()
        

    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go(page.route)


flet.app(main)
