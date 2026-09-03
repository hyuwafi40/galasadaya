document.addEventListener('DOMContentLoaded', function () {
    const usernameInput = document.getElementById('id_username');
    if (usernameInput) {
        usernameInput.focus();
    }

    const togglePasswordBtn = document.getElementById('toggle-password');
    const passwordInput = document.getElementById('id_password');

    if (togglePasswordBtn && passwordInput) {
        togglePasswordBtn.addEventListener('click', function () {
            const isPassword = passwordInput.type === 'password';
            passwordInput.type = isPassword ? 'text' : 'password';
            togglePasswordBtn.innerHTML = isPassword
                ? '<i class="fa-solid fa-eye-slash"></i>'
                : '<i class="fa-solid fa-eye"></i>';
            togglePasswordBtn.setAttribute('aria-label', isPassword ? 'Sembunyikan password' : 'Tampilkan password');
        });
    }

    const loginForm = document.getElementById('login-form');
    const loginBtn = document.getElementById('login-submit');
    const btnText = document.getElementById('login-btn-text');
    const btnLoader = document.getElementById('login-btn-loader');

    if (loginForm && loginBtn && btnText && btnLoader) {
        loginForm.addEventListener('submit', function (event) {
            if (!loginForm.checkValidity()) {
                return;
            }
            loginBtn.disabled = true;
            btnText.textContent = 'Memproses...';
            btnLoader.classList.remove('hidden');
        });
    }
});