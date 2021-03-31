package com.snake;

import com.snake.templates.AbstractBoard;
import com.snake.ui.BoardUI;

/**
 * This is a class representing the game board for our Snake game TEST one two
 */
public class Board extends AbstractBoard {
	
	private BoardUI ui = null;
	private int rows;
	private int cols;

    // This variable will hold the actual grid behind the game board!
    // Notice it is made up of 'Cell' objects, a custom class that we
    // will be extending!
    private Cell[][] grid;
	
	public Board(int cellSize, int rows, int cols) {
		this.rows = rows;
		this.cols = cols;

        // Add code here for Task 2 to set up the grid array
        
	}

    /**
     * This method is called when the Snake game starts. We will implement this
     * later
     */
    public void start() {
	}

    /**
     * When this method is first called, it will create a new
     * BoardUI object, and every time after that it will use the
     * already created object.
     *
     * @return BoardUI object.
     */
    public BoardUI getBoardUI() {
		if (ui == null) {
			ui = new BoardUI(this, rows, cols);
		}
		return ui;
	}

}