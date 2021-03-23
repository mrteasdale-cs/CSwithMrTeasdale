package com.snake;

import com.snake.templates.AbstractCell;
import java.awt.Graphics;


/**
 * Class representing a square cell
 * @author Sean
 */
public class Cell extends AbstractCell {

   // Declare your fields here

	public Cell(int sideSize, int row, int col) {
       // TODO Create a field (private variable in the class) for each of
       // the parameters
       // You can assign it in the following way:
       // this.sideSize = sideSize;
	}

    /**
     * Draw the current cell. This method needs to be called from BoardUI so
     * that it has access to a Graphics object. This will be explained in the
     * worksheet.
     */
	public void drawCell(Graphics g) {

        // Set color with (eg) g.setColor(Color.RED);

        // To draw (and colour in) a rectangle on the screen, we can use:
        // g.fillRect(x, y, width, height);

    }
}