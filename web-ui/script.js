async function sendMessage() {
  const input = document.getElementById("userInput");
  const chatBox = document.getElementById("chatBox");

  const userMessage = input.value;
  if (!userMessage) return;

  chatBox.innerHTML += `<div class="user">${userMessage}</div>`;
  input.value = "";

  const response = await fetch("http://BOT_SERVICE_IP/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: userMessage })
  });

  const data = await response.json();
  chatBox.innerHTML += `<div class="bot">${data.reply}</div>`;
}
