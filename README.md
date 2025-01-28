The Dune Infra Pair-Programming Exercise
========================================

In this session, we’ll work together to **debug, containerize, and refine** a small Python microservice. The goal is to see how you approach problems in real-time—from diagnosing errors to explaining your reasoning as you go.

What We Provide
---------------
- **`app.py`**: A microservice with a few bugs and potential security issues.
- **`Dockerfile`**: An early, incomplete attempt at containerizing the service.
- **`blockchain_or_not.sqlite`**: A small SQLite database used by `app.py`.
- **`test_integration_app.py`**: Our pytest suite to validate the service.

What We'll Do
-------------
1. **Live Debugging & Containerization**  
   - You’ll walk us through fixing the Dockerfile so that it builds and runs successfully.
   - We’ll discuss best practices (e.g., base image choice, security, port binding).
2. **Code Fixes**  
   - We’ll address issues in `app.py` (e.g., SQL injection, returning proper JSON).
   - We won’t replace SQLite or add major features; our focus is production-readiness for what’s already there.
3. **Testing**  
   - Once your fixes are in place, we’ll run the tests in `test_integration_app.py` and confirm everything passes.
4. **Kubernetes Debugging & Deployment**  
   - We’ve provided a `k8s/deployment.yaml` that contains a few intentional misconfigurations.
   - If time permits, you’ll debug and fix those issues so the microservice can run properly on a local Kubernetes cluster (e.g., Minikube).
5. **Discussion & Teaching Moments**  
   - We’ll ask you to explain your approach, share insights on containerization, and highlight improvements that could help a junior developer (Sam) learn and maintain this code.
6. **Optional Extensions**  
   - If time allows, we may explore quick wins for observability (health checks, logs) or how this might be deployed.


Let’s get started!
