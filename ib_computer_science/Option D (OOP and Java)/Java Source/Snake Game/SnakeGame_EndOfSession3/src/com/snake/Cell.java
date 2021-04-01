package com.snake;

import com.snake.templates.AbstractCell;
import java.awt.Color;
import java.awt.Graphics;

/**
 * Class representing a square cell
 *
 * @author Sean
 */
public class Cell extends AbstractCell {

   // Declare your fields here
   private int sideSize, row, col;
   private CellType type = CellType.EMPTY;
   private Direction dir = Direction.NONE;

   public Cell(int sideSize, int row, int col) {
      this.sideSize = sideSize;
      this.row = row;
      this.col = col;
   }

   /**
    * Draw the current cell. This method needs to be called from BoardUI so that
    * it has access to a Graphics object. This will be explained in the
    * worksheet.
    */
   public void drawCell(Graphics g) {
      Color bg = Color.GREEN.darker().darker().darker();

      // Create a Cell of the correct colour, depending
      // on which type the Cell is
      switch (type) {
         case EMPTY:
            fillCell(g, bg);
            break;
         case HEAD:
            fillCell(g, Color.GREEN);
            break;
         case BODY:
            fillCell(g, Color.GREEN.darker());
            break;
         case TAIL:
            fillCell(g, Color.GREEN.darker());
            break;
         case FOOD:
            fillCell(g, Color.RED);
            break;
      }

   }

   /**
    * Actually fill in the Cell with the specified colour
    */
   private void fillCell(Graphics g, Color color) {
      
      // Set color with (eg) g.setColor(Color.RED);
      g.setColor(color);
      
      // To draw (and colour in) a rectangle on the screen, we can use:
      // g.fillRect(x, y, width, height);
      int xVal = (col * sideSize);
      int yVal = (row * sideSize);

      g.fillRect(xVal, yVal, sideSize, sideSize);
      g.setColor(color.brighter());
      g.drawRect(xVal, yVal, sideSize, sideSize);
   }

   /**
    * Return the type of Cell this object is
    */
   public CellType getType() {
      return type;
   }

   /**
    * Set the type of Cell this object is
    */
   public void setType(CellType type) {
      this.type = type;
   }

   /**
    * Set the direction of the Cell - should be NONE for empty Cells
    */
   public void setDirection(Direction direction) {
      dir = direction;
   }

   /**
    * Get the direction of the current cell
    */
   public Direction getDirection() {
      return dir;
   }

   /**
    * Get the row index of the current cell
    */
   public int getRow() {
      return row;
   }

   /**
    * Get the column index of the current cell
    */
   public int getCol() {
      return col;
   }
}