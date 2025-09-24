// Function to show a custom message box
function showMessage(message) {
    const messageBox = document.getElementById('messageBox');
    const messageText = document.getElementById('messageText');
    messageText.textContent = message;
    messageBox.classList.remove('hidden');
}

document.getElementById('generateBtn').addEventListener('click', async () => {
    const imagePrompt = document.getElementById('imagePrompt').value;
    if (!imagePrompt) {
        showMessage('Por favor, digite uma descrição para a imagem.');
        return;
    }

    const button = document.getElementById('generateBtn');
    const loading = document.getElementById('loading');
    const imageContainer = document.getElementById('imageContainer');
    const generatedImage = document.getElementById('generatedImage');

    // Hide previous message if any
    document.getElementById('messageBox').classList.add('hidden');

    // Show loading state
    button.classList.add('hidden');
    loading.classList.remove('hidden');
    imageContainer.classList.add('hidden');

    try {
        // Get the API key
        const apiKey = "";
        const apiUrl = `https://generativelanguage.googleapis.com/v1beta/models/imagen-3.0-generate-002:predict?key=${apiKey}`;

        const payload = {
            instances: [{ prompt: imagePrompt }],
            parameters: { sampleCount: 1 }
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
        const base64Data = result?.predictions?.[0]?.bytesBase64Encoded;

        if (base64Data) {
            const imageUrl = `data:image/png;base64,${base64Data}`;
            generatedImage.src = imageUrl;
            imageContainer.classList.remove('hidden');
        } else {
            throw new Error("No image data received from the API.");
        }

    } catch (error) {
        console.error("Failed to generate image:", error);
        showMessage("Falha ao gerar a imagem. Por favor, tente novamente.");
    } finally {
        // Hide loading and show button again
        loading.classList.add('hidden');
        button.classList.remove('hidden');
    }
});