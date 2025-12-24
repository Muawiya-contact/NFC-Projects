# SFS: Secure File System

### Information Security Project – 3rd Semester  
**Under the supervision of Sir Khalid Mehmood**

---

## 👥 Project Team
- **Moavia Amir**
- **Mirza Muhammad Dawood**
- **Arslan Nasir**
- **Ali Raza**

---

## 📌 Project Overview

**SFS (Secure File System)** is a professional-grade, zero-knowledge encrypted file storage and sharing platform developed as part of the **Information Security course (3rd Semester)**.

The system utilizes the browser’s native **WebCrypto API** to perform **client-side encryption**, ensuring that all data is encrypted before being transmitted or stored. At no point are plaintext files or private cryptographic keys exposed to the server.

---

## 🚀 Deployment Guide

### 1. Prepare GitHub Repository
- Initialize the repository:
  ```bash
  git init
  ```

### 2. Vercel Deployment (Recommended)
- Connect the GitHub repository to **Vercel**
- Set the environment variable `API_KEY` with your **Google AI Studio API key**
- The project auto-configures using the included `vercel.json`

### 3. Netlify Deployment
- Connect the GitHub repository to **Netlify**
- Set the `API_KEY` in **Site Settings → Environment Variables**
- Routing and security headers are managed using `netlify.toml` and `_redirects`

---

## 🛡️ Security Specifications
- **Symmetric Encryption**: AES-256-GCM (file content encryption)
- **Asymmetric Encryption**: RSA-2048-OAEP (secure key wrapping)
- **Hash Algorithm**: SHA-256 (data integrity verification)
- **Zero-Knowledge Architecture**:
  - No plaintext files stored
  - No private keys transmitted
  - No sensitive data exposed on the server

---

## 🛠️ Key Features
- **Identity Provisioning**: Automatic RSA key-pair generation during user registration
- **Secure File Sharing**: RSA-based key re-encryption for authorized recipients
- **Neural Security Logic**: Gemini-3-Flash integration for cryptographic analysis
- **Immutable Audit Logging**: Real-time logging of security-sensitive operations

---

© 2025 **Coding Moves – Engineering Branch**  
Developed for academic purposes under the **Information Security curriculum**.
