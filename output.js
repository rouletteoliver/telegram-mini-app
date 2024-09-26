// Подключение Telegram Web App API
const tg = window.Telegram.WebApp;

// Инициализация интерфейса и отображение текущих данных
function initializeInterface() {
    const nickname = document.getElementById('nickname');
    const avatar = document.getElementById('avatar');
    const walletAddress = document.getElementById('wallet-address');
    const connectBtn = document.getElementById('connect-evm');

    // Обновление информации о пользователе Telegram
    if (tg.initDataUnsafe && tg.initDataUnsafe.user) {
        nickname.textContent = tg.initDataUnsafe.user.username || tg.initDataUnsafe.user.first_name || 'Имя не найдено';
        if (tg.initDataUnsafe.user.photo_url) {
            avatar.src = tg.initDataUnsafe.user.photo_url;
            avatar.onerror = () => {
                avatar.src = 'img/avatar.png';
            };
        } else {
            avatar.src = 'img/avatar.png';
        }
    } else {
        nickname.textContent = 'Имя не найдено';
        avatar.src = 'img/avatar.png';
    }

    // Инициализация кнопки подключения кошелька
    connectBtn.addEventListener('click', connectWallet);

    // Инициализация других кнопок
    document.getElementById('game-button').addEventListener('click', () => {
        window.location.href = 'game.html';
    });

    tg.ready();
}

// Функция подключения к MetaMask или другому EVM-кошельку
async function connectWallet() {
    const walletAddress = document.getElementById('wallet-address');
    const connectBtn = document.getElementById('connect-evm');

    if (window.ethereum) {
        try {
            const provider = new ethers.providers.Web3Provider(window.ethereum);
            await provider.send("eth_requestAccounts", []);
            const signer = provider.getSigner();
            const account = await signer.getAddress();

            walletAddress.textContent = account;
            connectBtn.textContent = 'disconnect evm';
            connectBtn.classList.add('disconnect-btn');

        } catch (error) {
            console.error('Ошибка при подключении к кошельку:', error);
            walletAddress.textContent = 'Ошибка подключения';
        }
    } else {
        alert('Пожалуйста, установите MetaMask или другой EVM-совместимый кошелек!');
    }
}

// Функция отключения кошелька
function disconnectWallet() {
    const walletAddress = document.getElementById('wallet-address');
    const connectBtn = document.getElementById('connect-evm');

    walletAddress.textContent = 'Кошелёк не подключён';
    connectBtn.textContent = 'connect evm';
    connectBtn.classList.remove('disconnect-btn');
}

// Запуск приложения
initializeInterface();
