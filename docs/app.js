// Smooth scroll for nav links
document.querySelectorAll('nav a').forEach(function(link) {
  link.addEventListener('click', function(e) {
    e.preventDefault();
    var target = document.querySelector(this.getAttribute('href'));
    if (target) {
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});

// Highlight active nav link on scroll
var sections = document.querySelectorAll('.section');
var navLinks = document.querySelectorAll('nav a');

window.addEventListener('scroll', function() {
  var scrollPos = window.scrollY + 100;
  sections.forEach(function(section) {
    if (section.offsetTop <= scrollPos && section.offsetTop + section.offsetHeight > scrollPos) {
      navLinks.forEach(function(link) { link.style.color = ''; });
      var active = document.querySelector('nav a[href="#' + section.id + '"]');
      if (active) active.style.color = '#c49b5c';
    }
  });
});
