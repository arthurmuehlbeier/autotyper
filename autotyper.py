#!/usr/bin/env python3
"""
AutoTyper - A human-like text typing simulator
"""

import time
import random
import argparse
import sys
import threading
from typing import Optional
import pyautogui
import keyboard


class AutoTyper:
    def __init__(self, text: str, min_delay: float = 0.02, max_delay: float = 0.05, use_alt_enter: bool = True):
        """
        Initialize AutoTyper with text and typing delays.
        
        Args:
            text: The text to type
            min_delay: Minimum delay between keystrokes (in seconds)
            max_delay: Maximum delay between keystrokes (in seconds)
            use_alt_enter: If True, use Alt+Enter for newlines; if False, use Enter
        """
        self.text = text
        self.min_delay = min_delay
        self.max_delay = max_delay
        self.use_alt_enter = use_alt_enter
        self.typing_thread: Optional[threading.Thread] = None
        self.stop_typing = threading.Event()
        
        # Disable pyautogui failsafe (moving mouse to corner won't stop it)
        pyautogui.FAILSAFE = False
        
    def type_text(self):
        """Type the text with human-like delays between characters."""
        # Type character by character with delays
        for char in self.text:
            if self.stop_typing.is_set():
                break
                
            # Handle newline based on configuration
            if char == '\n':
                if self.use_alt_enter:
                    keyboard.press_and_release('alt+enter')
                else:
                    keyboard.press_and_release('enter')
            else:
                keyboard.write(char)
            
            # Add human-like delay between characters
            delay = random.uniform(self.min_delay, self.max_delay)
            time.sleep(delay)
    
    def start_typing_with_delay(self, delay: float):
        """Start typing after a specified delay."""
        print(f"Waiting {delay} seconds before typing...")
        time.sleep(delay)
        print("Starting to type...")
        self.type_text()
        print("\nTyping completed!")
    
    def start_typing_with_hotkey(self, hotkey: str):
        """Wait for hotkey press and then start typing."""
        print(f"Press '{hotkey}' to start typing (ESC to cancel)...")
        
        def on_hotkey():
            if self.typing_thread and self.typing_thread.is_alive():
                print("\nAlready typing!")
                return
                
            print("\nStarting to type...")
            self.typing_thread = threading.Thread(target=self.type_text)
            self.typing_thread.start()
        
        # Register hotkey
        keyboard.add_hotkey(hotkey, on_hotkey)
        
        # Wait for ESC to exit
        keyboard.wait('esc')
        self.stop_typing.set()
        
        if self.typing_thread and self.typing_thread.is_alive():
            self.typing_thread.join()
            
        print("\nExiting...")


def main():
    parser = argparse.ArgumentParser(
        description="AutoTyper - Simulates human-like typing of text",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    # Text input options
    text_group = parser.add_mutually_exclusive_group(required=True)
    text_group.add_argument('-t', '--text', help='Text to type')
    text_group.add_argument('-f', '--file', help='File containing text to type')
    
    # Trigger options
    trigger_group = parser.add_mutually_exclusive_group(required=True)
    trigger_group.add_argument('-d', '--delay', type=float, 
                              help='Delay in seconds before typing starts')
    trigger_group.add_argument('-k', '--hotkey', 
                              help='Hotkey to trigger typing (e.g., "ctrl+shift+t")')
    
    # Typing speed options
    parser.add_argument('--min-delay', type=float, default=0.02,
                       help='Minimum delay between keystrokes (default: 0.02)')
    parser.add_argument('--max-delay', type=float, default=0.05,
                       help='Maximum delay between keystrokes (default: 0.05)')
    
    # Newline behavior options
    parser.add_argument('--use-enter', action='store_true',
                       help='Use Enter for newlines instead of Alt+Enter (default: Alt+Enter)')
    
    args = parser.parse_args()
    
    # Get text
    if args.text:
        text = args.text
    else:
        try:
            with open(args.file, 'r', encoding='utf-8') as f:
                text = f.read()
        except FileNotFoundError:
            print(f"Error: File '{args.file}' not found")
            sys.exit(1)
        except Exception as e:
            print(f"Error reading file: {e}")
            sys.exit(1)
    
    # Validate delays
    if args.min_delay < 0 or args.max_delay < 0:
        print("Error: Delays must be positive")
        sys.exit(1)
    
    if args.min_delay > args.max_delay:
        print("Error: min-delay must be less than or equal to max-delay")
        sys.exit(1)
    
    # Create AutoTyper instance
    typer = AutoTyper(text, args.min_delay, args.max_delay, use_alt_enter=not args.use_enter)
    
    # Start typing based on trigger method
    try:
        if args.delay is not None:
            typer.start_typing_with_delay(args.delay)
        else:
            typer.start_typing_with_hotkey(args.hotkey)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        sys.exit(0)


if __name__ == "__main__":
    main()