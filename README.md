# Memory and CPU Tester App

This is a simple Flask application designed to test memory and CPU consumption in a Kubernetes environment. It provides endpoints to dynamically increase or decrease memory and CPU usage on demand.

## Features

- Increase/decrease memory consumption by allocating/deallocating large data structures
- Increase/decrease CPU consumption by starting/stopping background computation threads
- Automatic random adjustments every 6 hours to simulate varying load

## Endpoints

- `GET /` : Returns a status message with current memory load and CPU status
- `GET /increase_memory` : Increases memory usage by allocating ~4MB of data
- `GET /decrease_memory` : Decreases memory usage by deallocating the last allocated block
- `GET /increase_cpu` : Starts a background thread performing CPU-intensive calculations
- `GET /decrease_cpu` : Stops the CPU-intensive background thread

## Running Locally

1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `python app.py`
3. Access at http://localhost:5000

## Docker

Build the image: `docker build -t cremerfc/cost-opt-app .`

Run locally: `docker run -p 5000:5000 cremerfc/cost-opt-app`

## CI/CD

The project includes a GitHub Action that automatically builds and pushes the Docker image to Docker Hub (`cremerfc/cost-opt-app:latest`) on pushes to the main branch.

To set up:
1. Set the following secrets in your GitHub repository:
   - `DOCKERHUB_USERNAME`: Your Docker Hub username
   - `DOCKERHUB_TOKEN`: Your Docker Hub access token (create one at https://hub.docker.com/settings/security)
2. Push to the main branch to trigger the build.

## Kubernetes Deployment

1. Ensure the Docker image is built and pushed (via GitHub Action or manually)
2. Apply the manifests: `kubectl apply -f k8s/`
3. Access the service via the LoadBalancer IP on port 80

## Notes

- Memory increases are in ~4MB increments
- CPU load uses a simple summation loop; adjust the range for more/less intensity
- Automatic adjustments occur every 6 hours, randomly increasing or decreasing memory or CPU
- This is for testing purposes only; not optimized for production