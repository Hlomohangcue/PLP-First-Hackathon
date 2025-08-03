# My Personal Portfolio Website

This is a personal portfolio website developed as part of the **PLP Software Engineering Hackathon**. The website showcases my background, skills, projects, and interests, and provides a way for visitors to get in touch with me.

The site is built as a static website using only **HTML5** and **CSS3**, following the core requirements of the hackathon. It is deployed and hosted on **Vercel**.

## Project Details

### Requirements
The primary goal of this hackathon was to build a personal portfolio website that includes the following sections:
- **Background / About Me**: A brief introduction to myself and my professional journey.
- **Skills**: A list of my technical and soft skills.
- **Interests**: Hobbies and areas of personal interest.
- **Projects**: A showcase of key projects I have worked on, including details and links.
- **Contact**: A way for visitors to contact me.

The project was required to be developed using only **HTML** and **CSS** and deployed on **Vercel**.

### Key Features
- **Clean and Responsive Design**: The website is designed to be easily accessible and visually appealing on various devices, from desktops to mobile phones.
- **Static Website**: The entire site is built using static HTML and CSS files, ensuring fast load times and a simple, efficient architecture.
- **Project Showcase**: The projects section includes detailed descriptions, images, and video media to provide a comprehensive view of my work.
- **WhatsApp Contact Link**: The contact form has been updated to use a direct WhatsApp link, providing a simple and immediate way for visitors to connect with me. This approach was implemented to meet the hackathon's constraints and deployment requirements.

### Technologies Used
- **HTML5**: Used for structuring the content of the website.
- **CSS3**: Used for styling and creating the visual layout.
- **Vercel**: The platform used for deploying and hosting the static website.
- **Font Awesome**: Used for social media icons and other visual elements.

## Project Structure

The project follows a clean and logical file structure:

/
├── templates/
│   ├── index.html
│   ├── about.html
│   ├── skills.html
│   ├── education.html
│   ├── projects.html
│   ├── interests.html
│   ├── contact.html
│   └── ... (other HTML pages)
├── static/
│   ├── images/
│   │   └── ... (all image and video files)
│   ├── styles.css
│   └── ... (other static assets)
└── vercel.json


- **`templates/`**: This directory contains all the main HTML pages of the website.
- **`static/`**: This directory holds all the static assets, including images, videos, and the primary stylesheet (`styles.css`).
- **`vercel.json`**: This file configures Vercel to correctly route all requests to the static files within the `templates` and `static` directories, ensuring the website is served properly.

## Deployment

The website is deployed and hosted on Vercel. The deployment process is configured to build and serve the static files without a backend server, adhering to the project's requirements.

The `vercel.json` file handles the routing for all the HTML and static assets, allowing the website to function seamlessly on the Vercel platform.

## How to Run Locally

If you wish to run this project locally, you can simply open the `index.html` file in your web browser. Due to the project being a static website, no web server is required.

1.  Clone the repository.
2.  Navigate to the `templates` folder.
3.  Open `index.html` in your favorite web browser.

---
**Author**: Hlomohang Sethuntsa
