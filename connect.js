// Подключение ethers.js
import { ethers } from 'ethers';

let connectBtn = document.getElementById('connect-evm');
let walletAddress = document.getElementById('wallet-address');

connectBtn.addEventListener('click', async () => {
    if (connectBtn.textContent === 'connect evm') {
        if (window.ethereum) {
            try {
                // Подключение к MetaMask
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
    } else {
        // Логика отключения кошелька
        walletAddress.textContent = 'Кошелёк не подключён';
        connectBtn.textContent = 'connect evm';
        connectBtn.classList.remove('disconnect-btn');
    }
});
