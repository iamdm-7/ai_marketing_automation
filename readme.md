
# **AI Marketing Automation System**

An intelligent marketing automation system designed to analyze campaign performance, optimize decisions, and provide actionable insights using AI and data-driven rules.

- Daksh Malhotra
---

## **Features**
- **Automated Campaign Management**:  
  - Pauses underperforming campaigns.
  - Increases or decreases budgets based on key metrics like ROAS, CTR, and conversions.
- **AI-Driven Insights**:  
  - Leverages predefined rules to optimize campaigns.
  - Generates actionable recommendations for improving ad creatives and targeting.
- **Streamlit Dashboard**:  
  - Visualizes campaign performance through interactive graphs and reports.
- **Scalable Pipeline**:  
  - Handles multiple campaigns efficiently using batch processing.

---

## **Setup Instructions**

### **1. Prerequisites**
- Python 3.8 or higher
- Streamlit
- Required Python packages (listed in `requirements.txt`)

### **2. Installation**
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/ai-marketing-automation.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ai-marketing-automation
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### **3. Run the Dashboard**
Start the Streamlit app:
```bash
streamlit run dashboard/app.py
```
Access the dashboard at [http://localhost:8501](http://localhost:8501).

---

## **How It Works**
1. **Data Preprocessing**:  
   Campaign data is loaded from a CSV file and cleaned for analysis.
2. **Analysis Engine**:  
   Key performance metrics like CTR, ROAS, and CPA are calculated.
3. **Decision Agent**:  
   Implements rules for pausing, increasing, or decreasing budgets.
4. **Reporting**:  
   Daily summaries and insights are generated for review.
5. **Visualization**:  
   Interactive graphs display campaign trends and performance metrics.

---

## **Sample Use Case**
1. Input:
   - A CSV file containing 10 active campaigns with varying performance data.
2. Actions:
   - Pauses 2 campaigns due to low CTR.
   - Increases the budget for 3 campaigns with high ROAS.
   - Decreases the budget for 1 campaign due to poor performance.
3. Output:
   - Updated campaign statuses and budgets.
   - A report summarizing actions taken and reasons.

---

## **Developer**
**Daksh Malhotra**  
- **Portfolio**: [dakshmalhotra.xyz](https://www.dakshmalhotra.xyz)  
- **Resume**: [View Resume](https://www.dakshmalhotra.xyz/resume.html)  

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

 - Let me know if you’d like to make any changes!
---
 

**Screenshot of Deployment:**
https://drive.google.com/file/d/1aOgXlSI2G0h2FWJd0xbvZjUP1NHugdkq/view?usp=sharing
