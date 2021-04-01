package com.snake.ui;

import com.snake.Board;
import java.awt.Color;
import java.awt.Graphics;
import javax.swing.JPanel;

public class BoardUI extends JPanel {
	
   private static final long serialVersionUID = 1L;
	
	public BoardUI (Board board, int rows, int cols) {
		setBackground(Color.GRAY);
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

        // Add your code here
	}

}
