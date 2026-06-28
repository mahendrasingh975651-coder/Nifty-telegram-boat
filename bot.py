from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN ="8851522995:AAHARedisPA31vDh9yYAzCDWvFsTC_YUPl4"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Nifty Signal Bot Started!\n\n"
        "अभी यह टेस्ट मोड में है।"
    )

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if text == "hi":
        await update.message.reply_text("👋 Hello Mahisingh!")

    elif text == "signal":
        await update.message.reply_text(
            "📈 NIFTY SIGNAL\n"
            "Direction: BUY\n"
            "Entry: Demo\n"
            "SL: Demo\n"
            "Target: Demo"
        )

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

app.run_polling()
