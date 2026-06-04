/**
 * Simple Logger utility conforming to SOLID principles.
 * Single Responsibility: Only handles logging to console (could be extended to send to external service).
 */
export class Logger {
  static info(message, data = null) {
    console.log(`[INFO] ${message}`, data ? data : '');
  }

  static warn(message, data = null) {
    console.warn(`[WARN] ${message}`, data ? data : '');
  }

  static error(message, error = null) {
    console.error(`[ERROR] ${message}`, error ? error : '');
  }
}
