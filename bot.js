const { Telegraf } = require(`telegraf`);
require('dotenv').config()

const bot = new Telegraf(process.env.BOT_SECRET);

function dateFormate() {
  const agora = new Date();

  const day = String(agora.getDate()).padStart(2, "0");
  const month = String(agora.getMonth() + 1).padStart(2, "0");
  const year = agora.getFullYear();

  const hours = String(agora.getHours()).padStart(2, "0");
  const minutes = String(agora.getMinutes()).padStart(2, "0");
  const seconds = String(agora.getSeconds()).padStart(2, "0");

  return `${day}/${month}/${year} ${hours}:${minutes}:${seconds}`;
}

async function sendMessage() {
console.log(`start bot sucess.`)
  try {
    const cap =
      `A safra aqui não para! 🌾🚜\n` +
      `Estamos a todo vapor com a equipe em campo 💪\n` +
      `Vamos que vamos! 🔥\n\n` +
      `Atualização: ${dateFormate()}`;
    await bot.telegram.sendPhoto(
      process.env.CHAT_ID,
      { source: `fs.png` },
      { caption: cap }
    );
  } catch (error) {
    const { spawn } = require("child_process");
    spawn("python", ["index.py"]);
  }
}

sendMessage();
