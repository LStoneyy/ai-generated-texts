let startTime = Date.now();

document.getElementById("classify-form").addEventListener("submit", () => {
    let endTime = Date.now();
    let responseTime = endTime - startTime;
    document.querySelector('input[name="response_time"]').value = responseTime;
});
