from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8754413830:AAEmvMDByU5nXUApdI1A72F-HnAf-TbMIok"

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if "hi" in text.lower():
        await update.message.reply_text("Hello 👋 Welcome!")
    elif "price" in text.lower():
        await update.message.reply_text("Our price starts from $10 💰")
    else:
        await update.message.reply_text("Thanks for your message 🙏")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), auto_reply))

app.run_polling()
