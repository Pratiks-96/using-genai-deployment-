async function sendMessage() {
  const input = document.getElementById("userInput");
  const chatBox = document.getElementById("chatBox");

  const userMessage = input.value.trim();
  if (!userMessage) return;

  chatBox.innerHTML += `<div class="user">${userMessage}</div>`;
  input.value = "";

  const response = await fetch("http://54.163.41.42:8080/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: userMessage })
  });

  const data = await response.json();
  chatBox.innerHTML += `<div class="bot">${data.reply}</div>`;
}
