package com.snake.ui;

import com.snake.Board;
import com.snake.Cell;
import java.awt.Color;
import java.awt.Graphics;
import javax.swing.JPanel;

public class BoardUI extends JPanel {
	
   private static final long serialVersionUID = 1L;

   private Board board;
   private int rows, cols;
	
	public BoardUI (Board board, int rows, int cols) {
		setBackground(Color.GRAY);

        this.board = board;
        this.rows = rows;
        this.cols = cols;
	}
	
	/**
	 * This is a method used to draw the JPanel object on the screen.
	 * We can override this method from the superclass (JPanel)
	 * so our own code is called when BoardUI is drawn on screen.
     *
     * We don't do anything special just yet, but you will add to this
     * method later!
	 */
	@Override
	protected void paintComponent(Graphics g) {
		super.paintComponent(g);

        // Loop through all the different Cells, and draw them
        for (int row = 0; row < rows; row++) {
           for (int col = 0; col < cols; col++) {
              Cell cell = board.getCell(row, col);
              cell.drawCell(g);
           }
        }
	}

}
