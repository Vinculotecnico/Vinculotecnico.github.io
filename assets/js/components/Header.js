import { Logger } from '../core/Logger.js';

/**
 * Handles Header interactivity (mobile menu).
 * Adheres to SRP by only managing the header DOM element.
 */
export class Header {
  constructor(headerElement) {
    if (!headerElement) {
      Logger.warn('Header element not found on page.');
      return;
    }
    
    this.header = headerElement;
    this.menuToggle = this.header.querySelector('.mobile-menu-toggle');
    this.mainNav = this.header.querySelector('.main-nav');
    
    this.init();
  }

  init() {
    if (this.menuToggle && this.mainNav) {
      this.menuToggle.addEventListener('click', () => this.toggleMenu());
    }
  }

  toggleMenu() {
    const isOpen = this.mainNav.classList.contains('is-open');
    if (isOpen) {
      this.mainNav.classList.remove('is-open');
      this.menuToggle.setAttribute('aria-expanded', 'false');
    } else {
      this.mainNav.classList.add('is-open');
      this.menuToggle.setAttribute('aria-expanded', 'true');
    }
    Logger.info(`Mobile menu toggled: ${!isOpen}`);
  }
}
