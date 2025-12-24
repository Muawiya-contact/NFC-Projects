# SSF: Secure File System

**Presented by Coding Moves**

SSF is a professional-grade, zero-knowledge encrypted file storage and sharing platform. It utilizes the browser's native WebCrypto API to ensure that data is encrypted on the client side before ever reaching a server.

## 🚀 Deployment Guide

### 1. Prepare GitHub Repository
*   Initialize a git repo: `git init`
*   Push your code: `git push origin main`

### 2. Vercel Deployment (Recommended)
1.  Connect your GitHub repo to **Vercel**.
2.  Set the Environment Variable `API_KEY` to your Google AI Studio key.
3.  The project will auto-configure using the included `vercel.json`.

### 3. Netlify Deployment
1.  Connect your GitHub repo to **Netlify**.
2.  Set the `API_KEY` environment variable in **Site Settings > Environment Variables**.
3.  Netlify will use the `netlify.toml` and `_redirects` files to handle routing and security headers.

## 🛡️ Security Specifications
*   **Symmetric Encryption**: AES-256-GCM for file content.
*   **Asymmetric Encryption**: RSA-2048-OAEP for key wrapping.
*   **Hash Algorithm**: SHA-256 for integrity checks.
*   **Zero-Knowledge**: No private keys or plaintext files are ever transmitted or stored on the server.

## 🛠️ Features
*   **Identity Provisioning**: Automatic RSA key pair generation on signup.
*   **Secure Sharing**: RSA-based key re-wrapping for secondary recipients.
*   **Neural Security Logic**: Integrated Gemini-3-Flash for cryptographic analysis.
*   **Immutable Audit**: Real-time logging of all security-sensitive events.

---
© 2025 Coding Moves Engineering Branch. All Rights Reserved.