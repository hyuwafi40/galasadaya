const sidebar = document.getElementById('sidebar');
const sidebarOverlay = document.getElementById('sidebarOverlay');
const openSidebarBtn = document.getElementById('openSidebar');
const closeSidebarBtn = document.getElementById('closeSidebar');

function toggleSidebar() {
    if (!sidebar || !sidebarOverlay) return;
    sidebar.classList.toggle('-translate-x-full');
    if (sidebar.classList.contains('-translate-x-full')) {
        sidebarOverlay.classList.add('hidden');
    } else {
        sidebarOverlay.classList.remove('hidden');
    }
}

if (openSidebarBtn && closeSidebarBtn && sidebarOverlay) {
    openSidebarBtn.addEventListener('click', toggleSidebar);
    closeSidebarBtn.addEventListener('click', toggleSidebar);
    sidebarOverlay.addEventListener('click', toggleSidebar);
}

const profileBtn = document.getElementById('profileBtn');
const profileMenu = document.getElementById('profileMenu');

if (profileBtn && profileMenu) {
    profileBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        profileMenu.classList.toggle('hidden');
        setTimeout(() => {
            profileMenu.classList.toggle('opacity-0');
            profileMenu.classList.toggle('scale-95');
        }, 10);
    });

    document.addEventListener('click', (e) => {
        if (!profileBtn.contains(e.target) && !profileMenu.contains(e.target) && !profileMenu.classList.contains('hidden')) {
            profileMenu.classList.add('opacity-0', 'scale-95');
            setTimeout(() => {
                profileMenu.classList.add('hidden');
            }, 150);
        }
    });
}

function showToast(toastItem) {
    toastItem.classList.remove('toast-hidden');
    toastItem.classList.add('toast-visible');
    setTimeout(() => hideToast(toastItem), 4000);
}

function hideToast(toastItem) {
    toastItem.classList.remove('toast-visible');
    toastItem.classList.add('toast-hidden');
    setTimeout(() => toastItem.remove(), 500);
}

document.addEventListener('click', (e) => {
    const closeToastBtn = e.target.closest('.close-toast');
    if (closeToastBtn) {
        const toastItem = closeToastBtn.closest('.toast-item');
        if (toastItem) hideToast(toastItem);
    }
});

document.querySelectorAll('.toast-item').forEach(toastItem => showToast(toastItem));

const modalOverlay = document.getElementById('modalOverlay');
const modalContent = document.getElementById('modalContent');

function openModal() {
    if (!modalOverlay || !modalContent) return;
    modalOverlay.classList.remove('hidden');
    setTimeout(() => {
        modalOverlay.classList.remove('opacity-0');
        modalContent.classList.remove('scale-95');
    }, 10);
}

function closeModal() {
    if (!modalOverlay || !modalContent) return;
    modalOverlay.classList.add('opacity-0');
    modalContent.classList.add('scale-95');
    setTimeout(() => {
        modalOverlay.classList.add('hidden');
    }, 300);
}

document.addEventListener('click', (e) => {
    const trigger = e.target.closest('[data-modal-open]');
    if (trigger) {
        const url = trigger.getAttribute('data-url');
        const form = modalOverlay?.querySelector('form');
        if (url && form) form.action = url;
        openModal();
        return;
    }

    if (e.target.closest('#cancelModal')) {
        closeModal();
        return;
    }

    if (e.target === modalOverlay) {
        closeModal();
    }
});