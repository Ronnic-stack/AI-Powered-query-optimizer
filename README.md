# 🚀 AI-Powered Database Query Optimizer

> **Instantly reverse-engineer, debug, and rewrite sluggish SQL into production-ready operations.**

Database bottlenecks are a massive silent killer of application scale and compute budgets. A single bad nested subquery or missing index can bring an entire system to a crawl. This tool acts as an AI-powered Database Administrator that lives right in your browser—catching unoptimized code before it ever hits production.

<img width="2940" height="1726" alt="image" src="https://github.com/user-attachments/assets/d8937b48-8d26-4b26-8940-5b358ab8827f" />

## ✨ Key Features

* 🧠 **Advanced AI Refactoring:** Powered by Google's **Gemini 2.5 Flash** model. It doesn't just format text; it fundamentally rewrites logic (e.g., removing N+1 problems, updating implicit joins, flattening redundant subqueries).
* 👨‍🏫 **Educational Output:** Provides a detailed, bulleted explanation of *why* the old query was bad and *how* the new query saves compute costs.
* 🛡️ **Zero-Dependency "Firewall-Proof" UI:** The frontend is built with **100% pure native CSS and Vanilla JS**. Because it relies on zero external libraries or CDNs, it completely bypasses aggressive enterprise ad-blockers and Fortinet firewalls.
* 🎨 **Premium Aesthetic:** Features a custom glassmorphic input panel, animated glowing background orbs, and native dark mode for an enterprise-grade developer experience.
* 🔒 **Secure Architecture:** Environment variables keep API keys completely hidden from source control.

## 🛠️ Tech Stack

* **Frontend:** HTML5, Pure CSS3, Vanilla JavaScript (Zero external dependencies)
* **Backend:** Python, FastAPI, Uvicorn
* **AI Engine:** Google GenAI SDK (`gemini-2.5-flash`)

---

## 💻 How to Run Locally

It takes less than 2 minutes to spin up the local development environment.

### 1. Clone the Repository
```bash
git clone [https://github.com/Ronnic-stack/AI-Powered-query-optimizer.git](https://github.com/Ronnic-stack/AI-Powered-query-optimizer.git)
cd AI-Powered-query-optimizer
