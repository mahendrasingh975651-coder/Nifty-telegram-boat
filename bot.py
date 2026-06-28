from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN = "8859992598:AAF8ZRS3xt1vavbtLvVWhBGkuKEEx-YJ_M0"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Nifty Signal Bot Started!\n\nअभी यह टेस्ट मोड में है।"
    )

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if text == "hi":
        await update.message.reply_text("👋 Hello!")

    elif text == "signal":
        await update.message.reply_text(
            "📈 NIFTY SIGNAL\nDirection: BUY\nEntry: Demo\nSL: Demo\nTarget: Demo"
        )

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

app.run_polling()
