// static/js/script.js
document.getElementById('predictButton').addEventListener('click', function() {
    fetch('/predict', { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            document.getElementById('result').textContent = 'Prediction: ' + data.prediction;
        });
});
