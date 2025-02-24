# Persistent Queue System

## Overview
This project implements a **persistent producer-consumer queue** using SQLite.

## Problem Description
The system is designed to manage jobs submitted by producers and processed by consumers. It ensures that jobs are persistent, meaning they survive application restarts, and that no job is processed by multiple consumers simultaneously.

## System Design
The architecture consists of three main components:
- **Producers**: Submit jobs to the queue.
- **Consumers**: Process jobs from the queue.
- **Admin Console**: Manage job reprocessing and status.
- **Ops Console**: View job statuses and details.

The queue must support multiple producers and consumers, ensuring robustness against application crashes.

## Usage Instructions
To start the producer, consumer, and consoles, run the following commands:

```bash
poetry run python persistent_queue_system/producer.py
poetry run python persistent_queue_system/consumer.py
poetry run streamlit run persistent_queue_system/ops.py
```

### Diagrams
Use Mermaid diagrams to visualize the task flow and different states of the system.


## Features
- **Producers** submit jobs to the queue.
- **Consumers** process jobs.
- **Persistent Storage**: Jobs survive restarts.
- **Admin Console**: Manage job reprocessing.
- **Ops Console**: View job statuses.

## Installation
```bash
cd persistent_queue_system
poetry install

## Usage
Start the producer, consumer, and consoles:

poetry run python persistent_queue_system/producer.py
poetry run python persistent_queue_system/consumer.py
poetry run streamlit run persistent_queue_system/ops.py
