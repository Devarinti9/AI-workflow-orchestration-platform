# Project Overview

## Project name
AI Workflow Orchestration Platform

## Purpose
This project demonstrates a backend workflow system that:
- ingests data from an external HTTP source
- processes the ingested data through a small orchestration flow
- stores raw and processed outputs in a relational database
- exposes the workflow through REST endpoints

## What problem it solves
Many backend systems need a lightweight orchestration layer to fetch data, run deterministic processing steps, and store results for later review. This project shows that pattern in a compact and interview-friendly form.

## Core capabilities
- External API ingestion using `requests`
- REST API built with FastAPI
- Database persistence through SQLAlchemy
- Workflow execution using LangGraph
- Record retrieval and simple orchestration replay

## Processing behavior
For each ingested item, the project currently:
1. reads the `title` field from the source payload
2. generates a short summary
3. counts the number of words in the title
4. classifies the record into one of the following buckets:
   - `incident`
   - `user-data`
   - `finance`
   - `general`

## Primary technology stack
- Python
- FastAPI
- SQLAlchemy
- LangGraph
- SQLite (default in current implementation)
- Docker
- Airflow starter DAG

## Intended use
This repository is best used as:
- a portfolio project
- a backend API demo
- a starting point for a larger orchestration system

It is not positioned as production-ready without further hardening, observability, authentication, and deployment work.
