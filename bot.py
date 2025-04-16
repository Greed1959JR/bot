from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# 👉 Cole seu TOKEN aqui:
import os
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

    # Se for uma mensagem nova (comando /start)
    if isinstance(update_or_query, Update):
        await update_or_query.message.reply_text(text, reply_markup=reply_markup)
    # Se for retorno do botão "voltar"
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

# 🔹 Iniciar o bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("🤖 Bot rodando...")
    app.run_polling()
