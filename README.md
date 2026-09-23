---
layout: default
---

## $ whoami

Welcome to my cybersecurity portfolio.

This site documents my hands-on journey toward becoming a **Security Engineer**. It's a collection of projects, labs, scripts, and documentation that showcase my experience building, securing, monitoring, and troubleshooting real-world environments.

I bring 8 years of experience as a Navy avionics technician — quality assurance, COMSEC management, troubleshooting complex systems, and leading teams — and I'm applying that same discipline to security.

Rather than focusing solely on certifications, I'm developing practical skills through hands-on learning. Each project is an opportunity to better understand the technologies, tools, and concepts used in modern cybersecurity.

> **My goal is simple:** continuously learn, build, document, and improve.

## 🧰 What You'll Find Here
- SIEM platforms & threat detection
- Active Directory
- Windows & Linux administration
- Python automation
- Networking
- Endpoint monitoring

## 🛠 Projects
- 

## 📜 Certifications
- ✅ CompTIA Security+

## 📝 Latest Posts
{% for post in site.posts %}
- **{{ post.date | date: "%b %d, %Y" }}** — [{{ post.title }}]({{ post.url | relative_url }})
{% endfor %}
