'use strict';

const filters = document.querySelector('.filters');
const sections = [...document.querySelectorAll('[data-resource-section]')];
const resultMessage = document.getElementById('filter-result');

function showCategory(category, moveFocus = false) {
  if (!filters) return;
  const buttons = [...filters.querySelectorAll('[data-filter]')];
  const active = buttons.find(button => button.dataset.filter === category);
  if (!active) return;
  buttons.forEach(button => button.setAttribute('aria-pressed', String(button === active)));
  sections.forEach(section => { section.hidden = category !== 'all' && section.dataset.resourceSection !== category; });
  if (resultMessage) resultMessage.textContent = category === 'all'
    ? 'Tüm destek içerikleri gösteriliyor.'
    : `${active.textContent.trim()} gösteriliyor.`;
  if (moveFocus) active.focus({preventScroll: true});
}

if (filters) {
  filters.hidden = false;
  filters.addEventListener('click', event => {
    const button = event.target.closest('[data-filter]');
    if (button) showCategory(button.dataset.filter);
  });
  document.querySelectorAll('[data-show-category]').forEach(link => {
    link.addEventListener('click', () => { showCategory(link.dataset.showCategory); });
  });
}

// A directly shared section or activity link must remain visible after filtering.
function revealHashTarget() {
  let target;
  try { target = document.getElementById(decodeURIComponent(location.hash.slice(1))); }
  catch { return; }
  if (!target) return;
  const section = target.closest('[data-resource-section]');
  if (section && section.hidden) showCategory(section.dataset.resourceSection);
  if (target.matches('details')) target.open = true;
}
window.addEventListener('hashchange', revealHashTarget);
revealHashTarget();
