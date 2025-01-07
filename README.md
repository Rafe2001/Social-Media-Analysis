# Social Media Performance Analysis

A simple and effective analytics tool developed for the **Level Supermind Hackathon Pre-Hackathon Assignment**. This tool uses **Langflow**, **DataStax Astra DB**, and **Groq** to analyze engagement metrics from mock social media accounts and generate actionable insights. The application leverages Flask for the backend and integrates Chart.js for data visualization.

![image](https://github.com/user-attachments/assets/f3eea6a0-c48b-4d41-90d6-d304211b6e6b)


---

## **Hackathon Details**
- **Assignment:** Pre-Hackathon Social Media Performance Analysis
- **Deadline:** January 8th, 2025
- **Hackathon Link:** [Level Supermind Hackathon - Social Media Analysis](#)

---

## **Features**

1. **Data Simulation and Storage**  
   - Mock datasets simulate engagement metrics (likes, shares, comments) for various post types (carousel, reels, static images).  
   - Data is stored and queried efficiently using **DataStax Astra DB**.

2. **Post Performance Analysis**  
   - Uses Langflow to calculate and compare average engagement for different post types.  
   - The insights provide detailed engagement trends.

3. **AI-Powered Insights**  
   - Integrated with **Groq** through Langflow to deliver meaningful insights, such as:
     - *"Carousel posts have 20% higher engagement than static posts."*
     - *"Reels generate twice as many comments as other post types."*

4. **Conversational Interface**  
   - Includes a chatbot interface to answer user queries related to the data.

---

## **Tech Stack**

- **Backend:** Python, Flask  
- **Database:** DataStax Astra DB  
- **AI Workflow:** Langflow  
- **Insights Engine:** Groq  
- **Environment Management:** dotenv  
- **Frontend:** HTML, CSS, JavaScript  

---

## **Setup Instructions**

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/Rafe2001/Social-Media-Analysis.git
   cd Social-Media-Analysis
   ```

2. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**  
   - Create a `.env` file in the root directory with the following variables:
     ```plaintext
     LANGFLOW_ID=your-langflow-id
     FLOW_ID=your-flow-id
     APPLICATION_TOKEN=your-application-token
     ```

4. **Configure DataStax Astra DB**  
   - Create an account at [DataStax Astra](https://www.datastax.com/).
   - Set up a new database and download the secure connect bundle.
   - Update database credentials in your project configuration.

5. **Run the Application**  
   ```bash
   flask run
   ```
   Access the app at: [http://localhost:5000](http://localhost:5000)

---

## **How to Use**

1. **View Engagement Data**  
   - Navigate to the homepage to see charts displaying likes, shares, and comments for different post types.

2. **Ask Questions**  
   - Use the chatbot interface to analyze post performance or query engagement insights.

3. **Interactive Insights**  
   - Insights are generated dynamically based on engagement metrics, guiding decision-making.

---

## **File Structure**

```plaintext
Social-Media-Analysis/
├── templates/           # HTML files for the frontend
├── .env                 # Environment variables (ignored by Git)
├── .gitignore           # Git ignored files
├── app.py               # Flask application backend
├── data_generate.py     # Script to generate mock data
├── data_generated.csv   # Generated mock data file
├── main.py              # Main workflow integration script
├── requirements.txt     # Python dependencies
```

---

## **Demo Video**

Youtube Video Link: [https://www.youtube.com/watch?v=G_YYlxymV04]

In this video, you’ll see:
- Langflow integration for workflows.
- How DataStax Astra DB stores and queries data.
- Groq-powered insights generation.

---

## **Contributing**

Contributions are welcome! Feel free to fork this repository, make changes, and submit a pull request.

---

## **License**

This project is licensed under the MIT License. See the `LICENSE` file for more details.
