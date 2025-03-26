document.getElementById('generateBtn').addEventListener('click', async () => {
    try {
        const response = await fetch('/generate');
        const data = await response.json();
        
        const themeElement = document.getElementById('theme-text');
        themeElement.textContent = data.theme;
        
        // Animation
        themeElement.parentElement.style.animation = 'none';
        setTimeout(() => {
            themeElement.parentElement.style.animation = 'fadeIn 0.5s';
        }, 10);
    } catch (error) {
        console.error('Erreur:', error);
    }
});

// Ajouter l'animation CSS dynamiquement
const style = document.createElement('style');
style.textContent = `
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
`;
document.head.appendChild(style);