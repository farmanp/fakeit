# Faker Data Generation API

## Overview

This project is a Python-based API for generating fake data using **FastAPI** and **Faker**. The API provides endpoints to generate single or batch records of fake data, as well as WebSocket support for streaming events. This tool is perfect for testing, mocking data, or learning purposes, and can generate data such as names, emails, addresses, and more.

**Note:** This project is strictly intended for **simulation and testing purposes** only. It should not be used for fraudulent activities or any form of malicious use.

### Key Features:
- REST API endpoints for generating single or multiple records of fake data.
- WebSocket endpoint for streaming fake events.
- Supports schema definitions in both YAML and JSON formats.

## File Structure

```
.
├── api.py                # Contains REST API endpoints
├── websocket.py          # Contains WebSocket streaming functionality
├── faker_data_generator.py  # Utility functions for schema loading and data generation
├── app.py                # Entry point for FastAPI including both REST and WebSocket routes
├── requirements.txt      # Python dependencies for the project
├── schema.json           # Example JSON schema file
├── schema.yaml           # Example YAML schema file
└── README.md             # This README file
```

## Getting Started

### Prerequisites

To run this project, you need to have **Python 3.7+** installed. Additionally, install the required dependencies listed in the `requirements.txt` file.

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/faker-data-generation-api.git
   cd faker-data-generation-api
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Server**:
   - To run the FastAPI server, execute:
   ```bash
   uvicorn app:app --reload
   ```
   The API will be available at `http://127.0.0.1:8000/`.

## Usage

### REST API Endpoints

1. **Generate Single Record**
   - **Endpoint**: `/generate-single`
   - **Method**: `POST`
   - **Body** (example):
     ```json
     {
       "fields": [
         {"name": "name"},
         {"email": "email"},
         {"address": {
           "street": "street_address",
           "city": "city",
           "state": "state",
           "zipcode": "postcode"
         }}
       ]
     }
     ```
   - **Response**: Returns a single record based on the provided schema.

2. **Generate Batch Records**
   - **Endpoint**: `/generate-batch`
   - **Method**: `POST`
   - **Body** (same as `/generate-single`)
   - **Query Parameter**: `num_records` (Optional)
   - **Response**: Returns multiple records of fake data.

3. **Generate Data from File**
   - **Endpoint**: `/generate-from-file`
   - **Method**: `POST`
   - **Form Data**: Upload a YAML or JSON file containing the schema.
   - **Response**: Returns generated fake data based on the uploaded schema.

### WebSocket Endpoint

1. **Streaming Fake Events**
   - **Endpoint**: `/ws/fake-events`
   - **Description**: Connect to this endpoint via WebSocket to receive continuous fake event data, such as names, emails, and addresses, at a configurable interval.

### Example Usage

#### Using Python WebSocket Client
To test the WebSocket endpoint, you can use the following Python script:

```python
import asyncio
import websockets

async def test_websocket():
    uri = "ws://localhost:8000/ws/fake-events"
    async with websockets.connect(uri) as websocket:
        while True:
            message = await websocket.recv()
            print(f"Received: {message}")

asyncio.run(test_websocket())
```

## Schema Examples

### YAML Schema (`schema.yaml`)
```yaml
fields:
  - name: name
  - email: email
  - address:
      street: street_address
      city: city
      state: state
      zipcode: postcode
```

### JSON Schema (`schema.json`)
```json
{
  "fields": [
    { "name": "name" },
    { "email": "email" },
    { "address": {
        "street": "street_address",
        "city": "city",
        "state": "state",
        "zipcode": "postcode"
      }
    }
  ]
}
```

## Development

If you want to modify the project or add new features, consider using a virtual environment to manage your dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

## Contributing

If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any questions or suggestions, please open an issue or reach out to me at [farman.pirz@gmail.com].
