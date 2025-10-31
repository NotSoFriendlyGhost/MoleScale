# ⚖️ MoleScale

**MoleScale** is a unique educational tool that measures the amount of substance in **moles**. Built for the **2024 Maker Faire**, it combines an **Arduino with a load cell and HX711 amplifier** with a **Raspberry Pi touchscreen GUI** to automate chemistry calculations.

---

## ℹ️ About

Traditional lab scales only measure in grams, leaving students to calculate moles manually. MoleScale simplifies this process by automatically converting the weight of an object to moles based on user-inputted elements.  

The device was designed to **streamline chemistry experiments and education** by integrating hardware and software in a single interactive platform.

---

## ⚙️ Key Features

### ⚖️ Weight Measurement
- Load cell + HX711 module measures weight in grams.
- Arduino handles analog-to-digital conversion and sends the data via serial to the Raspberry Pi.

### 🖥 Touchscreen Interface
- Raspberry Pi GUI allows users to input the chemical element(s) being measured.
- Calculates and displays the number of moles in real time.
- User-friendly touchscreen controls for easy interaction during labs.

### 💡 Educational Utility
- Ideal for chemistry experiments where mole calculations are required.
- Helps students visualize the relationship between grams and moles.
- Can be extended to include multiple elements, compounds, or mixture calculations.

---

## 🛠 Tech Stack

| Component           | Details |
|--------------------|---------|
| **Microcontroller** | Arduino Uno / Nano |
| **Sensor**          | Load Cell + HX711 Amplifier |
| **Display**         | Raspberry Pi with Touchscreen |
| **Programming**     | Arduino C/C++ (weight measurement), Python (GUI + calculations) |
| **Communication**   | Serial between Arduino and Raspberry Pi |

---

## 🧠 How It Works

1. **Calibration:** Load cell is calibrated for accurate gram measurement.  
2. **Measurement:** Arduino reads the weight in grams from the load cell and sends it via serial to the Raspberry Pi.  
3. **Input Element:** User selects the element or compound in the Python GUI.  
4. **Calculation:** Program computes moles using the formula:

moles = mass_in_grams / molar_mass_of_element

yaml
Copy code

5. **Display:** Number of moles is displayed on the touchscreen in real-time.

---

## 📁 Repository Structure

```text
MoleScale/
├── firmware/            # Arduino code (HX711 + load cell)
├── gui/                 # Python GUI code for Raspberry Pi
├── docs/                # Schematics, diagrams, Maker Faire write-up
├── examples/            # Sample element inputs and testing scripts
└── README.md            # Project overview
