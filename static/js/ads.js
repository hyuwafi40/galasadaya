const formModal = document.getElementById('formModal');

if (formModal) {
    const form = formModal.querySelector('form');
    const modalContent = formModal.querySelector('.modal-content');

    function openFormModal(url, data) {
        if (form) {
            form.reset();
            form.action = url;
            if (data) {
                Object.keys(data).forEach(key => {
                    const input = form.querySelector(`#id_${key}`);
                    if (!input) return;
                    if (input.type === 'checkbox') {
                        input.checked = (data[key] === 'true' || data[key] === '1');
                    } else {
                        input.value = data[key];
                    }
                });
            }
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
            const data = {};
            Array.from(trigger.attributes).forEach(attr => {
                if (attr.name.startsWith('data-') && attr.name !== 'data-url' && attr.name !== 'data-form-open') {
                    data[attr.name.slice(5)] = attr.value;
                }
            });
            openFormModal(url, data);
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