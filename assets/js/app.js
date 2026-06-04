import { Logger } from './core/Logger.js';
import { Header } from './components/Header.js';

/**
 * Main Application class
 * Coordinates initialization of components based on the DOM.
 */
class App {
  constructor() {
    this.components = {};
  }

  init() {
    Logger.info('Vínculo Técnico App initializing...');
    
    // Initialize components if they exist on the current page
    this.initComponents();
    
    Logger.info('App initialization complete.');
  }

  initComponents() {
    const headerElement = document.querySelector('.site-header');
    if (headerElement) {
      this.components.header = new Header(headerElement);
    }
  }
}

// Bootstrap the application when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
  const app = new App();
  app.init();
});
