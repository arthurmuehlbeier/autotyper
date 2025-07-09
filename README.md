# AutoTyper 🤖⌨️

> A powerful Python tool for simulating human-like typing with customizable speed and behavior

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](https://github.com)

AutoTyper is a versatile desktop automation tool that simulates realistic human typing. Perfect for automating text input, creating engaging demonstrations, testing applications, or any scenario where you need programmatic keyboard input with a natural feel.

## ✨ Key Features

- 🎯 **Human-like typing simulation** with random delays between keystrokes
- 🔥 **Multiple trigger methods**: delay-based or hotkey-based activation
- ⚡ **Configurable typing speed** from instant to slow human-like pace
- 📝 **Flexible newline handling**: Choose between Enter or Alt+Enter for line breaks
- 📁 **File input support** for typing longer texts
- 🔒 **Thread-safe operation** with graceful shutdown
- 🌍 **Cross-platform compatibility** (Windows, macOS, Linux)

## 🚀 Quick Start

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/autotyper.git
   cd autotyper
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Dependencies

- `pyautogui==0.9.54` - For keyboard simulation
- `keyboard==0.13.5` - For hotkey detection and advanced keyboard control

### First Run

```bash
# Type "Hello, World!" after 5 seconds
python autotyper.py -t "Hello, World!" -d 5
```

## 📖 Usage Guide

### Basic Usage

```bash
# Type text after a delay
python autotyper.py -t "Hello, World!" -d 5

# Type text from a file
python autotyper.py -f message.txt -d 3

# Type text when hotkey is pressed
python autotyper.py -t "Triggered by hotkey" -k "ctrl+shift+t"
```

### ⚡ Speed Control

```bash
# Default speed (natural human typing)
python autotyper.py -t "Normal typing speed" -d 5

# Lightning fast typing
python autotyper.py -t "Super fast typing" --min-delay 0.01 --max-delay 0.02

# Slow, thoughtful typing
python autotyper.py -t "Slow typing" --min-delay 0.1 --max-delay 0.3 -d 5
```

### 📝 Newline Behavior

```bash
# Default: Alt+Enter for newlines (great for chat apps)
python autotyper.py -t "Line 1\nLine 2\nLine 3" -d 5

# Use regular Enter for newlines
python autotyper.py -t "Line 1\nLine 2\nLine 3" -d 5 --use-enter
```

## ⚙️ Command Line Options

```
usage: autotyper.py [-h] (-t TEXT | -f FILE) (-d DELAY | -k HOTKEY)
                    [--min-delay MIN_DELAY] [--max-delay MAX_DELAY]
                    [--use-enter]
```

### Required Arguments

| Option | Description |
|--------|-------------|
| `-t TEXT, --text TEXT` | Text to type directly |
| `-f FILE, --file FILE` | File containing text to type |

### Trigger Methods

| Option | Description |
|--------|-------------|
| `-d DELAY, --delay DELAY` | Delay in seconds before typing starts |
| `-k HOTKEY, --hotkey HOTKEY` | Hotkey to trigger typing (e.g., "ctrl+shift+t") |

### Optional Parameters

| Option | Default | Description |
|--------|---------|-------------|
| `--min-delay` | 0.02 | Minimum delay between keystrokes (seconds) |
| `--max-delay` | 0.05 | Maximum delay between keystrokes (seconds) |
| `--use-enter` | False | Use Enter instead of Alt+Enter for newlines |

## 🎯 Examples

### Basic Examples

```bash
# Type a simple message after 3 seconds
python autotyper.py -t "Hello from AutoTyper!" -d 3

# Type content from a file
python autotyper.py -f my_message.txt -d 5

# Wait for hotkey activation
python autotyper.py -t "Hotkey activated!" -k "ctrl+shift+t"
```

### Advanced Examples

#### 🏃 Speed Variations
```bash
# Ultra-fast typing for demos
python autotyper.py -t "Lightning fast demo!" --min-delay 0.005 --max-delay 0.015 -d 2

# Natural typing speed
python autotyper.py -t "This feels like real typing" -d 3

# Slow, thoughtful typing
python autotyper.py -t "Hmm... let me think..." --min-delay 0.2 --max-delay 0.5 -d 3

# Instant typing (almost no delay)
python autotyper.py -t "INSTANT!" --min-delay 0 --max-delay 0.001 -d 1
```

#### 📝 Multi-line Text
```bash
# Chat application (Alt+Enter for new lines)
python autotyper.py -t "Hey!\nHow are you?\nLet's catch up soon!" -d 3

# Regular text editor (Enter for new lines)
python autotyper.py -t "Line 1\nLine 2\nLine 3" -d 3 --use-enter

# Code snippet with proper formatting
python autotyper.py -t "def hello():\n    print('Hello, World!')\n    return True" -d 5 --use-enter
```

#### 🎮 Hotkey Examples
```bash
# Gaming macro
python autotyper.py -t "/gamecommand activate" -k "f1"

# Quick response
python autotyper.py -t "Thank you for contacting support!" -k "ctrl+alt+1"

# Code snippet insertion
python autotyper.py -t "if __name__ == '__main__':\n    main()" -k "ctrl+shift+m" --use-enter
```

### 📄 File Input Examples

**Example 1: Email Template**

Create `email_template.txt`:
```
Dear Customer,

Thank you for your recent purchase!

We appreciate your business and hope you enjoy your new product.
If you have any questions, please don't hesitate to contact us.

Best regards,
The AutoTyper Team
```

Run:
```bash
python autotyper.py -f email_template.txt -d 3
```

**Example 2: Code Template**

Create `code_template.txt`:
```python
class MyClass:
    def __init__(self):
        self.data = []
    
    def add_item(self, item):
        self.data.append(item)
    
    def get_items(self):
        return self.data
```

Run:
```bash
python autotyper.py -f code_template.txt -d 5 --use-enter
```

## 💡 Real-World Use Cases

### 🎥 **Live Demonstrations**
- Create engaging coding tutorials with realistic typing
- Show step-by-step command execution in presentations
- Simulate user interaction for software demos

### 🧪 **Testing & QA**
- Automated testing of form inputs
- Stress testing text fields with various input speeds
- Testing chat applications and messaging systems
- Validating keyboard shortcuts and input handling

### 🤖 **Automation**
- Fill repetitive forms automatically
- Insert frequently used text snippets
- Automate data entry tasks
- Create macros for gaming or applications

### 💬 **Communication**
- Type in chat applications with proper formatting
- Send pre-written responses quickly
- Insert email templates or signatures
- Type in applications that don't support copy-paste

### 👨‍🏫 **Education**
- Create typing tutorials
- Demonstrate programming concepts live
- Show command-line operations step by step
- Make interactive coding workshops

## 🎹 Hotkey Reference

### Common Combinations

| Hotkey | Description | Example Use Case |
|--------|-------------|------------------|
| `ctrl+shift+t` | Custom trigger | General purpose macro |
| `ctrl+alt+1-9` | Number combinations | Quick responses 1-9 |
| `f1-f12` | Function keys | Gaming macros, shortcuts |
| `alt+space` | Alt + Space | Window management |
| `ctrl+shift+letter` | Letter combinations | Application-specific |

### Platform-Specific Notes

- **Windows**: All combinations work as expected
- **macOS**: Use `cmd` instead of `ctrl` for some combinations
- **Linux**: May need to run with elevated permissions

## 🛡️ Safety & Security

### Built-in Safety Features

- **🛑 Graceful Shutdown**: Press `Ctrl+C` to stop typing immediately
- **🔐 Thread-safe Operation**: Multiple hotkeys won't cause conflicts
- **🚪 ESC to Exit**: In hotkey mode, press `ESC` to cleanly exit
- **🖱️ No Mouse Interference**: Mouse movement won't interrupt typing

### Best Practices

1. **Test First**: Always test with a small delay in a safe environment
2. **Use Delays**: Give yourself time to position the cursor
3. **Know Your Hotkeys**: Avoid conflicts with system shortcuts
4. **Monitor Output**: Watch what's being typed to ensure accuracy

## 🔧 Troubleshooting

### Common Issues & Solutions

#### ❌ **"Module not found" Error**
```bash
# Solution: Install dependencies
pip install -r requirements.txt

# Or install manually
pip install pyautogui==0.9.54 keyboard==0.13.5
```

#### ❌ **Permission Denied (Linux/macOS)**
```bash
# Option 1: Run with sudo
sudo python autotyper.py -t "test" -d 3

# Option 2: Add user to input group (Linux)
sudo usermod -a -G input $USER
# Then logout and login again
```

#### ❌ **Hotkeys Not Working**

1. **Check for conflicts**: Ensure no other app uses the same hotkey
2. **Try simple keys first**: `f1`, `f2`, etc.
3. **Use different combinations**: `ctrl+alt+key` often works best
4. **Run as administrator** (Windows) or with `sudo` (Linux/macOS)

#### ❌ **Typing in Wrong Window**

- Increase delay to give more time to switch windows
- Use hotkey mode for better control
- Click the target window during the delay period

### 🚀 Performance Optimization

| Use Case | Min Delay | Max Delay | Notes |
|----------|-----------|-----------|-------|
| **Ultra Fast** | 0 | 0.001 | Nearly instant |
| **Demo/Presentation** | 0.05 | 0.1 | Readable speed |
| **Natural Typing** | 0.02 | 0.05 | Default, realistic |
| **Slow & Deliberate** | 0.1 | 0.3 | For emphasis |

### 🐛 Debug Mode

If you're having issues, try these debug steps:

```bash
# Test with simple text and long delay
python autotyper.py -t "test" -d 10

# Test hotkey detection
python autotyper.py -t "hotkey works" -k "f1"

# Test file reading
echo "file test" > test.txt
python autotyper.py -f test.txt -d 5
```

## 🔬 Technical Details

### Architecture

- **Single-file Design**: All functionality in one Python file for portability
- **Object-Oriented**: Clean `AutoTyper` class encapsulation
- **Event-Driven**: Thread-safe hotkey handling with proper cleanup
- **No External Config**: All settings via command-line arguments

### Implementation Details

```python
# Core typing algorithm
for char in text:
    if char == '\n':
        keyboard.press_and_release('alt+enter')  # or 'enter'
    else:
        keyboard.write(char)
    time.sleep(random.uniform(min_delay, max_delay))
```

### Key Features Explained

1. **Human-like Delays**: Random delay between each keystroke
2. **Smart Newline Handling**: Adapts to different application needs
3. **Thread Safety**: Prevents race conditions in hotkey mode
4. **Cross-platform Compatibility**: Works across all major OS

### Performance Characteristics

- **Memory Usage**: Minimal (~10-20 MB)
- **CPU Usage**: Negligible during delays
- **Max Text Length**: Limited only by system memory
- **Typing Speed**: 0-1000+ characters per second

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Acknowledgments

- Built with [PyAutoGUI](https://github.com/asweigart/pyautogui) and [keyboard](https://github.com/boppreh/keyboard)
- Inspired by the need for better typing automation

---

<p align="center">
  Made with ❤️ for the automation community
</p>