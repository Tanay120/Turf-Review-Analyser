# Turf Review Analyser ⚽

A full-stack web application that allows users to browse and book sports turfs. The standout feature is a sentiment analysis model built with KerasNLP that predicts a star rating based on user-submitted text reviews.



---

## ✨ Features

* **Turf Listings:** Browse available sports turfs with details on location and price.
* **AI-Powered Reviews:** Submit a text review and see the AI model predict a 1-5 star rating in real-time.
* **Dynamic Ratings:** The average rating for each turf updates automatically after each new review.
* **Theme Toggle:** Switch between a light and dark mode for comfortable viewing.
* **Responsive Design:** A clean, modern UI that works on both desktop and mobile devices.

---

## 🛠️ Tech Stack

* **Frontend:** HTML5, Tailwind CSS, Vanilla JavaScript
* **Backend:** Python, Flask
* **Machine Learning:** TensorFlow, Keras, KerasNLP (DistilBERT model)
* **Version Control:** Git & Git LFS for handling the large model file.

---

## 🚀 Setup and Installation

To run this project locally, please follow these steps.

### **Prerequisites**

Make sure you have the following installed on your system:
* [Python 3.10+](https://www.python.org/downloads/)
* [Git](https://git-scm.com/downloads/)
* [Git LFS](https://git-lfs.github.com/)

### **Installation**

1.  **Clone the repository:**
    This project uses Git LFS. Ensure it's installed before cloning.
    ```bash
    git clone [https://github.com/Tanay120/Turf-Review-Analyser.git](https://github.com/Tanay120/Turf-Review-Analyser.git)
    cd Turf-Review-Analyser
    ```

2.  **Create and activate a virtual environment:**
    * **For Linux/macOS:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    * **For Windows:**
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Install the required packages:**
    The `requirements.txt` file contains all the necessary Python libraries.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Flask application:**
    ```bash
    flask --app app run
    ```

5.  **Access the application:**
    Open your web browser and navigate to `http://localhost:5000`.

---

## 🧠 How the Sentiment Analysis Works

The core of this project is the sentiment analysis model that predicts star ratings.

1.  A user writes a review (e.g., "The field was fantastic and clean.") and submits it.
2.  The frontend sends this raw text to the `/predict` endpoint of the Flask backend.
3.  The pre-trained `DistilBERT` model, loaded via KerasNLP, takes the text as input. DistilBERT is a powerful language model that understands context and nuance.
4.  The model processes the text and outputs a prediction across 5 categories (representing 1 to 5 stars).
5.  The backend code identifies the category with the highest probability and translates it into a star rating (e.g., `[0.1, 0.1, 0.2, 0.8, 0.9]` -> 5 Stars).
6.  This rating is sent back to the frontend, which then updates the turf's overall score and review count.

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.