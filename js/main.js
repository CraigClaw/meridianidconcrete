/**
 * Meridian Concrete Solutions - Main JavaScript
 * Smooth animations, interactive components, enhanced UX
 */
(function () {
  'use strict';
  document.addEventListener('DOMContentLoaded', init);
  function init() {
    initStickyHeader();
    initMobileNav();
    initFAQAccordion();
    initSmoothScroll();
    initScrollAnimations();
    initLazyImages();
    initFormValidation();
    initCounterAnimation();
    initParallax();
  }
  function initStickyHeader() {
    const header = document.querySelector('.site-header');
    if (!header) return;
    let ticking = false;
    function updateHeader() {
      if (window.scrollY > 40) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
      ticking = false;
    }
    window.addEventListener('scroll', function () {
      if (!ticking) {
        window.requestAnimationFrame(updateHeader);
        ticking = true;
      }
    }, { passive: true });
    updateHeader();
  }
  function initMobileNav() {
    const toggle = document.querySelector('.menu-toggle');
    const nav = document.querySelector('.nav-links');
    const body = document.body;
    if (!toggle || !nav) return;
    const closeBtn = document.createElement('button');
    closeBtn.className = 'nav-close-btn';
    closeBtn.setAttribute('aria-label', 'Close menu');
    closeBtn.innerHTML = `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>`;
    nav.appendChild(closeBtn);
    function openMenu() {
      nav.classList.add('active');
      toggle.setAttribute('aria-expanded', 'true');
      body.style.overflow = 'hidden';
    }
    function closeMenu() {
      nav.classList.remove('active');
      toggle.setAttribute('aria-expanded', 'false');
      body.style.overflow = '';
    }
    toggle.addEventListener('click', function () {
      if (nav.classList.contains('active')) {
        closeMenu();
      } else {
        openMenu();
      }
    });
    closeBtn.addEventListener('click', closeMenu);
    nav.querySelectorAll('a:not(.nav-close-btn)').forEach(function (link) {
      link.addEventListener('click', function () {
        closeMenu();
      });
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('active')) {
        closeMenu();
        toggle.focus();
      }
    });
    nav.addEventListener('click', function (e) {
      if (e.target === nav) {
        closeMenu();
      }
    });
  }
  function initFAQAccordion() {
    const items = document.querySelectorAll('.faq-item');
    items.forEach(function (item) {
      const question = item.querySelector('.faq-question');
      const answer = item.querySelector('.faq-answer');
      if (!question || !answer) return;
      question.addEventListener('click', function () {
        const isActive = item.classList.contains('is-active');
        items.forEach(function (otherItem) {
          if (otherItem !== item) {
            otherItem.classList.remove('is-active');
            const otherQuestion = otherItem.querySelector('.faq-question');
            const otherAnswer = otherItem.querySelector('.faq-answer');
            if (otherQuestion) otherQuestion.classList.remove('active');
            if (otherAnswer) otherAnswer.classList.remove('open');
          }
        });
        if (!isActive) {
          item.classList.add('is-active');
          question.classList.add('active');
          answer.classList.add('open');
          question.setAttribute('aria-expanded', 'true');
        } else {
          item.classList.remove('is-active');
          question.classList.remove('active');
          answer.classList.remove('open');
          question.setAttribute('aria-expanded', 'false');
        }
      });
      question.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          question.click();
        }
      });
    });
  }
  function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
      anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href === '#' || href === '#!' || href === '#0') return;
        const target = document.querySelector(href);
        if (target) {
          e.preventDefault();
          const headerHeight = document.querySelector('.site-header')
            ? document.querySelector('.site-header').offsetHeight
            : 0;
          const navHeight = document.querySelector('.main-nav-container')
            ? document.querySelector('.main-nav-container').offsetHeight
            : 0;
          const totalOffset = headerHeight + navHeight + 24;
          const targetPosition = target.getBoundingClientRect().top + window.pageYOffset;
          const top = targetPosition - totalOffset;
          window.scrollTo({
            top: top,
            behavior: 'smooth'
          });
          history.pushState(null, null, href);
        }
      });
    });
  }
  function initScrollAnimations() {
    if (!('IntersectionObserver' in window)) {
      document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-scale')
        .forEach(function (el) {
          el.classList.add('visible');
        });
      return;
    }
    const observerOptions = {
      root: null,
      rootMargin: '0px 0px -80px 0px',
      threshold: 0.1
    };
    const observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, observerOptions);
    document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-scale')
      .forEach(function (el) {
        observer.observe(el);
      });
  }
  function initCounterAnimation() {
    const counters = document.querySelectorAll('.stat-number[data-count]');
    if (!counters.length) return;
    if (!('IntersectionObserver' in window)) {
      counters.forEach(function (counter) {
        counter.textContent = counter.getAttribute('data-count');
      });
      return;
    }
    const observerOptions = {
      root: null,
      rootMargin: '0px',
      threshold: 0.5
    };
    const observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          animateCounter(entry.target);
          observer.unobserve(entry.target);
        }
      });
    }, observerOptions);
    counters.forEach(function (counter) {
      observer.observe(counter);
    });
    function animateCounter(element) {
      const target = parseInt(element.getAttribute('data-count'), 10);
      const duration = 2000;
      const start = 0;
      const startTime = performance.now();
      function update(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const easeOut = 1 - Math.pow(1 - progress, 3);
        const current = Math.round(start + (target - start) * easeOut);
        element.textContent = current + (element.getAttribute('data-suffix') || '');
        if (progress < 1) {
          requestAnimationFrame(update);
        }
      }
      requestAnimationFrame(update);
    }
  }
  function initParallax() {
    const heroImage = document.querySelector('.hero-image img');
    if (!heroImage) return;
    let ticking = false;
    window.addEventListener('scroll', function () {
      if (!ticking) {
        window.requestAnimationFrame(function () {
          const scrolled = window.pageYOffset;
          const heroSection = document.querySelector('.hero');
          if (heroSection) {
            const rect = heroSection.getBoundingClientRect();
            if (rect.bottom > 0) {
              const parallax = scrolled * 0.15;
              heroImage.style.transform = 'translateY(' + parallax + 'px) scale(1.05)';
            }
          }
          ticking = false;
        });
        ticking = true;
      }
    }, { passive: true });
  }
  function initLazyImages() {
    if ('loading' in HTMLImageElement.prototype) {
      document.querySelectorAll('img[data-src]').forEach(function (img) {
        img.src = img.dataset.src;
        img.removeAttribute('data-src');
      });
    } else if ('IntersectionObserver' in window) {
      const imageObserver = new IntersectionObserver(function (entries, observer) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            const img = entry.target;
            img.src = img.dataset.src;
            img.removeAttribute('data-src');
            observer.unobserve(img);
          }
        });
      }, { rootMargin: '50px 0px', threshold: 0.01 });
      document.querySelectorAll('img[data-src]').forEach(function (img) {
        imageObserver.observe(img);
      });
    }
  }
  function initFormValidation() {
    const forms = document.querySelectorAll('form[data-validate]');
    forms.forEach(function (form) {
      form.addEventListener('submit', function (e) {
        let isValid = true;
        const required = form.querySelectorAll('[required]');
        required.forEach(function (field) {
          const value = field.value.trim();
          const type = field.type;
          field.classList.remove('error');
          if (!value) {
            isValid = false;
            field.classList.add('error');
          }
          if (type === 'email' && value) {
            const emailRe = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRe.test(value)) {
              isValid = false;
              field.classList.add('error');
            }
          }
          if (type === 'tel' && value) {
            const phoneRe = /^[\d\s\-()+ ]{10,}$/;
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
            firstError.scrollIntoView({ behavior: 'smooth', block: 'center' });
          }
        }
      });
      form.querySelectorAll('input, select, textarea').forEach(function (field) {
        field.addEventListener('input', function () {
          field.classList.remove('error');
        });
        field.addEventListener('blur', function () {
          if (field.value.trim()) {
            field.classList.remove('error');
          }
        });
      });
    });
  }
  function initBackToTop() {
    const btn = document.createElement('button');
    btn.className = 'back-to-top';
    btn.setAttribute('aria-label', 'Back to top');
    btn.innerHTML = `<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"></polyline></svg>`;
    const style = document.createElement('style');
    style.textContent = `
      .back-to-top {
        position: fixed;
        bottom: 100px;
        right: 24px;
        width: 48px;
        height: 48px;
        background: var(--accent);
        color: white;
        border: none;
        border-radius: 50%;
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: var(--shadow-lg);
        opacity: 0;
        visibility: hidden;
        transform: translateY(20px);
        transition: all 0.3s ease;
        z-index: 998;
      }
      .back-to-top.visible {
        opacity: 1;
        visibility: visible;
        transform: translateY(0);
      }
      .back-to-top:hover {
        background: var(--accent-hover);
        transform: translateY(-2px);
        box-shadow: var(--shadow-xl);
      }
      @media (max-width: 768px) {
        .back-to-top { display: none; }
      }
    `;
    document.head.appendChild(style);
    document.body.appendChild(btn);
    btn.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
    let ticking = false;
    window.addEventListener('scroll', function () {
      if (!ticking) {
        window.requestAnimationFrame(function () {
          if (window.scrollY > 600) {
            btn.classList.add('visible');
          } else {
            btn.classList.remove('visible');
          }
          ticking = false;
        });
        ticking = true;
      }
    }, { passive: true });
  }
  setTimeout(initBackToTop, 1000);
})();