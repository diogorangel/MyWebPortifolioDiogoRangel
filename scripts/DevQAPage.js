// Function to show a custom message box
function showMessage(message) {
    const messageBox = document.getElementById('messageBox');
    const messageText = document.getElementById('messageText');
    messageText.textContent = message;
    messageBox.classList.remove('hidden');
}

document.getElementById('generateBtn').addEventListener('click', async () => {
    const scenarioPrompt = document.getElementById('scenarioPrompt').value;
    const testType = document.getElementById('testType').value;
    const language = document.getElementById('language').value;

    if (!scenarioPrompt) {
        showMessage('Por favor, digite uma descrição para o cenário de teste.');
        return;
    }

    const button = document.getElementById('generateBtn');
    const loading = document.getElementById('loading');
    const resultsContainer = document.getElementById('resultsContainer');
    const testResult = document.getElementById('testResult');

    // Hide previous message if any
    document.getElementById('messageBox').classList.add('hidden');

    // Show loading state
    button.classList.add('hidden');
    loading.classList.remove('hidden');
    resultsContainer.classList.add('hidden');

    const systemPrompt = `Você é um especialista em testes de software. Baseado na descrição fornecida, crie um cenário de teste detalhado. Se o tipo de teste for 'manual', gere os passos em Markdown. Se for 'automatizado', gere o código completo na linguagem e framework especificados. Inclua comentários e organize o código de forma clara.`;

    let userQuery = `Gerar um cenário de teste para o seguinte cenário: "${scenarioPrompt}". Tipo de teste: ${testType}. Linguagem/Formato: ${language}.`;

    try {
        const apiKey = "";
        const apiUrl = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-05-20:generateContent?key=${apiKey}`;

        const payload = {
            contents: [{ parts: [{ text: userQuery }] }],
            systemInstruction: { parts: [{ text: systemPrompt }] },
        };

        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        if (!response.ok) {
            throw new Error(`API call failed with status: ${response.status}`);
        }

        const result = await response.json();
        const generatedText = result?.candidates?.[0]?.content?.parts?.[0]?.text;

        if (generatedText) {
            testResult.textContent = generatedText;
            resultsContainer.classList.remove('hidden');
        } else {
            throw new Error("No content received from the API.");
        }

    } catch (error) {
        console.error("Failed to generate test case:", error);
        showMessage("Falha ao gerar o cenário de teste. Por favor, tente novamente.");
    } finally {
        // Hide loading and show button again
        loading.classList.add('hidden');
        button.classList.remove('hidden');
    }
});
