tailwind.config = {
    theme: {
        extend: {
            fontFamily: {
                sans: ['Outfit', 'sans-serif'],
            },
            colors: {
                neon: {
                    pink: '#ff2a85',
                    cyan: '#00f0ff',
                    violet: '#8a2be2',
                    yellow: '#fcee0a'
                }
            }
        }
    }
};

document.addEventListener('DOMContentLoaded', function () {
    const searchForm = document.getElementById('search-form');
    if (searchForm) {
        searchForm.addEventListener('submit', function (e) {
            e.preventDefault();
            const input = searchForm.querySelector('input[name="q"]');
            const query = input.value.trim();
            if (query) {
                window.location.href = searchForm.getAttribute('action') + '?q=' + encodeURIComponent(query);
            } else {
                alert('Masukkan kata kunci pencarian.');
            }
        });
    }

    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    const mobileOverlay = document.getElementById('mobile-overlay');
    const menuIconOpen = document.getElementById('menu-icon-open');
    const menuIconClose = document.getElementById('menu-icon-close');

    if (mobileMenuBtn && mobileMenu && mobileOverlay) {
        function toggleMobileMenu() {
            const isOpen = mobileMenu.classList.toggle('open');
            mobileOverlay.classList.toggle('show', isOpen);
            menuIconOpen.classList.toggle('hidden', isOpen);
            menuIconClose.classList.toggle('hidden', !isOpen);
            mobileMenuBtn.setAttribute('aria-expanded', isOpen);
        }

        mobileMenuBtn.addEventListener('click', toggleMobileMenu);
        mobileOverlay.addEventListener('click', toggleMobileMenu);
    }

    const carouselSection = document.getElementById('hero-carousel');
    if (carouselSection) {
        const track = document.getElementById('carousel-track');
        const prevBtn = document.getElementById('carousel-prev');
        const nextBtn = document.getElementById('carousel-next');
        const dots = document.querySelectorAll('.carousel-dot');
        const slides = track ? track.children : [];
        let currentIndex = 0;
        let autoPlayInterval;

        function goToSlide(index) {
            if (slides.length === 0) return;
            if (index < 0) index = slides.length - 1;
            if (index >= slides.length) index = 0;
            currentIndex = index;
            track.style.transform = `translateX(-${currentIndex * 100}%)`;
            dots.forEach((dot, i) => {
                if (i === currentIndex) dot.classList.add('active');
                else dot.classList.remove('active');
            });
        }

        function nextSlide() {
            goToSlide(currentIndex + 1);
        }

        function prevSlide() {
            goToSlide(currentIndex - 1);
        }

        function startAutoPlay() {
            if (slides.length > 1) {
                autoPlayInterval = setInterval(nextSlide, 5000);
            }
        }

        function stopAutoPlay() {
            clearInterval(autoPlayInterval);
        }

        function resetAutoPlay() {
            stopAutoPlay();
            startAutoPlay();
        }

        if (prevBtn) prevBtn.addEventListener('click', function () {
            prevSlide();
            resetAutoPlay();
        });
        if (nextBtn) nextBtn.addEventListener('click', function () {
            nextSlide();
            resetAutoPlay();
        });
        dots.forEach(dot => {
            dot.addEventListener('click', function () {
                goToSlide(parseInt(dot.dataset.index, 10));
                resetAutoPlay();
            });
        });

        carouselSection.addEventListener('mouseenter', stopAutoPlay);
        carouselSection.addEventListener('mouseleave', startAutoPlay);

        goToSlide(0);
        startAutoPlay();
    }
});