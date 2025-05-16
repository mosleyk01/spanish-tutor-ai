document.addEventListener("DOMContentLoaded", function() {
    async function initializeConversation() {
      console.log("Initialize conversation button clicked.");
      try {
        const response = await fetch('/start');
        console.log("Fetch response:", response);
        const data = await response.json();
        console.log("Data received:", data);
        document.getElementById('chatOutput').innerHTML = `<p><strong>AI:</strong> ${data.response}</p>`;
      } catch (err) {
        console.error('Error initializing conversation', err);
      }
    }
  
    async function sendMessage(event) {
      event.preventDefault();
      const userInput = document.getElementById('userInput').value;
      if (!userInput) return;  // Prevent sending an empty message
      document.getElementById('chatOutput').innerHTML += `<p><strong>You:</strong> ${userInput}</p>`;
      try {
        const response = await fetch('/chat', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({ message: userInput })
        });
        const data = await response.json();
        const aiResponse = document.createElement('div');
        aiResponse.innerHTML = `<strong>AI:</strong> ${data.response}`;
        document.getElementById('chatOutput').appendChild(aiResponse);

        // vocalize bot response
        speak(data.response)
      } catch (err) {
        console.error('Error sending message', err);
      }
      document.getElementById('userInput').value = '';

    
    }
  
    document.getElementById('initButton').addEventListener('click', initializeConversation);
    document.getElementById('chatForm').addEventListener('submit', sendMessage);
  });
  

  // speak funciton

  function speak(text) {
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'es-MX'; // Mexican voice
    speechSynthesis.speak(utterance)
  }