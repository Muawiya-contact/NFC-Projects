# Medical Store Management System (MSMS)

A full-stack pharmacy management app built for the Database Lab course. It covers
day-to-day medical store operations: medicine inventory with batch and expiry
tracking, a point-of-sale screen with prescription validation, and management of
customers, suppliers, doctors, employees, and payments. The database does much of
the heavy lifting — 12 normalized tables (3NF) plus auxiliary tables, 4 triggers
(stock deduction, low-stock alerts, order total recalculation, expiry checks),
4 stored procedures (GenerateBill, RestockMedicine, PlaceOrder, CompletePayment),
7 reporting views, and indexes on frequent query columns.

Other features: JWT authentication with role-based access (Admin / Manager /
Pharmacist / Cashier), a reports page with a sales chart and CSV export, printable
invoices with A5 PDF download, dark mode, and low-stock / expiry alerts on the
dashboard.

Tech stack: React 18 + Vite + TailwindCSS + Recharts frontend, Node.js/Express 4
backend with mysql2, MySQL 8.0, JWT + bcryptjs auth, react-hook-form + Zod,
jsPDF + html2canvas for bills.

## Prerequisites

- Node.js v18+ and npm v9+
- MySQL 8.0 running locally

## Setup

```bash
git clone https://github.com/Coding-Moves/BSAI-Projects.git
cd BSAI-Projects/msms
npm run install:all        # installs root, backend, and frontend packages
```

Configure the backend environment:

```bash
cd backend
cp .env.example .env       # then fill in your MySQL credentials
```

## Database setup

Run the SQL files in `database/` against your MySQL server in this order:

```bash
mysql -u root -p < database/schema.sql
mysql -u root -p msms_db < database/sample_data.sql
mysql -u root -p msms_db < database/triggers.sql
mysql -u root -p msms_db < database/stored_procedures.sql
mysql -u root -p msms_db < database/views.sql
mysql -u root -p msms_db < database/indexes.sql
```

(You can also `SOURCE` them from MySQL Workbench in the same order.)

## Run

From the project root:

```bash
npm run dev
```

This starts both servers concurrently — backend API at http://localhost:5000,
frontend at http://localhost:5173. You can also run them separately with
`npm run server` and `npm run client`.

Default login: username `admin`, password `admin123`. Change it after first login.

Project documents (proposal, manual, ER diagram) are in `docs/`.

## Credits

Moavia (Muawiya) Amir — 2k24_BSAI_72, BS Artificial Intelligence, 4th Semester.
Database Lab, Instructor: Sir Ahsan Ahmed.
