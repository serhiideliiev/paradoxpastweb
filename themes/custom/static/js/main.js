// Project Paradox Past - Main JavaScript
// Modern ES6+ JavaScript for interactive features

/**
 * Initialize the site when DOM is loaded
 */
document.addEventListener('DOMContentLoaded', function() {
  initializeNavigation();
  initializeSearch();
  initializeSmoothScrolling();
  initializePerformanceOptimizations();
});

/**
 * Mobile Navigation Management
 */
function initializeNavigation() {
  const navToggle = document.querySelector('.nav-toggle');
  const navMenu = document.querySelector('.nav-menu');
  
  if (!navToggle || !navMenu) return;
  
  // Toggle mobile menu
  navToggle.addEventListener('click', function(e) {
    e.preventDefault();
    const isExpanded = navToggle.getAttribute('aria-expanded') === 'true';
    
    navToggle.setAttribute('aria-expanded', !isExpanded);
    navToggle.classList.toggle('nav-open');
    navMenu.classList.toggle('active');
  });
  
  // Close mobile menu when clicking on navigation links
  const navLinks = document.querySelectorAll('.nav-links a');
  navLinks.forEach(link => {
    link.addEventListener('click', () => {
      navToggle.setAttribute('aria-expanded', 'false');
      navToggle.classList.remove('nav-open');
      navMenu.classList.remove('active');
    });
  });
  
  // Close mobile menu when clicking outside
  document.addEventListener('click', function(event) {
    if (!navToggle.contains(event.target) && !navMenu.contains(event.target)) {
      navToggle.setAttribute('aria-expanded', 'false');
      navToggle.classList.remove('nav-open');
      navMenu.classList.remove('active');
    }
  });
  
  // Handle ESC key to close mobile menu
  document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape' && navMenu.classList.contains('active')) {
      navToggle.setAttribute('aria-expanded', 'false');
      navToggle.classList.remove('nav-open');
      navMenu.classList.remove('active');
      navToggle.focus();
    }
  });
}

/**
 * Initialize search functionality (placeholder for future implementation)
 */
function initializeSearch() {
  const searchInputs = document.querySelectorAll('input[type="search"]');
  
  searchInputs.forEach(input => {
    input.addEventListener('input', debounce(function(e) {
      const query = e.target.value.trim();
      if (query.length > 2) {
        // Future: Implement search functionality
        console.log('Search query:', query);
      }
    }, 300));
  });
}

/**
 * Smooth scrolling for anchor links
 */
function initializeSmoothScrolling() {
  const anchorLinks = document.querySelectorAll('a[href^="#"]');
  
  anchorLinks.forEach(link => {
    link.addEventListener('click', function(e) {
      const href = this.getAttribute('href');
      if (href === '#') return;
      
      const target = document.querySelector(href);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
        
        // Update URL without triggering navigation
        if (history.pushState) {
          history.pushState(null, null, href);
        }
      }
    });
  });
}

/**
 * Performance optimizations
 */
function initializePerformanceOptimizations() {
  // Lazy load images (if supported)
  if ('loading' in HTMLImageElement.prototype) {
    const images = document.querySelectorAll('img[data-src]');
    images.forEach(img => {
      img.src = img.dataset.src;
      img.removeAttribute('data-src');
    });
  } else {
    // Fallback for browsers that don't support lazy loading
    const script = document.createElement('script');
    script.src = 'https://polyfill.io/v3/polyfill.min.js?features=IntersectionObserver';
    document.head.appendChild(script);
  }
  
  // Preload critical resources
  const criticalResources = [
    '/theme/css/style.css',
    '/theme/fonts/inter.woff2' // If we add custom fonts
  ];
  
  criticalResources.forEach(resource => {
    const link = document.createElement('link');
    link.rel = 'preload';
    link.as = resource.endsWith('.css') ? 'style' : 'font';
    link.href = resource;
    if (resource.endsWith('.woff2')) {
      link.type = 'font/woff2';
      link.crossOrigin = 'anonymous';
    }
    document.head.appendChild(link);
  });
}

/**
 * Utility function: Debounce
 */
function debounce(func, wait, immediate) {
  let timeout;
  return function executedFunction() {
    const context = this;
    const args = arguments;
    const later = function() {
      timeout = null;
      if (!immediate) func.apply(context, args);
    };
    const callNow = immediate && !timeout;
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
    if (callNow) func.apply(context, args);
  };
}

/**
 * Newsletter subscription handling
 */
function handleNewsletterSubmission(form) {
  const emailInput = form.querySelector('input[type="email"]');
  const errorElement = form.querySelector('.error-message, .sr-only');
  
  if (!emailInput || !errorElement) return false;
  
  const email = emailInput.value.trim();
  
  // Basic validation
  if (!email) {
    showError(errorElement, 'Please enter your email address.');
    return false;
  }
  
  // Email format validation
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email)) {
    showError(errorElement, 'Please enter a valid email address.');
    return false;
  }
  
  // Clear any previous errors
  clearError(errorElement);
  
  // Simulate newsletter subscription (replace with actual implementation)
  console.log('Newsletter subscription:', email);
  
  // Show success message
  showSuccess(form, 'Thank you for subscribing!');
  emailInput.value = '';
  
  return false; // Prevent form submission
}

/**
 * Show error message
 */
function showError(element, message) {
  element.textContent = message;
  element.className = 'error-message';
  element.setAttribute('role', 'alert');
}

/**
 * Clear error message
 */
function clearError(element) {
  element.textContent = '';
  element.className = 'sr-only';
  element.removeAttribute('role');
}

/**
 * Show success message
 */
function showSuccess(form, message) {
  const successElement = form.querySelector('.success-message') || 
                        document.createElement('div');
  
  successElement.className = 'success-message';
  successElement.textContent = message;
  successElement.setAttribute('role', 'status');
  
  if (!form.contains(successElement)) {
    form.appendChild(successElement);
  }
  
  // Remove success message after 5 seconds
  setTimeout(() => {
    if (form.contains(successElement)) {
      form.removeChild(successElement);
    }
  }, 5000);
}

// Export functions for use in templates
window.handleNewsletterSubmission = handleNewsletterSubmission;
