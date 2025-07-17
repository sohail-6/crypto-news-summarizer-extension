document.getElementById("summarizeBtn").addEventListener("click", () => {
  const url = document.getElementById("urlInput").value;
  document.getElementById("output").textContent = `URL received: ${url}`;
});
