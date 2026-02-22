Since your virtual environment is in the root folder, it’s actually easier for someone else to set up because the `.venv` is already there—though they’ll still need to activate it to match your **Fedora** environment.

Here is the updated **README.md** with the University details at the top and the specific local pathing for your project.

---

# Baum-Welch Hidden Markov Model (HMM) Dashboard

**Name:** Rohan Shyam

**Roll Number:** [Insert Roll Number]

**University:** IIT Madras BS Degree

---

## 🚀 Project Overview

An interactive dashboard for analyzing Hidden Markov Models using the Baum-Welch algorithm. This project allows users to input observation sequences and visualize the optimization of Transition (A) and Emission (B) matrices.

### 🛠️ Tech Stack

* **Backend:** Django, Django REST Framework, NumPy
* **Frontend:** Next.js, React, Tailwind CSS
* **Environment:** Developed and tested on Fedora Linux

---

## 💻 Local Execution Instructions

### 1. Prerequisites

Ensure you have **Python 3.11+** and **Node.js** installed on your machine.

### 2. Backend Setup

The virtual environment is located in the root directory.

1. Navigate to the root folder of the project.
2. Activate the virtual environment:
```bash
source .venv/bin/activate

```


3. Navigate to the server directory:
```bash
cd server

```


4. Run the server:
```bash
python manage.py runserver

```


*The API will be live at `http://127.0.0.1:8000*`

### 3. Frontend Setup

1. Open a new terminal.
2. Navigate to the client directory:
```bash
cd client

```


3. Install dependencies and run the development server:
```bash
npm install
npm run dev

```


*Access the dashboard at `http://localhost:3000*`

---

## ⚙️ Core Logic: Baum-Welch Algorithm

The algorithm performs iterative expectation-maximization to find the maximum likelihood estimates of HMM parameters.

1. **Expectation (E-step):** Calculates forward () and backward () probabilities.
2. **Maximization (M-step):** Updates the A, B, and  matrices based on the calculated probabilities.

---

### One Final Warning

Make sure the `fetch` call in `client/src/app/page.js` is set to `http://127.0.0.1:8000/api/run/`. If it still points to **Render** or **Railway**, the local frontend won't be able to talk to your local backend.

Would you like me to add a **troubleshooting** section for common Python/Node version issues?
