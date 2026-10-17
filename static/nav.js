// Shared header behaviour: mobile menu, current-page highlight, shadow on scroll.
function toggleMenu() {
  const menu = document.getElementById('navMenu');
  if (menu) menu.classList.toggle('active');
}

document.addEventListener('DOMContentLoaded', () => {
  const menu = document.getElementById('navMenu');
  const header = document.querySelector('header');
  const path = location.pathname.replace(/\/+$/, '') || '/';

  document.querySelectorAll('#navMenu a').forEach((a) => {
    const target = new URL(a.href, location.origin).pathname.replace(/\/+$/, '') || '/';
    if (target === path) { a.classList.add('current'); a.setAttribute('aria-current', 'page'); }
    a.addEventListener('click', () => menu && menu.classList.remove('active'));
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && menu) menu.classList.remove('active');
  });
  document.addEventListener('click', (e) => {
    if (menu && !e.target.closest('header')) menu.classList.remove('active');
  });

  const onScroll = () => header && header.classList.toggle('scrolled', window.scrollY > 8);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });
});
