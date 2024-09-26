// Проверяем, что элементы корректно связаны
const connectBtn = document.getElementById('connect-evm');
const walletAddress = document.getElementById('wallet-address');

if (connectBtn && walletAddress) {
    // Функция подключения кошелька
    async function connectWallet() {
        try {
            if (window.ethereum) {
                const provider = new ethers.providers.Web3Provider(window.ethereum);
                await provider.send("eth_requestAccounts", []);
                const signer = provider.getSigner();
                const account = await signer.getAddress();

                // Обновление состояния интерфейса после подключения
                walletAddress.textContent = account;
                connectBtn.textContent = 'disconnect evm';
                connectBtn.classList.add('disconnect-btn');
            } else {
                alert('Пожалуйста, установите MetaMask или другой EVM-совместимый кошелек!');
            }
        } catch (error) {
            console.error('Ошибка при подключении к кошельку:', error);
            walletAddress.textContent = 'Ошибка подключения';
        }
    }

    // Функция отключения кошелька
    function disconnectWallet() {
        walletAddress.textContent = 'Кошелёк не подключён';
        connectBtn.textContent = 'connect evm';
        connectBtn.classList.remove('disconnect-btn');
    }

    // Событие для кнопки подключения/отключения
    connectBtn.addEventListener('click', () => {
        if (connectBtn.textContent === 'connect evm') {
            connectWallet();
        } else {
            disconnectWallet();
        }
    });

    // Экспорт функций для вызова в profile.html
    window.connectWallet = connectWallet;
} else {
    console.error("Кнопка подключения или элемент отображения адреса кошелька не найдены.");
}
