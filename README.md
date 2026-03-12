# 🍀 4chan analyzer

A web-based tool designed to fetch and analyze data from [4chan.org](https://4chan.org) threads using the official 4chan API. This application provides a dashboard for visualizing post frequency, common keywords, and media distribution.

## Features

* **Thread Data Extraction**: Fetches JSON data directly from 4chan boards for specific threads.
* **Text Analysis**: 
    * Sanitizes post content by removing HTML tags and special characters.
    * Identifies and counts the most frequently used keywords in the discussion.
* **Visual Dashboards**:
    * **Post Velocity**: Visualizes thread activity and post frequency over time.
    * **Media Breakdown**: Analyzes the distribution of image and video file types (JPG, PNG, WebM, etc.).
* **Sentiment Overview**: Provides a high-level summary of thread engagement and discussion content.

## Technical Stack

* **Backend**: Python with the **Flask** web framework.
* **Data Processing**:
    * `requests`: Handles API communication with 4chan.
    * `re`: Regular expressions for cleaning and parsing post data.
    * `collections.Counter`: Efficiently tallies word and media frequencies.
* **Frontend**:
    * **HTML5/CSS3**: Clean and responsive user interface.
    * **Chart.js**: Powers the analytical visualizations and graphs.

## Installation & Setup

1.  **Clone the repository**:
    ```bash
    git clone [https://github.com/drachmacollector/4chan-analyzer.git](https://github.com/drachmacollector/4chan-analyzer.git)
    cd 4chan-analyzer
    ```

2.  **Install dependencies**:
    Ensure you have Python installed, then run:
    ```bash
    pip install flask requests
    ```

3.  **Launch the application**:
    Run the Flask server:
    ```bash
    python app.py
    ```

4.  **Access the tool**:
    Navigate to `http://127.0.0.1:5000` in your web browser.

## Usage

1.  Select a **Board** (e.g., `v` for video games, `g` for technology).
2.  Enter a valid **Thread ID**.
3.  Click **Analyze** to generate the data visualizations and keyword statistics.

## Project Structure

* `app.py`: The Flask server handling routing and user requests.
* `analyzer.py`: The core logic for data fetching, text sanitization, and statistical processing.
* `index.html`: The frontend template for the dashboard and input forms.
