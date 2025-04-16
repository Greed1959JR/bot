
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

# 👉 Pegando o token da variável de ambiente
TOKEN = os.getenv("BOT_TOKEN")

# 🔹 Função que exibe o menu principal
async def show_main_menu(update_or_query, context):
    keyboard = [
        [InlineKeyboardButton("📢 Canal Grátis", callback_data='canal_gratis')],
        [InlineKeyboardButton("💰 Canal VIP", callback_data='canal_vip')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    text = (
        "👋 Seja bem-vindo(a) ao Overgeared Tips!\n\n"
        "Quer começar a lucrar com apostas esportivas de forma inteligente?\n\n"
        "Escolha uma opção abaixo:"
    )

    if isinstance(update_or_query, Update):
        await update_or_query.message.reply_text(text, reply_markup=reply_markup)
    else:
        await update_or_query.edit_message_text(text, reply_markup=reply_markup)

# 🔹 Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await show_main_menu(update, context)

# 🔹 Ações dos botões
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'canal_gratis':
        keyboard = [[InlineKeyboardButton("🔙 Voltar", callback_data='voltar')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("✅ Aqui está o canal gratuito: https://t.me/+aDwQp2uAGj0zY2Qx", reply_markup=reply_markup)

    elif query.data == 'canal_vip':
        keyboard = [[InlineKeyboardButton("🔙 Voltar", callback_data='voltar')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("💰 Para acessar o VIP, clique aqui para fazer o pagamento:\nhttps://web.telegram.org/k/#@KrayOG_Bot", reply_markup=reply_markup)

    elif query.data == 'voltar':
        await show_main_menu(query, context)

# 🔹 Servidor web para manter o bot "acordado"
from flask import Flask
from threading import Thread

app_flask = Flask('')

@app_flask.route('/')
def home():
    return "Bot está vivo!"

def run():
    app_flask.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# 🔹 Iniciar o bot
if __name__ == '__main__':
    keep_alive()  # Ativa o webserver fake
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("🤖 Bot rodando...")
    app.run_polling()
