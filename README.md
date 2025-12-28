🟦 WEEK 0 (Optional but Strongly Recommended)
Linux, Networking & Git Foundations
Learn

Linux internals

Process lifecycle (ps, top, htop)

Memory (free, /proc, OOM)

Signals (SIGTERM, SIGKILL)

Bash scripting

Variables, loops, functions

Cron jobs

Networking basics

DNS resolution

TCP vs UDP

HTTP vs HTTPS

SSH, ports, NAT

Git advanced

rebase, cherry-pick

tags

PR workflow

Hands-on

Bash automation:

Log rotation

Compression

Simulated backup (local folder)

Deliverables (inside repo)
week-0-linux-networking-git/
 ├── backup.sh
 ├── cron-example.txt
 └── README.md


🟦 WEEK 1 – Docker Basics & App Lifecycle
Learn

Docker architecture

Images vs containers

Dockerfile basics

Port mapping & volumes

Hands-on

Create Python Flask app

Write Dockerfile

Build & run locally

Deliverables
week-1-docker-basics/
 ├── app/
 ├── Dockerfile
 └── README.md



 🟦 WEEK 2 – Advanced Docker & Security ddddd
Learn

Multi-stage Dockerfiles

Image size optimization

Docker security basics

Hands-on

Java Spring Boot app

Multi-stage Dockerfile

Scan image using Trivy

Deliverables
week-2-docker-advanced/
 ├── Dockerfile.multi
 ├── trivy-scan.txt
 └── README.md



 🟦 WEEK 4 – Kubernetes Core (Local)
Learn

Pods, Deployments, Services

Namespaces

Labels & selectors

Hands-on

Create 2-node kind cluster

Deploy app in dev namespace

Deliverables
week-4-kubernetes-core/
 ├── kind-config.yaml
 ├── deployment.yaml
 └── README.md



 🟦 WEEK 5 – Kubernetes Config & Scaling
Learn

ConfigMaps & Secrets

Liveness & Readiness probes

HPA basics

Hands-on

Add health checks

Enable HPA

Simulate CPU load

Deliverables
week-5-k8s-scaling/
 ├── configmap.yaml
 ├── hpa.yaml
 └── README.md


 🟦 WEEK 6 – Kubernetes Deployment Strategies
Learn

Rolling updates

Blue-Green deployment

Canary concepts

Hands-on

Deploy app in:

dev

staging

prod namespaces

Blue-Green simulation

Deliverables
week-6-k8s-deploy-strategies/
 ├── blue.yaml
 ├── green.yaml
 └── README.md










 🟦 WEEK 7 – Monitoring with Prometheus & Grafana
Learn

Prometheus architecture

Metrics vs logs

JVM metrics

Hands-on

Install Prometheus & Grafana (local)

JVM memory dashboard

Pod restart alerts

Deliverables
week-7-monitoring/
 ├── prometheus-values.yaml
 ├── alerts.yaml
 └── README.md





 🟦 WEEK 8 – Logging with Loki & Alertmanager
Learn

Centralized logging

Log labels & queries

Alert routing

Hands-on

Loki + Promtail

Log-based alerts

Alertmanager config

Deliverables
week-8-logging/
 ├── loki.yaml
 ├── alertmanager.yaml
 └── README.md







 🟦 WEEK 9 – Terraform & IaC
Learn

Terraform basics

Providers & state

Modules & variables

Hands-on

Create:

VPC

EC2

Minimal EKS (optional)

Deliverables
week-9-terraform/
 ├── main.tf
 ├── variables.tf
 └── README.md







 🟦 WEEK 10 – AWS Secure Infrastructure
Learn

IAM least privilege

Security Groups

S3 lifecycle

CloudWatch basics

Hands-on

Secure EC2

Enable logging

Cost-optimized setup

Deliverables
week-10-aws-security/
 ├── iam-policy.json
 ├── s3-lifecycle.json
 └── README.md








 🟦 WEEK 11 – Databases & Reliability
Learn

PostgreSQL basics

DynamoDB concepts

Redis caching

Hands-on

Backup automation

Slow query monitoring

Failure simulation

Deliverables
week-11-database-ops/
 ├── backup-script.sh
 ├── monitoring-notes.md
 └── README.md










 🟦 WEEK 13–14 – LLM + DevOps (🔥 Differentiator)
Learn

Using LLMs via API

Prompt engineering

Log summarization

Hands-on

Python tool:

Log summarization

Alert RCA explanation

LangChain integration

Deliverables
week-13-llm-devops/
 ├── log_analyzer.py
 ├── prompts.md
 └── README.md