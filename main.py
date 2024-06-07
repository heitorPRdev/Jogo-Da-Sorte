import flet as ft
from random import randint
def main(page: ft.Page):
    def sorteio(e):
        randomNum = 0
        randomNum = randint(1,50)
        res.value = ''
        res.bgcolor = ''
        res.color = ''
        page.update()
        try:
            if randomNum == int(num.value):
                
                res.value = f'Você venceu, o número que eu escolhi foi {randomNum} e o que você escolheu foi {num.value}. Parabéns!!'
                res.bgcolor = 'green'
                res.color = 'black'
                res.size = 26
                page.update()
            
            else:
                res.value = f'Você perdeu, o número que eu escolhi foi {randomNum} e o que você escolheu foi {num.value}.\nEscolha outro número e tente a sorte denovo'
                res.bgcolor = 'red'
                res.color = 'black'
                res.text_align = 'center'
                res.size = 26
                page.update()

            
        except ValueError:
            res.value = f'Somente números, tente denovo.'
            res.bgcolor = 'red'
            res.color = 'black'
            res.text_align = 'center'
            res.size = 26
            page.update()
            
        

    page.title = 'Jogo da Sorte'
    frase1 = ft.Text('Escolha um número de 1 a 50(probabilidade = ⅕)')
    num = ft.TextField(label='digite o seu número aqui')
    enviar = ft.ElevatedButton(text='Enviar',on_click=sorteio)
    res = ft.Text()
    page.add(
        frase1,
        num,
        enviar,
        res
    )
ft.app(target=main)