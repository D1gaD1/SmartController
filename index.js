function toggleElement(id) {
  const element = document.getElementById(id);
  if (element.style.maxHeight) {
      element.style.maxHeight = null;
  } else {
      element.style.maxHeight = element.scrollHeight + "px";
  }
}

document.getElementById('login').addEventListener('click', function() {
  toggleElement('login-window');
});

document.getElementById('controller').addEventListener('click', function() {
  toggleElement('controller-window');
});

document.getElementById('logs').addEventListener('click', function() {
  toggleElement('logs-window');
});

document.getElementById('toggle-sidebar').addEventListener('click', function() {
  const sidebar = document.getElementById('sidebar');
  if (sidebar.classList.contains('show')) {
      sidebar.classList.remove('show');
  } else {
      sidebar.classList.add('show');
  }
});

// Rest of the JavaScript code...
