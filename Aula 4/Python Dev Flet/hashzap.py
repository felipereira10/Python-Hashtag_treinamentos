# Título: Hashzap
# Botão: Iniciar chat
    # popup/modal/alerta
        # Título: Bem vindo ao Hashzap
        # Campo de Texto: Escreva seu nome no chat
        # Botão: Entrar no chat
            # Sumir com Título e o Botão Inicial
            # Fechar popup
            # Criar o chat (com a mensagem de "nome do usuário entrou no chat")
            # Embaixo do chat:
                # Campo de texto: Digite sua mensagem
                # Botão Enviar
                    # Vai aparecer a mensagem no chat com nome do usuário
                    # Felipe: Boa noite!

# Flet cria -> aplicativo/site/programa de computador
# pip install flet

# 1 passo p/ Flet: importar o flet 
import flet as ft

# 2 passo p/ Flet: criar a função principal do seu sistema
def main(pagina):
    # criar o título
    titulo = ft.Text("Hashzap")

    def enviar_mensagem_tunel(mensagem):
        chat.controls.append(ft.Text(mensagem))
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel) # cria o tunel de comunicação
    

    titulo_janela = ft.Text("Bem vindo ao Hashzap")
    campo_nome_usuario = ft.TextField(label="Escreva seu nome no chat")

    def enviar_mensagem(evento):
        texto = f"{campo_nome_usuario.value}: {texto_mensagem.value}"
        # enviar mensagem no chat:
            # Usuário: mensagem
        # enviar uma mensagem no tunel
        pagina.pubsub.send_all(texto) # envia uma mensagem no tunel

        # limpar campo mensagem
        texto_mensagem.value = ""
        pagina.update()

    texto_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    chat = ft.Column()
    # colunas e linhas
    linha_mensagem = ft.Row([texto_mensagem, botao_enviar])

    def entrar_chat(evento):
        # tirar o titulo da página
        pagina.remove(titulo)
        # tirar o botao_iniciar
        pagina.remove(botao_iniciar)
        # fehcar o popup/janela
        janela.open = False
        # criar o chat
        pagina.add(chat)
        # adicionar o linha de mensagem
        pagina.add(linha_mensagem)

        # escrever a mensagem: usuário entrou no chat
        texto_entrou_chat = f"{campo_nome_usuario.value} entrou no chat!"
        pagina.pubsub.send_all(texto_entrou_chat)

        pagina.update()

    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)


    janela = ft.AlertDialog(
        title=titulo_janela,
        content=campo_nome_usuario,
        actions=[botao_entrar]
    )

    def abrir_popup(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

    # adicionar o título da página
    pagina.add(titulo)
    pagina.add(botao_iniciar)

# 3 passo p/ Flet: executar o seu sistema
ft.app(target=main, view=ft.WEB_BROWSER, port=8000)