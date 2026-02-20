# Python Pomodoro Timer

A desktop application that implements the Pomodoro Technique, a time management method that uses a timer to break work into focused intervals separated by short breaks.

## Features

- **Work Sessions**: 1-minute focused work periods (customizable)
- **Short Breaks**: 1-minute breaks between work sessions (customizable)
- **Long Breaks**: 20-minute breaks after every 4 work sessions (customizable)
- **Visual Feedback**: 
  - Tomato icon displayed during timer
  - Color-coded timer status (pink for work, green for breaks, red for long breaks)
  - Checkmarks (✔) displayed for each completed work session
- **Start/Reset Controls**: Easy-to-use buttons to start and reset the timer
- **Always-on-Top**: Window automatically comes to focus when timer starts
- **Intuitive UI**: Clean, minimalist interface with clear timer display

## Requirements

- Python 3.x
- Tkinter (usually included with Python)

## Installation

1. Clone or download this project
2. Ensure `tomato.png` is in the same directory as `main.py`
3. No additional dependencies required

## Usage

1. Run the application:
   ```bash
   python main.py
   ```

2. Use the **Start** button to begin a work session
   - The timer will cycle automatically through work sessions and breaks
   - After each work session, a checkmark appears to track progress
   
3. Use the **Reset** button to stop the timer and clear the session count

## How It Works

The Pomodoro cycle follows this pattern:
- **Session 1**: 1 minute work
- **Session 2**: 1 minute short break
- **Session 3**: 1 minute work
- **Session 4**: 1 minute short break
- ... (repeats)
- **Session 8**: 1 minute work
- **Session 9**: 20 minute long break (then cycle restarts)

Each completed work session is marked with a checkmark (✔).

## Customization

You can modify the timer durations by editing the constants at the top of `main.py`:

```python
WORK_MIN = 1              # Work session duration in minutes
SHORT_BREAK_MIN = 1       # Short break duration in minutes
LONG_BREAK_MIN = 20       # Long break duration in minutes
```

For a real Pomodoro experience, use:
- `WORK_MIN = 25`
- `SHORT_BREAK_MIN = 5`
- `LONG_BREAK_MIN = 15`

## Color Legend

- **Pink** (#e2979c): Work session active
- **Green** (#9bdeac): Short break active
- **Red** (#e7305b): Long break active
- **Yellow** (#f7f5dd): Background color

## Files

- `main.py` - Main application code
- `tomato.png` - Tomato icon displayed in the timer (required)

## Demo
![alt text](demo/pomodoro1.png)

![alt text](demo/pomodoro2.png)
