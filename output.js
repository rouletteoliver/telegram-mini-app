// Проверка загрузки Telegram Web App API
if (window.Telegram && window.Telegram.WebApp) {
    const tg = window.Telegram.WebApp;

    // Инициализация интерфейса и отображение текущих данных
    function initializeInterface() {
        const gameButton = document.getElementById('game-button');
        const searchGameButton = document.getElementById('search-button');
        const profileButton = document.getElementById('profile-button');

        // Проверка наличия элементов
        if (!gameButton || !searchGameButton || !profileButton) {
            console.error("Некоторые элементы интерфейса не найдены, проверьте правильность ID в HTML.");
            return;
        }

        // Инициализация кнопок, пока они ничего не делают при нажатии
        gameButton.addEventListener('click', () => {
            console.log("Game button clicked");
        });

        searchGameButton.addEventListener('click', () => {
            console.log("Search Game button clicked");
        });

        profileButton.addEventListener('click', () => {
            console.log("Profile button clicked");
        });

        tg.ready();
    }

    // Запуск приложения
    initializeInterface();
} else {
    console.error('Telegram Web App API не загружен.');
}
