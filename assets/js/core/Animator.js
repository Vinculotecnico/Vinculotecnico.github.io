import { Logger } from './Logger.js';

/**
 * Handles Intersection Observer logic to trigger CSS animations when elements
 * scroll into the viewport. This ensures animations only run when visible.
 */
export class Animator {
  constructor() {
    this.elements = document.querySelectorAll('.animate-on-scroll');
    
    // Check for reduced motion preference
    this.prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    
    this.init();
  }

  init() {
    if (this.elements.length === 0) return;
    
    // If the user prefers reduced motion, make everything visible immediately
    if (this.prefersReducedMotion) {
      Logger.info('Reduced motion preference detected. Animations disabled.');
      this.elements.forEach(el => el.classList.add('is-visible'));
      return;
    }

    Logger.info(`Initializing Animator for ${this.elements.length} elements.`);
    
    const observerOptions = {
      root: null, // use the viewport
      rootMargin: '0px',
      threshold: 0.15 // trigger when 15% of the element is visible
    };

    const observer = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          // Once animated, stop observing to improve performance
          observer.unobserve(entry.target);
        }
      });
    }, observerOptions);

    this.elements.forEach(el => observer.observe(el));
  }
}
