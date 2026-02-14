# Mashup Generator Application

**Roll Number: 102303599**

------------------------------------------------------------------------

## Project Overview

The Mashup Generator is a Python-based application designed to
automatically create an audio mashup using songs from YouTube. The
system accepts user input such as singer name, number of songs, and clip
duration, and produces a single merged audio file.

The project demonstrates backend development, media processing, modular
architecture, and web integration using modern tools and frameworks.

------------------------------------------------------------------------

## Objectives

The main objectives of this project include:

-   Automate retrieval of songs from YouTube
-   Process and extract audio segments
-   Combine multiple audio clips into one mashup
-   Provide both CLI and Web-based interfaces
-   Follow structured and modular development practices

------------------------------------------------------------------------

## System Architecture

``` mermaid
flowchart LR
    A[User Input] --> B[Flask Web Interface]
    B --> C[Mashup Engine]
    C --> D[YouTube Search]
    D --> E[Download Audio]
    E --> F[Convert Audio]
    F --> G[Extract Clips]
    G --> H[Merge Audio]
    H --> I[Generate Mashup File]
    I --> J[Return Output to User]
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

    User->>WebApp: Enter Singer, Count, Duration
    WebApp->>Downloader: Search videos
    Downloader->>Converter: Provide downloaded files
    Converter->>Cutter: Convert to MP3
    Cutter->>Merger: Provide trimmed clips
    Merger->>WebApp: Return mashup file
    WebApp->>User: Provide output
```

------------------------------------------------------------------------

## Module Structure

``` mermaid
graph TD
    A[Mashup System] --> B[Downloader Module]
    A --> C[Converter Module]
    A --> D[Cutter Module]
    A --> E[Merger Module]
    A --> F[Web Interface]

    B --> B1[YouTube Search]
    B --> B2[Download Files]

    C --> C1[Format Conversion]

    D --> D1[Clip Extraction]

    E --> E1[Audio Merging]

    F --> F1[Flask Application]
    F --> F2[Bootstrap UI]
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

------------------------------------------------------------------------

## Command Line Usage

The mashup can be generated using:

    python 102303599.py "Singer Name" 5 20 mashup.mp3

Example:

    python 102303599.py "Arijit Singh" 10 25 mashup.mp3

------------------------------------------------------------------------

## Web Application Usage

Steps:

1.  Run the Flask application

```{=html}
<!-- -->
```
    python webapp/app.py

2.  Open browser

```{=html}
<!-- -->
```
    http://127.0.0.1:5000

3.  Enter required details

4.  Generate mashup

------------------------------------------------------------------------

## Data Flow Diagram

``` mermaid
flowchart TD
    A[Input Parameters] --> B[Search Videos]
    B --> C[Download Audio]
    C --> D[Convert Format]
    D --> E[Trim Audio]
    E --> F[Merge Clips]
    F --> G[Output Mashup]
```

------------------------------------------------------------------------

## Key Features

-   Automated mashup creation
-   Modular architecture
-   Web-based user interface
-   Command-line support
-   Automated audio processing

------------------------------------------------------------------------

## Learning Outcomes

Through this project, the following concepts were explored:

-   Backend development using Flask
-   Media processing using Python
-   Modular software design
-   Web application integration
-   Handling real-world media data

------------------------------------------------------------------------

## Limitations

-   Processing time depends on internet speed
-   Depends on availability of YouTube content
-   Large files may take longer to process

------------------------------------------------------------------------

## Future Improvements

-   Progress tracking feature
-   Improved UI design
-   Cloud storage integration
-   Performance optimization

------------------------------------------------------------------------

## Conclusion

This project successfully demonstrates an automated mashup generation
system using Python and web technologies. It integrates media
processing, backend development, and web interface design into a
complete application.

------------------------------------------------------------------------

## Author

Roll Number: 102303599\
Mashup Generator Assignment
