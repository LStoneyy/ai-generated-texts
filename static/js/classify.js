let startTime = Date.now();

document.getElementById("classify-form").addEventListener("submit", () => {
    let endTime = Date.now();
    let responseTime = endTime - startTime;
    document.getElementById("response-time").value = responseTime;
});
