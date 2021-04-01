package com.snake;

import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

/**
 *	Handles keyboard events for the Snake game
 */
public class SnakeKeyAdapter implements KeyListener {
	
	// Board field
	private Board board;
	
	// SnakeKeyAdapter constructor method
	public SnakeKeyAdapter(Board board) {
		this.board = board;
	}

	// This method is called every time you press a key on the keyboard!
	@Override
	public void keyPressed(KeyEvent e) {
		
		// Get the key that was pressed - Java does this by assigning each key
		// to a number
		int keycode = e.getKeyCode();
		
		// Get the snake
		Snake snake = (Snake) board.getSnake();
		
		if (keycode == KeyEvent.VK_ENTER) {
			board.start();
            board.getBoardUI().repaint();
			return;
		}
		
		// Close the program if the user presses ESC
		if (keycode == KeyEvent.VK_ESCAPE) {
			System.exit(0);
		}
		
		
		if (keycode == KeyEvent.VK_UP) {
			snake.setDirection(Direction.NORTH);
		} else if (keycode == KeyEvent.VK_RIGHT) {
			snake.setDirection(Direction.EAST);
		} else if (keycode == KeyEvent.VK_DOWN) {
			snake.setDirection(Direction.SOUTH);
		} else if (keycode == KeyEvent.VK_LEFT) {
			snake.setDirection(Direction.WEST);
		}
	}
	
	// Ignore the following methods, they aren't used.
	@Override
	public void keyTyped(KeyEvent e) {}

	@Override
	public void keyReleased(KeyEvent e) {}

}
