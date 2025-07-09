# AutoTyper

A Python tool for simulating human-like typing with customizable speed and behavior. Perfect for automating text input, demonstrations, or testing applications that require keyboard input.

## Features

- **Human-like typing simulation** with random delays between keystrokes
- **Multiple trigger methods**: delay-based or hotkey-based activation
- **Configurable typing speed** from instant to slow human-like pace
- **Flexible newline handling**: Choose between Enter or Alt+Enter for line breaks
- **File input support** for typing longer texts
- **Thread-safe operation** with graceful shutdown
- **Cross-platform compatibility** (Windows, macOS, Linux)

## Installation

1. **Clone or download** this repository
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Dependencies

- `pyautogui==0.9.54` - For keyboard simulation
- `keyboard==0.13.5` - For hotkey detection and advanced keyboard control

## Usage

### Basic Usage

**Type text after a delay:**
```bash
python autotyper.py -t "Hello, World!" -d 5
```

**Type text from a file:**
```bash
python autotyper.py -f message.txt -d 3
```

**Type text when hotkey is pressed:**
```bash
python autotyper.py -t "Triggered by hotkey" -k "ctrl+shift+t"
```

### Speed Control

**Default speed (fast human-like):**
```bash
python autotyper.py -t "Normal typing speed" -d 5
```

**Super fast typing:**
```bash
python autotyper.py -t "Super fast typing" --min-delay 0.01 --max-delay 0.02
```

**Slow, deliberate typing:**
```bash
python autotyper.py -t "Slow typing" --min-delay 0.1 --max-delay 0.3 -d 5
```

### Newline Behavior

**Default (Alt+Enter for newlines):**
```bash
python autotyper.py -t "Line 1\nLine 2\nLine 3" -d 5
```

**Use regular Enter for newlines:**
```bash
python autotyper.py -t "Line 1\nLine 2\nLine 3" -d 5 --use-enter
```

## Command Line Options

### Required Arguments (choose one)

| Option | Description |
|--------|-------------|
| `-t TEXT, --text TEXT` | Text to type directly |
| `-f FILE, --file FILE` | File containing text to type |

### Required Trigger (choose one)

| Option | Description |
|--------|-------------|
| `-d DELAY, --delay DELAY` | Delay in seconds before typing starts |
| `-k HOTKEY, --hotkey HOTKEY` | Hotkey to trigger typing (e.g., "ctrl+shift+t") |

### Optional Arguments

| Option | Default | Description |
|--------|---------|-------------|
| `--min-delay FLOAT` | 0.02 | Minimum delay between keystrokes (seconds) |
| `--max-delay FLOAT` | 0.05 | Maximum delay between keystrokes (seconds) |
| `--use-enter` | False | Use Enter instead of Alt+Enter for newlines |

## Examples

### Basic Examples

```bash
# Type a message after 3 seconds
python autotyper.py -t "Hello from AutoTyper!" -d 3

# Type content from a file after 5 seconds
python autotyper.py -f my_message.txt -d 5

# Wait for Ctrl+Shift+T hotkey to start typing
python autotyper.py -t "Hotkey activated!" -k "ctrl+shift+t"
```

### Advanced Examples

```bash
# Very fast typing (good for demos)
python autotyper.py -t "Lightning fast!" --min-delay 0.005 --max-delay 0.015 -d 2

# Slow, thoughtful typing
python autotyper.py -t "Thinking while typing..." --min-delay 0.2 --max-delay 0.5 -d 3

# Multi-line text with regular Enter
python autotyper.py -t "Line 1\nLine 2\nLine 3" -d 5 --use-enter

# Type code with Alt+Enter (good for chat applications)
python autotyper.py -t "print('Hello')\nprint('World')" -d 5
```

### File Input Example

Create a text file called `message.txt`:
```
This is a longer message
that spans multiple lines
and will be typed automatically!
```

Then run:
```bash
python autotyper.py -f message.txt -d 5
```

## Use Cases

- **Demonstrations**: Show typing in presentations or tutorials
- **Testing**: Test applications that require keyboard input
- **Automation**: Automate repetitive text entry tasks
- **Chat Applications**: Type messages with proper newline handling
- **Code Examples**: Simulate live coding demonstrations

## Hotkey Examples

Common hotkey combinations:
- `ctrl+shift+t` - Custom trigger
- `alt+space` - Alt + Space
- `ctrl+alt+a` - Ctrl + Alt + A
- `f1` - Function key
- `shift+enter` - Shift + Enter

## Safety Features

- **Graceful shutdown**: Press Ctrl+C to stop at any time
- **Thread-safe**: Safe to use with hotkeys and interruptions
- **ESC key support**: In hotkey mode, press ESC to exit
- **Fail-safe disabled**: Won't stop when mouse moves to screen corners

## Troubleshooting

### Common Issues

**"Module not found" errors:**
```bash
pip install -r requirements.txt
```

**Permissions issues on Linux/macOS:**
- May need to run with `sudo` on some systems
- Check if accessibility permissions are granted

**Hotkeys not working:**
- Ensure the hotkey combination is not used by other applications
- Try simpler combinations like `f1` or `ctrl+alt+a`

### Performance Tips

- For fastest typing, use `--min-delay 0 --max-delay 0.001`
- For most realistic human typing, use default settings
- For presentations, use `--min-delay 0.05 --max-delay 0.1`

## Technical Details

- **Character-by-character typing**: Each character is typed individually with random delays
- **Configurable delays**: Random delays between min and max values for natural variation
- **Newline handling**: Supports both Enter and Alt+Enter for different applications
- **Thread safety**: Uses threading.Event for clean shutdown in hotkey mode
- **Cross-platform**: Works on Windows, macOS, and Linux

## License

This project is open source. Feel free to modify and distribute as needed.

## Contributing

Feel free to submit issues, suggestions, or pull requests to improve AutoTyper!