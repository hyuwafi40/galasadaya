const formModal = document.getElementById('formModal');

if (formModal) {
    const form = formModal.querySelector('form');
    const modalContent = formModal.querySelector('.modal-content');
    const nameInput = form ? form.querySelector('#id_name') : null;

    function openFormModal(url, name) {
        if (form) {
            form.action = url;
        }
        if (nameInput) {
            nameInput.value = name || '';
        }
        formModal.classList.remove('hidden');
        requestAnimationFrame(() => {
            formModal.classList.remove('opacity-0');
            if (modalContent) {
                modalContent.classList.remove('scale-95');
            }
        });
    }

    function closeFormModal() {
        formModal.classList.add('opacity-0');
        if (modalContent) {
            modalContent.classList.add('scale-95');
        }
        setTimeout(() => {
            formModal.classList.add('hidden');
        }, 300);
    }

    document.addEventListener('click', (e) => {
        const trigger = e.target.closest('[data-form-open]');
        if (trigger) {
            e.preventDefault();
            const url = trigger.getAttribute('data-url') || '';
            const name = trigger.getAttribute('data-name') || '';
            openFormModal(url, name);
            return;
        }

        if (e.target.closest('[data-form-close]')) {
            closeFormModal();
        }
    });

    formModal.addEventListener('click', (e) => {
        if (e.target === formModal) {
            closeFormModal();
        }
    });
}