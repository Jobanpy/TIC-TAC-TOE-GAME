# TIC-TAC-TOE-GAME

Tic‑Tac‑Toe Console Application

Team Members: Harjoban Singh Jawanda and Komalpreet Kaur

Project Overview

This application provides a reliable, console‑based implementation of the traditional Tic‑Tac‑Toe game for two participants. Developed in Python, it delivers a straightforward text interface, rigorous input validation, and comprehensive game‑state management to ensure correct turn sequencing and accurate determination of win or draw outcomes.

Objectives

The purpose of this project is to enable two players to alternate placing their markers (“X” or “O”) on a 3×3 grid. The first player to align three of their own markers—horizontally, vertically, or diagonally—achieves victory. Should all nine positions be filled without a winning alignment, the application declares a draw.

Gameplay Mechanics


Turn Sequencing: Participants input a position number (1–9) to indicate where their marker should be placed.

Input Validation: The system rejects any input that is non‑numeric, falls outside the permitted range, or targets an already occupied cell, providing a clear explanatory message in each case.

Board Rendering: After each valid move, the current grid state is displayed in a clean ASCII format.

Victory Detection: Following every turn, the program evaluates all possible row, column, and diagonal alignments to determine if either player has secured three consecutive markers.

Draw Detection: If no winning alignment is detected and no empty cells remain, the game concludes in a draw.

Replay Prompt: Upon game completion, users are prompted to initiate a new session or exit the application.

Key Features


Robust Input Handling: Ensures only valid, in‑range, and unoccupied moves are accepted, thus preventing invalid state transitions.

Encapsulated Game Logic: Implements win and draw conditions within dedicated functions, promoting code clarity and maintainability.

Uncluttered Console Interface: Offers an intuitive representation of the game board after each move, enhancing user comprehension.

Session Management: Supports repeated playthroughs without restarting the program, enabling uninterrupted user engagement.

Technology Stack


Programming Language: Python 3.x

Execution Environment: Standard terminal or command‑line interface

Dependencies: None beyond Python’s standard library

Future Enhancements


Integrate a single‑player mode featuring an AI opponent, potentially using the minimax algorithm.

Develop a graphical user interface leveraging libraries such as Pygame or Tkinter.

Implement persistent storage of game outcomes and player statistics between sessions.

Extend the application to support variable grid sizes (e.g., 4×4, 5×5) and configurable win‑length requirements.

📞 Contact

Harjoban Singh 

📧 hjawanda@norquest.ca

📞 +1 (780)-224-0890
