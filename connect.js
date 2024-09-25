// connect.js
let provider, signer;

// Функция для подключения кошелька
async function connectWallet() {
    try {
        // Проверка наличия MetaMask и запрос на подключение
        if (!window.ethereum) {
            alert('MetaMask не установлен. Пожалуйста, установите MetaMask для продолжения.');
            return;
        }

        provider = new ethers.providers.Web3Provider(window.ethereum);
        await provider.send("eth_requestAccounts", []); // Запрос аккаунтов
        signer = provider.getSigner();
        const account = await signer.getAddress();
        console.log('Подключен аккаунт:', account);

        // Сохранение состояния в localStorage
        localStorage.setItem('walletAddress', account);
        alert('Кошелек подключен: ' + account);

        // Обновление UI
        document.getElementById('walletAddress').textContent = account;
        document.getElementById('connect-evm').textContent = 'disconnect evm';
        document.getElementById('connect-evm').classList.add('disconnect-btn');
    } catch (error) {
        console.error('Ошибка подключения через ethers.js:', error);
        alert('Ошибка подключения к кошельку: ' + error.message);
    }
}

// Функция для отключения кошелька
function disconnectWallet() {
    localStorage.removeItem('walletAddress');
    document.getElementById('walletAddress').textContent = 'Кошелёк не подключён';
    document.getElementById('connect-evm').textContent = 'connect evm';
    document.getElementById('connect-evm').classList.remove('disconnect-btn');
    alert('Кошелек отключен');
}

// Проверка состояния при загрузке страницы
window.onload = () => {
    const savedAddress = localStorage.getItem('walletAddress');
    if (savedAddress) {
        console.log('Кошелек уже подключен:', savedAddress);
        document.getElementById('walletAddress').textContent = savedAddress;
        document.getElementById('connect-evm').textContent = 'disconnect evm';
        document.getElementById('connect-evm').classList.add('disconnect-btn');
    }
};

// Добавление событий к кнопкам подключения и отключения
document.getElementById('connect-evm').addEventListener('click', () => {
    if (document.getElementById('connect-evm').textContent === 'connect evm') {
        connectWallet();
    } else {
        disconnectWallet();
    }
});
