# ENG2002
ENG2002 team work
# PolyU Python Assignment 3: 3D Vector Program (Group 19)

## 👥 Team Members & Responsibilities
* **Lihuailin (25097331D)**: User search/authentication function (Credit Part), main menu interface design, and PowerPoint slides.
* **Chen Yizhou (25090387D)**: Development of the `vazmAng` subclass and implementation of the manual `arctan` algorithm (Distinction Part).
* **LI Zhiheng (25090479D)**: Development of the `vazmAng` subclass and methods, and PowerPoint slides.

---

## 📌 Team Task: Task 4 — Magnitude Comparison
Based on our team number (19), we are assigned **Task 4** ($19 \pmod 5 = 4$).

### Task Objectives
* **Primary Function**: Implement a method to perform a magnitude comparison between our 3D vector and another 3D vector.
* **Calculation Logic**: The comparison must be based on the **square of the magnitude** of each vector ($a^2 + b^2 + c^2$).
* **Return Values**:
    * `0`: Both vectors have the same magnitude.
    * `-1`: The other 3D vector has a larger magnitude.
    * `1`: The other 3D vector has a smaller magnitude.

---

## 🛠️ Core Requirements
* **Class Design**: Implement a class named `threeDVec` representing a 3D vector $(ai + bj + ck)$, where $a$, $b$, and $c$ are floating-point numbers.
* **Exception Handling**: If the value of $a$ is zero during initialization, use a `try...except` block to show an error and force the user to re-enter the value. No object in the program is allowed to have $a = 0$.
* **Modular Structure**: The class and its methods must be built as a **separate library module** and imported by the main program.
* **Restrictions**: 
    * **NO** NumPy or any standard libraries are allowed for computation.
    * Only use techniques and functions taught in lessons.
* **User Interface**: Provide a text menu that allows users to repeatedly enter vector values and exit via a specific option.

---

## 🏆 Grading Tiers

### 💳 Credit Grade (User Authentication)
* **Login System**: Require a username upon startup, checked against a text file containing username-PIN pairs.
* **New Users**: If the username is new, ask for a PIN and save it to the file.
* **Security**: The program ends if the user fails to provide the correct PIN in **three consecutive trials**.

### 🎖️ Distinction Grade (Advanced Math)
* **Sub-class**: Develop `vazmAng` inherited from `threeDVec`.
* **Manual Arctan**: Implement a method for the arctan function using the provided formula (do NOT use built-in Python math libraries).
* **Azimuthal Angle**: Return the angle using `arctan(b/a)` for vectors where $a > 0$.
* **Constraint**: Raise a `ValueError` if the input does not satisfy $-1 \le b/a \le 1$ and terminate the program.

---

## 📅 Deadlines & Submission
* **Due Date**: On or before **18 April 2026**.
* **Files**: Zip all project folders (Jupyter Notebook `.ipynb` and Python `.py` files).
* **Video**: A presentation video is required; each member must present for **5 to 6 minutes**.