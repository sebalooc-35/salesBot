 # SalesBot 🛠️📊

 **SalesBot** is a lightweight backend solution designed to automate the processing of project availability data from PDF files. With SalesBot, you can upload PDF files containing project details, parse them into SQL queries using AI, and seamlessly integrate the data into your database for efficient management.

 ---

 ## Features 🚀
 - **File Upload**: Upload PDF files containing project data via a simple API endpoint.
 - **AI-Powered Parsing**: Leverages OpenAI's GPT-4 model to extract and transform project data into SQL-ready queries.
 - **Database Integration**: Directly use the generated SQL queries with your database using tools like JDBC.
 - **Containerized Setup**: Fully Dockerized for easy deployment and scalability.
 - **Environment Ready**: Supports secure configuration through environment variables.

 ---

 ## Getting Started 💻

 ### Prerequisites
 - Docker and Docker Compose installed on your machine.
 - OpenAI API key for accessing GPT-4.

 ---

 ### Installation

 1. **Clone the Repository**:
    ```bash
    git clone <your-repo-url>
    cd salesBot
    ```

 2. **Set Your OpenAI API Key**:
    - Add your OpenAI API key to the `docker-compose.yml` file or use a `.env` file.

 3. **Build and Run**:
    ```bash
    docker-compose up --build
    ```

 4. **Access the API**:
    The backend will be available at `http://127.0.0.1:8000`.

 ---

 ### API Endpoints
 #### **POST /upload**
 Upload a PDF file to extract and generate SQL queries.

 **Request**:
 - File: PDF file with project data.

 **Response**:
 - JSON containing the generated SQL queries.

 Example:
 ```bash
 curl -X POST "http://127.0.0.1:8000/upload" -F "file=@example.pdf"
 ```

 ---

 ## Technologies Used 🛠️
 - **Backend Framework**: [FastAPI](https://fastapi.tiangolo.com/)
 - **AI Integration**: [OpenAI GPT-4](https://platform.openai.com/)
 - **Containerization**: [Docker](https://www.docker.com/)
 - **Dependency Management**: `pip`

 ---

 ## Project Structure 📁
 ```
 salesBot/
 ├── app/
 │   ├── main.py          # Backend code
 │   ├── requirements.txt # Dependencies
 ├── Dockerfile           # Docker image configuration
 ├── docker-compose.yml   # Container orchestration
 ```

 ---

 ## Future Enhancements 🌟
 - Integration with a database schema for seamless data management.
 - User authentication for secure file uploads.
 - Frontend for an intuitive user interface.
 - Persistent chatbot for real-time project data queries and updates.

 ---

 ## Contribution 🤝
 Feel free to fork the project, submit issues, or contribute with pull requests. Your feedback and contributions are always welcome!

 ---

 ## License 📜
 This project is licensed under the [MIT License](LICENSE).

