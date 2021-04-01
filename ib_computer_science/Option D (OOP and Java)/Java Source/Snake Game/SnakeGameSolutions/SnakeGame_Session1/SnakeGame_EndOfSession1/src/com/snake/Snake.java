package com.snake;

import com.snake.templates.AbstractSnake;

public class Snake extends AbstractSnake {

   private final Board board;

   public Snake(Board board) {
      this.board = board;
   }

   /**
    * Place the Snake on the board
    */
   public void place() {
      board.getCell(0, 2).setType(CellType.HEAD);
      board.getCell(0, 1).setType(CellType.BODY);
      board.getCell(0, 0).setType(CellType.TAIL);
   }
}
