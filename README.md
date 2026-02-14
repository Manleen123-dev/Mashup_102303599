# Mashup Generator Application

**Roll Number: 102303599**

------------------------------------------------------------------------

## Project Overview

The Mashup Generator is a Python-based web application that
automatically creates an audio mashup from songs retrieved from YouTube.
Users provide input such as singer name, number of songs, and clip
duration, and the system downloads, processes, and merges audio clips
into a single mashup file.

This project demonstrates backend development, media processing, modular
software architecture, and cloud deployment.

------------------------------------------------------------------------

## System Architecture

``` mermaid
flowchart LR
    A[User] --> B[Web Browser]
    B --> C[Flask Web Application]
    C --> D[Mashup Processing Engine]
    D --> E[Download Audio yt-dlp]
    E --> F[Convert Audio ffmpeg]
    F --> G[Trim Clips pydub]
    G --> H[Merge Audio]
    H --> I[Generate Mashup]
    I --> J[Return to User]
```

------------------------------------------------------------------------

## Processing Workflow

``` mermaid
sequenceDiagram
    participant User
    participant WebApp
    participant Downloader
    participant Converter
    participant Cutter
    participant Merger

    User->>WebApp: Input singer and parameters
    WebApp->>Downloader: Fetch videos
    Downloader->>Converter: Provide audio
    Converter->>Cutter: Convert format
    Cutter->>Merger: Send clips
    Merger->>WebApp: Return mashup
    WebApp->>User: Provide output
```

------------------------------------------------------------------------

## Deployment

The application is deployed using Render cloud platform and can be
accessed through the following link:

**Deployment URL:**\
https://mashup-generator-102303599.onrender.com

This deployment allows users to access the mashup generator through a
web interface without installing any software locally.

------------------------------------------------------------------------

## Deployment Architecture

``` mermaid
flowchart TD
    A[Developer] --> B[GitHub Repository]
    B --> C[Render Cloud Platform]
    C --> D[Web Service]
    D --> E[Public Deployment URL]
    E --> F[End Users Access Application]
```

------------------------------------------------------------------------

## Project Structure

    Mashup_Assignment/
    │
    ├── webapp/
    │   ├── app.py
    │   ├── templates/
    │   └── static/
    │
    ├── src/
    │   ├── mashup.py
    │   ├── downloader.py
    │   ├── converter.py
    │   ├── cutter.py
    │   └── merger.py
    │
    ├── data/
    ├── requirements.txt
    ├── README.md

------------------------------------------------------------------------

## Technologies Used

### Backend

-   Python
-   Flask
-   yt-dlp
-   pydub
-   ffmpeg

### Frontend

-   HTML
-   Bootstrap
-   CSS

### Deployment

-   Render Cloud Platform
-   GitHub

------------------------------------------------------------------------

## Command Line Usage

    python 102303599.py "Singer Name" 5 20 mashup.mp3

Example:

    python 102303599.py "Arijit Singh" 10 25 mashup.mp3

------------------------------------------------------------------------

## Web Application Usage

Steps:

1.  Open the deployment link in a browser:

```{=html}
<!-- -->
```
    https://mashup-generator-102303599.onrender.com

2.  Enter required details

3.  Generate mashup

4.  Download output file

------------------------------------------------------------------------

## Data Flow Diagram

``` mermaid
flowchart TD
    A[User Input] --> B[Search Videos]
    B --> C[Download Audio]
    C --> D[Convert Audio]
    D --> E[Trim Clips]
    E --> F[Merge Audio]
    F --> G[Output Mashup]
```

------------------------------------------------------------------------

## Key Features

-   Automated mashup generation
-   Web-based interface
-   Modular architecture
-   Cloud deployment
-   Automated audio processing

------------------------------------------------------------------------

## Learning Outcomes

-   Backend development using Flask
-   Media processing using Python
-   Web application deployment
-   Modular software architecture
-   Cloud deployment using Render

------------------------------------------------------------------------

## Conclusion

This project successfully implements an automated mashup generator and
demonstrates integration of backend development, media processing, and
cloud deployment technologies.

------------------------------------------------------------------------

## Author

Roll Number: 102303599\
Mashup Generator Assignment
