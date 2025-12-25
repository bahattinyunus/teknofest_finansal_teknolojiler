# 🎯 Kubernetes Deployment Guide

## Prerequisites
- Kubernetes cluster (v1.24+)
- kubectl configured
- Secrets configured

## Quick Deploy

```bash
# Create namespace
kubectl create namespace fintech-prod

# Create secrets (replace with actual values)
kubectl create secret generic fintech-secrets \
  --from-literal=database-url='postgresql://user:pass@postgres:5432/findb' \
  -n fintech-prod

# Deploy
kubectl apply -f k8s-deployment.yaml

# Check status
kubectl get pods -n fintech-prod
kubectl get svc -n fintech-prod
```

## Architecture

```mermaid
graph TB
    LB[Load Balancer] --> SVC[fintech-api-service]
    SVC --> POD1[Pod 1]
    SVC --> POD2[Pod 2]
    SVC --> POD3[Pod 3]
    
    HPA[HorizontalPodAutoscaler] -.-> POD1
    HPA -.-> POD2
    HPA -.-> POD3
    
    POD1 --> DB[(PostgreSQL)]
    POD2 --> DB
    POD3 --> DB
    
    POD1 --> KAFKA[Kafka]
    POD2 --> KAFKA
    POD3 --> KAFKA
```

## Auto-Scaling
- **Min Replicas:** 3 (High Availability)
- **Max Replicas:** 10
- **Trigger:** CPU > 70%

## Health Checks
- **Liveness:** `/health` endpoint
- **Readiness:** `/ready` endpoint

## Security Notes
> [!CAUTION]
> - Never commit secrets to Git
> - Use Kubernetes Secrets or external secret managers (Vault, AWS Secrets Manager)
> - Enable Network Policies for pod-to-pod communication
