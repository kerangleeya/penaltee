function showToast(title, message, type = 'normal', duration = 3000) {
  const toastComponent = document.getElementById('toast-component');
  const toastTitle = document.getElementById('toast-title');
  const toastMessage = document.getElementById('toast-message');

  if (!toastComponent) return;

  // Reset style
  toastComponent.className = `
    fixed bottom-8 right-8 px-6 py-4 rounded-xl shadow-2xl border-2
    z-50 opacity-0 translate-y-8 pointer-events-none transition-all duration-500 ease-out max-w-sm w-fit
  `;

  // Apply theme
  if (type === 'success') {
    toastComponent.classList.add('bg-green-50', 'border-green-400', 'text-green-800');
  } else if (type === 'error') {
    toastComponent.classList.add('bg-red-50', 'border-red-400', 'text-red-800');
  } else {
    toastComponent.classList.add('bg-white', 'border-gray-300', 'text-gray-900');
  }

  // Set content
  toastTitle.textContent = title;
  toastMessage.textContent = message;

  // Show
  toastComponent.classList.remove('opacity-0', 'translate-y-8');
  toastComponent.classList.add('opacity-100', 'translate-y-0');

  // Hide after delay
  setTimeout(() => {
    toastComponent.classList.remove('opacity-100', 'translate-y-0');
    toastComponent.classList.add('opacity-0', 'translate-y-8');
  }, duration);
}
