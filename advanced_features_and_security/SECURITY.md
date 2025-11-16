# Security Measures Implemented

## HTTPS & Secure Redirects
- `SECURE_SSL_REDIRECT = True` forces all traffic to HTTPS.
- HSTS configured:
  - `SECURE_HSTS_SECONDS = 31536000`
  - `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`
  - `SECURE_HSTS_PRELOAD = True`

## Secure Cookies
- `SESSION_COOKIE_SECURE = True`
- `CSRF_COOKIE_SECURE = True`

## Secure Headers
- `X_FRAME_OPTIONS = 'DENY'`
- `SECURE_CONTENT_TYPE_NOSNIFF = True`
- `SECURE_BROWSER_XSS_FILTER = True`

## Deployment Notes
- In production, configure web server (Nginx/Apache) with SSL/TLS certificates and HTTP→HTTPS redirects.
