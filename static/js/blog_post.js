// When the user scrolls the page, execute scrollBar
window.onscroll = () => {
  scrollBar();
};

const scrollBar = () => {
  let winScroll = document.body.scrollTop || document.documentElement.scrollTop;
  let height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
  let scrolled = (winScroll / height) * 100;
  document.getElementById("myBar").style.width = scrolled + "%";
};

// HTMX CSRF Token
document.body.addEventListener('htmx:configRequest', (event) => {
  event.detail.headers['X-CSRFToken'] = '{{ csrf_token }}';
});

// Delete Confirmation Toggle
const toggleDelete = () => {
  let deleteButton = document.getElementById('delete-button');
  let deleteConfirm = document.querySelector('.delete-confirm');

  deleteButton.addEventListener('click', () => {
    if (deleteConfirm.style.display === 'none') {
      deleteConfirm.style.display = 'flex';
    } else {
      deleteConfirm.style.display = 'none';
    }
  });
};

window.onload = () => {
  toggleDelete();
};
