// connect.js
async function connectWallet() {
    if (typeof window.ethereum !== 'undefined') {
        try {
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            const account = accounts[0];
            document.getElementById('wallet-address').textContent = account;
            document.getElementById('connect-evm').textContent = 'disconnect evm';
            document.getElementById('connect-evm').classList.add('disconnect-btn');
        } catch (error) {
            console.error('Ошибка подключения:', error);
            document.getElementById('wallet-address').textContent = 'Ошибка подключения';
        }
    } else {
        alert('Пожалуйста, установите MetaMask или другой EVM-совместимый кошелек!');
    }
}

document.getElementById('connect-evm').addEventListener('click', () => {
    if (document.getElementById('connect-evm').textContent === 'connect evm') {
        connectWallet();
    } else {
        disconnectWallet();
    }
});

function disconnectWallet() {
    document.getElementById('wallet-address').textContent = 'Кошелёк не подключён';
    document.getElementById('connect-evm').textContent = 'connect evm';
    document.getElementById('connect-evm').classList.remove('disconnect-btn');
}

