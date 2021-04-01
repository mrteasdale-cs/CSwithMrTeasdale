package com.snake;

import com.snake.templates.AbstractSnake;
import com.snake.ui.ScoreBar;
import java.util.ArrayList;
import java.util.List;

/**
 * Class representing the Snake in the game, tracking each of its body parts
 */
public class Snake extends AbstractSnake {

   private final Board board;
   // The direction of the head- this can be changed by keyboard input
   private Direction dir = Direction.EAST;
   // Keep track of the Snake parts
   private Cell head;
   private List<Cell> body = new ArrayList<Cell>();
   private Cell tail;
   private int score = 0;

   public Snake(Board board) {
      this.board = board;
   }

   /**
    * Place the Snake on the board
    */
   public void place() {
      head = board.getCell(0, 2);
      head.setType(CellType.HEAD);
      head.setDirection(dir);

      Cell body = board.getCell(0, 1);
      body.setType(CellType.BODY);
      body.setDirection(dir);
      this.body.add(body);
      // Notice we use .add() method to add to the list

      tail = board.getCell(0, 0);
      tail.setType(CellType.TAIL);
      tail.setDirection(dir);
   }

   /**
    * Set the direction for the next game move
    */
   public void setDirection(Direction dir) {
      this.dir = dir;
   }

   /**
    * Actually move the Snake, based on the current direction of existing Snake
    * cells, and the dir field.
    */
   public synchronized void move() throws GameOverException {
      head = moveCell(head, CellType.HEAD);

      for (int i = 0; i < body.size(); i++) {
         Cell bodyCell = body.get(i);
         // Replace the body cell with the new one
         body.set(i, moveCell(bodyCell, CellType.BODY));
      }

      tail = moveCell(tail, CellType.TAIL);

      board.getBoardUI().repaint();
   }

   private Cell moveCell(Cell cell, CellType type) throws GameOverException {
      int row = cell.getRow();
      int col = cell.getCol();
      Direction dir = cell.getDirection();

      // Reset the current Cell to be empty
      cell.setType(CellType.EMPTY);
      cell.setDirection(Direction.NONE);

      switch (dir) {
         case NORTH:
            row--;
            break;
         case EAST:
            col++;
            break;
         case WEST:
            col--;
            break;
         case SOUTH:
            row++;
            break;
      }

      if (type == CellType.HEAD) {
         checkCollision(row, col);
      }


      Cell newCell = board.getCell(row, col);
      newCell.setType(type);
      newCell.setDirection(dir);

      return newCell;
   }

   public void checkCollision(int row, int col) throws GameOverException {
      Cell cell = board.getCell(row, col);
      if (cell.getType() == CellType.FOOD) {
         score += 10;
         ScoreBar.getInstance().setScoreLabel(score);

         body.add(tail);
         body.get(body.size()-1).setType(CellType.BODY);

         board.placeFood();
      } else if (cell.getType() != CellType.EMPTY) {
         throw new GameOverException(board, "Collision detected!");
      }
   }

   public void updateDirections() {
      // Update tail
      Cell lastBodyCell = body.get(body.size() - 1);
      tail.setDirection(lastBodyCell.getDirection());

      // Update body
      for (int i = body.size() - 1; i > 0; i--) {
         Cell currentBodyCell = body.get(i);
         currentBodyCell.setDirection(body.get(i - 1).getDirection());
      }
      body.get(0).setDirection(head.getDirection());

      // Update head
      head.setDirection(dir);
   }
}
