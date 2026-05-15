// Dark/Light mode toggle
const toggleBtn = document.getElementById('toggleMode');
if (toggleBtn) {
  toggleBtn.addEventListener('click', () => {
    const html = document.documentElement;
    const theme = html.getAttribute('data-bs-theme');
    html.setAttribute('data-bs-theme', theme === 'dark' ? 'light' : 'dark');
    localStorage.setItem('theme', html.getAttribute('data-bs-theme'));
  });
  // Load theme from localStorage
  window.addEventListener('DOMContentLoaded', () => {
    const saved = localStorage.getItem('theme');
    if (saved) document.documentElement.setAttribute('data-bs-theme', saved);
    toggleBtn.textContent = document.documentElement.getAttribute('data-bs-theme') === 'dark' ? '🌙 / ☀️' : '☀️ / 🌙';
  });
}

// Dynamic key hint update
const algorithmSelect = document.getElementById('algorithmSelect');
const keyHint = document.getElementById('keyHint');
const keyDesc = document.getElementById('keyDesc');
const keyInput = document.getElementById('keyInput');
if (algorithmSelect && keyHint && keyDesc && keyInput) {
  const hints = {
    'caesar': '0-25',
    'vigenere': 'A-Z',
    'affine': 'a dan b dipisah koma',
    'hill2': '4 angka dipisah koma',
    'hill3': '9 angka dipisah koma',
    'playfair': 'A-Z'
  };
  const labels = {
    'caesar': 'Key (angka)',
    'vigenere': 'Key (teks)',
    'affine': 'Key a,b (misal: 5,8)',
    'hill2': 'Key 2x2 (4 angka, misal: 3,3,2,5)',
    'hill3': 'Key 3x3 (9 angka, misal: 6,24,1,13,16,10,20,17,15)',
    'playfair': 'Key (teks)'
  };
  algorithmSelect.addEventListener('change', function() {
    const val = this.value;
    keyDesc.textContent = hints[val] || '';
    keyInput.placeholder = labels[val] || '';
  });

  const currentValue = algorithmSelect.value;
  keyDesc.textContent = hints[currentValue] || keyDesc.textContent;
  keyInput.placeholder = labels[currentValue] || keyInput.placeholder;
}
