# storymanager
A Table-Top Role Playing Games Game Master Game Manager
For use in CS548: Designing Usable systems

## Getting Started
The following are running instructions for the application at its current initial state

### Prerequisites
The project requires Django/Anadconda3 to be installed prior to running. 

Visit the [Anaconda Installation Site](https://docs.continuum.io/anaconda/install) to install Anaconda3 which includes python and Django. 

### Running the application
In the home directory for the application (`USR_DIRS\\gmgm`), use `python manage.py runserver` to start the serverlet and then browse to
>localhost:8000
or 
>127.0.0.1:8000 
to open the application. 

## Intro
This application helps Table Top RPG Game Master manage their stories by providing a simple facility to manage a story flowchart as well as combat/interaction scenarios and keep a database of items and enemies to reuse in their story. 

### Definitions
- Story: The game the GM is running, each story lets you assign it a name and specify the source book it is based on. 
- Mission: Each session/day in the story gets its own mission, this lets you create a flowchart for the story and add Scenes to it
- Scene: Each combat/interaction scenario. It ightei
