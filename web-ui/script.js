async function analyze() {
  const input = document.getElementById("input").value;
  const res = await fetch("/analyze", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({text: input})
  });
  const data = await res.json();
  document.getElementById("output").innerText = data.result;
}
