# -*- coding: utf-8 -*-

from cgitb import text
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.switch import Switch

from kivy.uix.button import Button

kivy.require('1.9.1')

var = 0
def soma_um(instance):
    global var
    var += 1
    instance.text = str(var)

def diminui_um(instance):
    global var
    var = var-1
    instance.text = str(var)    
    
class MeuApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical',
                padding=[40, 20, 40, 20])
        
        layout.add_widget(Label(text='Contando!'))
        btn = Button(text='Somar!', size=(50,50))
        btn2 = Button(text='Diminuir', size=(50,50))
        
        btn.bind(on_press=soma_um)
        btn2.bind(on_press=diminui_um)
        layout.add_widget(btn)
        layout.add_widget(btn2)
        layout.add_widget(Switch())
        return layout 
    
if __name__ == '__main__':
    MeuApp().run()