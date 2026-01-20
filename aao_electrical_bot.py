from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Replace with your BotFather token
BOT_TOKEN = "8351401751:AAF2bP9WIi3m4FnQiAKIQOkASKTUq5jJ7wo"

# Business info
BUSINESS_NAME = "Ahmed Abdulmalik Olamilekan Electrical & Electronic Engineering Services"
PHONE = "08128804465"
EMAIL = "ahmedabdulmalik952@gmail.com"
LOCATION = "Ogun State, Nigeria"
INSTAGRAM = "@bigishola333"

# Command handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = (
        f"Welcome to *{BUSINESS_NAME}* ⚡\n\n"
        "We provide professional electrical and electronic engineering services.\n\n"
        "Commands:\n"
        "/services – View services\n"
        "/repairs – Repair services\n"
        "/installation – Installation services\n"
        "/solar – Solar & inverter solutions\n"
        "/emergency – Urgent help\n"
        "/quote – Request a quote\n"
        "/contact – Contact details"
    )
    await update.message.reply_text(message, parse_mode="Markdown")

async def services(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔧 *Our Services*\n"
        "• Electrical wiring & rewiring\n"
        "• Electronics repair & troubleshooting\n"
        "• Inverter & solar installations\n"
        "• CCTV & security systems\n"
        "• Maintenance & diagnostics\n"
        "• Power backup solutions",
        parse_mode="Markdown"
    )

async def repairs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛠 *Repair Services*\n"
        "• Inverters & UPS systems\n"
        "• Power supplies\n"
        "• Home & industrial electronics\n"
        "• Fault tracing & component replacement",
        parse_mode="Markdown"
    )

async def installation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚙️ *Installation Services*\n"
        "• House & office wiring\n"
        "• Solar & inverter systems\n"
        "• Distribution boards\n"
        "• Lighting systems\n"
        "• CCTV & access control",
        parse_mode="Markdown"
    )

async def solar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "☀️ *Solar & Inverter Solutions*\n"
        "• Solar panel installation\n"
        "• Inverter setup & configuration\n"
        "• Battery sizing & replacement\n"
        "• Off-grid & backup power systems",
        parse_mode="Markdown"
    )

async def emergency(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"🚨 *Emergency Electrical Support*\n📞 Call: {PHONE}",
        parse_mode="Markdown"
    )

async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💰 *Request a Quote*\n"
        "Send:\n1. Type of service\n2. Location\n3. Urgency",
        parse_mode="Markdown"
    )

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"📞 *Contact Information*\nPhone: {PHONE}\nEmail: {EMAIL}\nLocation: {LOCATION}\nInstagram: {INSTAGRAM}",
        parse_mode="Markdown"
    )

# Main function
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("services", services))
    app.add_handler(CommandHandler("repairs", repairs))
    app.add_handler(CommandHandler("installation", installation))
    app.add_handler(CommandHandler("solar", solar))
    app.add_handler(CommandHandler("emergency", emergency))
    app.add_handler(CommandHandler("quote", quote))
    app.add_handler(CommandHandler("contact", contact))
    print("AAO Electrical Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()