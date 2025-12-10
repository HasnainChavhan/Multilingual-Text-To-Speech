# 🔊 Kira29.1 – Multilingual Neural Text-to-Speech System

<p align="center">
  <img src="https://img.shields.io/badge/Version-Kira29.1-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Python-3.8%2B-yellow?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Streamlit-Enabled-FF4B4B?style=for-the-badge&logo=streamlit" />
  <img src="https://img.shields.io/badge/EdgeTTS-Microsoft_Azure-0078D4?style=for-the-badge&logo=microsoft" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Production_Ready-brightgreen?style=for-the-badge" />
</p>

---

## 📌 Overview

**Kira29.1** is a powerful, multilingual neural **Text-to-Speech (TTS)** system developed using  
**Streamlit + Microsoft Edge Neural Voices**.

It converts text into natural-sounding speech in:

- 🇮🇳 Marathi  
- 🇮🇳 Hindi  
- 🇮🇳 Bengali  
- 🇮🇳 Tamil  

Supports **Male/Female voices**, instant audio playback, and downloadable MP3 output.

---

## ✨ Features

### 🎙 Neural Voice Output
Powered by Microsoft Edge Neural TTS  
High-quality, human-like voice synthesis.

### 🌐 Multilingual Support
Choose from 4 Indian languages  
Each with male & female voices.

### ⚡ Fast Audio Generation
Async implementation for fast processing.

### 🔊 Live Playback
Hear the generated MP3 file instantly.

### ⬇ Download Option
Save the audio file with one click.

### 🎨 Clean UI
Streamlit-based minimal & responsive design.

---

## 🧩 System Architecture

```mermaid
flowchart TD

A[User Input - Streamlit UI] --> B[Language and Voice Selection]
B --> C[Async TTS Engine - Edge TTS]
C --> D[Generate MP3 File using Tempfile]
D --> E[Play Audio using st audio]
D --> F[Download MP3 File]

A -->|Validation| G[Error Handling and Warnings]

classDef main fill:#4B9CD3,stroke:#036,stroke-width:2px,color:white;
classDef process fill:#50C878,stroke:#063,stroke-width:2px,color:white;
classDef output fill:#FFB347,stroke:#A65,stroke-width:2px,color:white;

class A,B main;
class C process;
class D,E,F output;




