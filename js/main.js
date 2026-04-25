// Meridian Concrete Solutions - Main JavaScript

(function() {
  'use strict';

  // DOM Ready
  document.addEventListener('DOMContentLoaded', init);

  function init() {
    initMobileMenu();
    initFAQAccordion();
    initSmoothScroll();
    initStickyHeader();
    initLazyImages();
    initFormValidation();
  }

  // Mobile Menu Toggle
  function initMobileMenu() {
    const toggle = document.querySelector('.menu-toggle');
    const nav = document.querySelector('.nav-links');

    if (!toggle || !nav) return;

    toggle.addEventListener('click', function() {
      nav.classList.toggle('active');
      const isOpen = nav.classList.contains('active');
      toggle.setAttribute('aria-expanded', isOpen);
      toggle.innerHTML = isOpen
        ? '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>'
        : '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>';
    });

    // Close on link click
    nav.querySelectorAll('a').forEach(function(link) {
      link.addEventListener('click', function() {
        if (window.innerWidth <= 768) {
          nav.classList.remove('active');
          toggle.setAttribute('aria-expanded', 'false');
          toggle.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>';
        }
      });
    });

    // Close on outside click
    document.addEventListener('click', function(e) {
      if (!nav.contains(e.target) && !toggle.contains(e.target)) {
        nav.classList.remove('active');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });
  }

  // FAQ Accordion
  function initFAQAccordion() {
    const questions = document.querySelectorAll('.faq-question');

    questions.forEach(function(btn) {
      btn.addEventListener('click', function() {
        const answer = btn.nextElementSibling;
        const isOpen = answer.classList.contains('open');

        // Close all others (single-open mode)
        questions.forEach(function(q) {
          q.classList.remove('active');
          const a = q.nextElementSibling;
          if (a) a.classList.remove('open');
        });

        // Toggle current
        if (!isOpen) {
          btn.classList.add('active');
          answer.classList.add('open');
          btn.setAttribute('aria-expanded', 'true');
          answer.setAttribute('aria-hidden', 'false');

          // Smooth height animation
          answer.style.maxHeight = answer.scrollHeight + 'px';
        } else {
          btn.setAttribute('aria-expanded', 'false');
          answer.setAttribute('aria-hidden', 'true');
          answer.style.maxHeight = '0';
        }
      });

      // Keyboard accessibility
      btn.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          btn.click();
        }
      });
    });
  }

  // Smooth Scroll for anchor links
  function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
      anchor.addEventListener('click', function(e) {
        const href = this.getAttribute('href');
        if (href === '#') return;

        const target = document.querySelector(href);
        if (target) {
          e.preventDefault();
          const headerOffset = 80;
          const top = target.getBoundingClientRect().top + window.pageYOffset - headerOffset;

          window.scrollTo({
            top: top,
            behavior: 'smooth'
          });

          // Update URL without jump
          history.pushState(null, null, href);
        }
      });
    });
  }

  // Sticky header shadow on scroll
  function initStickyHeader() {
    const header = document.querySelector('.site-header');
    if (!header) return;

    let ticking = false;

    window.addEventListener('scroll', function() {
      if (!ticking) {
        window.requestAnimationFrame(function() {
          if (window.scrollY > 10) {
            header.style.boxShadow = '0 1px 3px rgba(25, 24, 23, 0.08)';
          } else {
            header.style.boxShadow = 'none';
          }
          ticking = false;
        });
        ticking = true;
      }
    });
  }

  // Lazy-load images
  function initLazyImages() {
    if ('loading' in HTMLImageElement.prototype) {
      // Native lazy loading supported
      document.querySelectorAll('img[data-src]').forEach(function(img) {
        img.src = img.dataset.src;
      });
    } else {
      // Fallback for older browsers
      const lazyImages = document.querySelectorAll('img[data-src]');

      if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver(function(entries, observer) {
          entries.forEach(function(entry) {
            if (entry.isIntersecting) {
              const img = entry.target;
              img.src = img.dataset.src;
              img.removeAttribute('data-src');
              observer.unobserve(img);
            }
          });
        }, { rootMargin: '50px 0px', threshold: 0.01 });

        lazyImages.forEach(function(img) {
          imageObserver.observe(img);
        });
      }
    }
  }

  // Basic form validation
  function initFormValidation() {
    const forms = document.querySelectorAll('form[data-validate]');

    forms.forEach(function(form) {
      form.addEventListener('submit', function(e) {
        let isValid = true;
        const required = form.querySelectorAll('[required]');

        required.forEach(function(field) {
          const value = field.value.trim();
          const type = field.type;

          if (!value) {
            isValid = false;
            field.classList.add('error');
          } else {
            field.classList.remove('error');
          }

          // Email validation
          if (type === 'email' && value) {
            const emailRe = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRe.test(value)) {
              isValid = false;
              field.classList.add('error');
            }
          }

          // Phone validation (US format)
          if (type === 'tel' && value) {
            const phoneRe = /^[\d\s\-\(\)\+]{10,}$/;
            if (!phoneRe.test(value)) {
              isValid = false;
              field.classList.add('error');
            }
          }
        });

        if (!isValid) {
          e.preventDefault();
          const firstError = form.querySelector('.error');
          if (firstError) {
            firstError.focus();
          }
        }
      });

      // Clear error on input
      form.querySelectorAll('input, select, textarea').forEach(function(field) {
        field.addEventListener('input', function() {
          field.classList.remove('error');
        });
      });
    });
  }

})();